"""Data request from ESO Logs API."""

import asyncio
from typing import TYPE_CHECKING

from structlog.stdlib import get_logger

from esoraider_server.data.passives import Passives
from esoraider_server.esologs.api import ApiWrapper
from esoraider_server.esologs.consts import DataType, HostilityType

if TYPE_CHECKING:
    from collections.abc import Sequence

    from gql.dsl import DSLField

    from esoraider_server.analysis.tracked_info import TrackedInfo
    from esoraider_server.data.core import Stack
    from esoraider_server.esologs.responses.report_data.casts import (
        CastsTableData,
    )
    from esoraider_server.esologs.responses.report_data.effects import (
        Aura,
        EffectsTableData,
    )
    from esoraider_server.esologs.responses.report_data.graph import GraphData

logger = get_logger()


class DataRequest:
    """Generates and executes ESO Logs API queries based on data to track."""

    def __init__(
        self,
        api: ApiWrapper,
        log: str,
        fight_id: int,
        tracked_info: 'TrackedInfo',
        start_time: int = 0,
        end_time: int = 0,
        char_id: int | None = None,
        target: 'Sequence[int] | None' = None,
    ) -> None:
        self._api = api

        self._log = log
        self._fight_id = fight_id
        self._start_time = start_time
        self._end_time = end_time
        self._char_id = char_id
        self._target = target

        self._tracked_info = tracked_info

        self.total_time = self._end_time - self._start_time
        self.buffs_table: EffectsTableData | None = None
        self.debuffs_table: EffectsTableData | None = None
        self.damage_done_table: CastsTableData | None = None
        self.graphs: dict[int, GraphData] = {}
        self.passives: list[Aura] = []

    async def execute(self):
        """Query generation and execution."""
        if not self._start_time or not self._end_time:
            start, end = await self._api.query_fight_times(
                self._log, self._fight_id
            )
            self._start_time = start
            self._end_time = end
            self.total_time = self._end_time - self._start_time

        await asyncio.gather(
            asyncio.create_task(self._request_buffs()),
            asyncio.create_task(self._request_debuffs()),
            asyncio.create_task(self._request_damage_done()),
            asyncio.create_task(self._request_graphs()),
            asyncio.create_task(self._request_passives()),
        )

    def _generate_filter(
        self,
        ability_ids: 'Sequence[int]',
        targets: 'Sequence[int] | None' = None,
    ):
        if targets:
            return 'ability.id IN ({}) AND target.id IN ({})'.format(
                ', '.join(map(str, ability_ids)),
                ', '.join(map(str, targets)),
            )
        return 'ability.id IN ({})'.format(', '.join(map(str, ability_ids)))

    async def _request_buffs(self):
        if not self._tracked_info.buffs or self.buffs_table:
            await logger.ainfo('Skipping Buffs table request')
            return

        buff_ids = {bf.id for bf in self._tracked_info.buffs}

        await logger.ainfo('Requesting buffs table from API')
        self.buffs_table = await self._api.query_table(
            log=self._log,
            fight_id=self._fight_id,
            data_type=DataType.BUFFS,
            start_time=self._start_time,
            end_time=self._end_time,
            source_id=self._char_id,
            filter_exp=self._generate_filter(buff_ids),
        )

        await logger.ainfo(f'Got {len(self.buffs_table.auras)} buffs')
        for aura in self.buffs_table.auras:
            await logger.adebug(f'{aura.name} - {aura.guid}')

    async def _request_debuffs(self):
        if not self._tracked_info.debuffs or self.debuffs_table:
            await logger.ainfo('Skipping Debuffs table request')
            return

        debuff_ids = {db.id for db in self._tracked_info.debuffs}

        await logger.ainfo('Requesting debuffs table from API')
        self.debuffs_table = await self._api.query_table(
            log=self._log,
            fight_id=self._fight_id,
            data_type=DataType.DEBUFFS,
            start_time=self._start_time,
            end_time=self._end_time,
            hostility_type=HostilityType.ENEMIES,
            target_id=self._char_id,
            filter_exp=self._generate_filter(debuff_ids, self._target),
        )

        await logger.ainfo(f'Got {len(self.debuffs_table.auras)} debuffs')
        for aura in self.debuffs_table.auras:
            await logger.adebug(f'{aura.name} - {aura.guid}')

    async def _request_damage_done(self):
        if not self._tracked_info.skills or self.damage_done_table:
            await logger.ainfo('Skipping Damage Done table request')
            return

        ids = set()
        for skill in self._tracked_info.skills:
            ids.add(skill.id)
            if skill.children:
                for child in skill.children:
                    ids.add(child.id)

        await logger.ainfo('Requesting DamageDone table from API')
        self.damage_done_table = await self._api.query_table(
            log=self._log,
            fight_id=self._fight_id,
            data_type=DataType.DAMAGE_DONE,
            start_time=self._start_time,
            end_time=self._end_time,
            source_id=self._char_id,
            filter_exp=self._generate_filter(ids, self._target),
        )

        await logger.ainfo(
            f'Got {len(self.damage_done_table.entries)} casts',
        )
        for cast in self.damage_done_table.entries:
            await logger.adebug(f'{cast.name} - {cast.guid}')

    async def _request_graphs(self):
        if not self._tracked_info.stacks or self.graphs:
            await logger.ainfo('Skipping Graphs request')
            return

        simple_stacks = [
            # Excluding 'complex' stacks which rely on buffs / debuffs
            stack
            for stack in self._tracked_info.stacks
            if not stack.buffs and not stack.debuffs
        ]
        if not simple_stacks:
            return

        self.graphs = await self._api.query_graph(
            log=self._log,
            char_id=self._char_id,
            start_time=self._start_time,
            end_time=self._end_time,
            graphs=await self._partial_graphs(simple_stacks),
        )

        await logger.ainfo(f'Got {len(self.graphs)} graphs')

    async def _partial_graphs(
        self, stacks: list['Stack']
    ) -> dict[str, 'DSLField']:
        stacks_dict = {}
        for stack in stacks:
            hostility = HostilityType.FRIENDLIES
            if stack.type_ == DataType.DEBUFFS:
                hostility = HostilityType.ENEMIES
            stacks_dict.update(
                await self._api.partial_query_graph(
                    char_id=self._char_id,
                    data_type=stack.type_,
                    start_time=self._start_time,
                    end_time=self._end_time,
                    ability_id=stack.id,
                    hostility_type=hostility,
                ),
            )
        return stacks_dict

    async def _request_passives(self):
        if not self._tracked_info.skills or self.passives:
            await logger.ainfo('Skipping passives request')
            return

        await logger.ainfo('Requesting Events list with passives from API')
        events = await self._api.query_events(
            log=self._log,
            char_id=self._char_id,
            start_time=self._start_time,
            end_time=self._end_time,
        )

        await logger.ainfo('Requesting Buffs table with passives from API')
        weapon_passive_ids = [
            passive.id
            for passive in (
                # Next passives are not included in combatant info from events
                # TODO: Add a special flag to buff dataclass?
                Passives.TRI_FOCUS.value,
                Passives.PENETRATING_MAGIC.value,
                Passives.ANCIENT_KNOWLEDGE.value,
                Passives.DESTRUCTION_EXPERT.value,
                Passives.FORCEFUL.value,
                Passives.FOLLOW_UP.value,
                Passives.HAWK_EYE.value,
            )
        ]
        buffs = await self._api.query_table(
            log=self._log,
            fight_id=self._fight_id,
            data_type=DataType.BUFFS,
            start_time=self._start_time,
            end_time=self._end_time,
            source_id=self._char_id,
            filter_exp=self._generate_filter(weapon_passive_ids),
        )

        self.passives.extend(
            [aura for event in events for aura in event.auras],
        )
        self.passives.extend(list(buffs.auras))

        await logger.ainfo(f'Got {len(self.passives)} passives')
