"""Data request from ESO Logs API."""

import asyncio
from typing import Dict, List, Optional, Sequence, Tuple

from analysis.tracked_info import TrackedInfo
from data.core import Stack
from esologs.api import ApiWrapper
from esologs.responses.report_data.casts import CastsTableData
from esologs.responses.report_data.effects import EffectsTableData
from esologs.responses.report_data.graph import GraphData
from gql.dsl import DSLField  # type: ignore
from loguru import logger


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
        target: Optional[Tuple[int]] = None,
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
        self.graphs: List[GraphData] = []

    async def execute(self):
        """Query generation and execution."""
        buffs = asyncio.create_task(self._request_buffs())
        debuffs = asyncio.create_task(self._request_debuffs())
        damage_done = asyncio.create_task(self._request_damage_done())
        graphs = asyncio.create_task(self._request_graphs())
        await asyncio.gather(buffs, debuffs, damage_done, graphs)
        self.total_time = (
            self.buffs_table.total_time
            or self.debuffs_table.total_time
            or self.damage_done_table.total_time
        )

    def _generate_filter(
        self, ability_ids: Sequence[int], targets: Optional[Tuple[int]] = None,
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
            data_type='Buffs',
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
            data_type='Debuffs',
            start_time=self._start_time,
            end_time=self._end_time,
            hostility_type='Enemies',
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
            data_type='DamageDone',
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

        graphs = await self._partial_graphs(simple_stacks)
        response = await self._api.query_graph(
            log=self._log,
            char_id=self._char_id,
            start_time=self._start_time,
            end_time=self._end_time,
            graphs=graphs,
        )
        response = response.get('reportData')
        response = response.get('report')

        for raw_graph in response.values():
            self.graphs.append(GraphData.from_dict(raw_graph.get('data')))
        logger.info('Got {0} graphs'.format(len(self.graphs)))

    async def _partial_graphs(
        self, stacks: List[Stack],
    ) -> Dict[str, DSLField]:
        stacks_dict = {}
        for stack in stacks:
            data_type = 'Buffs' if stack.type_ == 'Buff' else 'Debuffs'
            hostility = 'Friendlies' if stack.type_ == 'Buff' else 'Enemies'
            stacks_dict.update(
                await self._api.partial_query_graph(
                    char_id=self._char_id,
                    data_type=data_type,
                    start_time=self._start_time,
                    end_time=self._end_time,
                    ability_id=stack.id,
                    hostility_type=hostility,
                ),
            )
        return stacks_dict
