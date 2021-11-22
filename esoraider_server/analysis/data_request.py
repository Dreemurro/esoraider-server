"""Data request from ESO Logs API."""

import asyncio
from typing import Dict, List, Optional, Sequence

from gql.dsl import DSLField  # type: ignore
from loguru import logger

from esoraider_server.analysis.tracked_info import TrackedInfo
from esoraider_server.data.core import Stack
from esoraider_server.data.passives import Passives
from esoraider_server.esologs.api import ApiWrapper
from esoraider_server.esologs.consts import DataType, HostilityType
from esoraider_server.esologs.responses.report_data.casts import CastsTableData
from esoraider_server.esologs.responses.report_data.effects import (
    Aura,
    EffectsTableData,
)
from esoraider_server.esologs.responses.report_data.graph import GraphData


class DataRequest(object):
    """Generates and executes ESO Logs API queries based on data to track."""

    def __init__(
        self,
        api: ApiWrapper,
        log: str,
        fight_id: int,
        start_time: int,
        end_time: int,
        tracked_info: TrackedInfo,
        char_id: Optional[int] = None,
        target: Optional[Sequence[int]] = None,
    ) -> None:
        self._api = api

        self._log = log
        self._fight_id = fight_id
        self._start_time = start_time
        self._end_time = end_time
        self._char_id = char_id
        self._target = target

        self._tracked_info = tracked_info

        self.total_time: Optional[int] = None
        self.buffs_table: Optional[EffectsTableData] = None
        self.debuffs_table: Optional[EffectsTableData] = None
        self.damage_done_table: Optional[CastsTableData] = None
        self.graphs: Dict[int, GraphData] = {}
        self.passives: List[Aura] = []

    async def execute(self):
        """Query generation and execution."""
        await asyncio.gather(
            asyncio.create_task(self._request_buffs()),
            asyncio.create_task(self._request_debuffs()),
            asyncio.create_task(self._request_damage_done()),
            asyncio.create_task(self._request_graphs()),
            asyncio.create_task(self._request_passives()),
        )
        self.total_time = (
            self.buffs_table.total_time
            or self.debuffs_table.total_time
            or self.damage_done_table.total_time
        )

    def _generate_filter(
        self,
        ability_ids: Sequence[int],
        targets: Optional[Sequence[int]] = None,
    ):
        if targets:
            return 'ability.id IN ({0}) AND target.id IN ({1})'.format(
                ', '.join(map(str, ability_ids)),
                ', '.join(map(str, targets)),
            )
        return 'ability.id IN ({0})'.format(', '.join(map(str, ability_ids)))

    async def _request_buffs(self):
        if not self._tracked_info.buffs or self.buffs_table:
            logger.info('Skipping Buffs table request')
            return

        buff_ids = {bf.id for bf in self._tracked_info.buffs}

        logger.info('Requesting buffs table from API')
        self.buffs_table = await self._api.query_table(
            log=self._log,
            fight_id=self._fight_id,
            data_type=DataType.BUFFS,
            start_time=self._start_time,
            end_time=self._end_time,
            source_id=self._char_id,
            filter_exp=self._generate_filter(buff_ids),
        )

        logger.info('Got {0} buffs'.format(len(self.buffs_table.auras)))
        for aura in self.buffs_table.auras:
            logger.debug('{0} - {1}'.format(aura.name, aura.guid))

    async def _request_debuffs(self):
        if not self._tracked_info.debuffs or self.debuffs_table:
            logger.info('Skipping Debuffs table request')
            return

        debuff_ids = {db.id for db in self._tracked_info.debuffs}

        logger.info('Requesting debuffs table from API')
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

        logger.info('Got {0} debuffs'.format(len(self.debuffs_table.auras)))
        for aura in self.debuffs_table.auras:
            logger.debug('{0} - {1}'.format(aura.name, aura.guid))

    async def _request_damage_done(self):
        if not self._tracked_info.skills or self.damage_done_table:
            logger.info('Skipping Damage Done table request')
            return

        ids = set()
        for skill in self._tracked_info.skills:
            ids.add(skill.id)
            if skill.children:
                for child in skill.children:
                    ids.add(child.id)

        logger.info('Requesting DamageDone table from API')
        self.damage_done_table = await self._api.query_table(
            log=self._log,
            fight_id=self._fight_id,
            data_type=DataType.DAMAGE_DONE,
            start_time=self._start_time,
            end_time=self._end_time,
            source_id=self._char_id,
            filter_exp=self._generate_filter(ids, self._target),
        )

        logger.info(
            'Got {0} casts'.format(len(self.damage_done_table.entries)),
        )
        for cast in self.damage_done_table.entries:
            logger.debug('{0} - {1}'.format(cast.name, cast.guid))

    async def _request_graphs(self):
        if not self._tracked_info.stacks or self.graphs:
            logger.info('Skipping Graphs request')
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

        logger.info('Got {0} graphs'.format(len(self.graphs)))

    async def _partial_graphs(
        self, stacks: List[Stack],
    ) -> Dict[str, DSLField]:
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
            logger.info('Skipping passives request')
            return

        logger.info('Requesting Events list with passives from API')
        events = await self._api.query_events(
            log=self._log,
            char_id=self._char_id,
            start_time=self._start_time,
            end_time=self._end_time,
        )

        logger.info('Requesting Buffs table with passives from API')
        weapon_passive_ids = [
            passive.id for passive in (
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
            [aura for event in events for aura in event.auras]
        )
        self.passives.extend([aura for aura in buffs.auras])

        logger.info('Got {0} passives'.format(len(self.passives)))
