import asyncio
from typing import Dict, List, Set

from analysis.tracked_info import TrackedInfo
from api.api import ApiWrapper
from api.response import BuffsTableData, CastsTableData, GraphData
from data.core import Stack
from gql.dsl import DSLField
from loguru import logger


class DataRequest:
    def __init__(
        self,
        api: ApiWrapper,
        log: str,
        fight_id: int,
        start_time: int,
        end_time: int,
        char_id: int,
        tracked_info: TrackedInfo,
    ) -> None:
        self._api = api

        self._log = log
        self._fight_id = fight_id
        self._start_time = start_time
        self._end_time = end_time
        self._char_id = char_id

        self._tracked_info = tracked_info

        self.buffs_table: BuffsTableData = None
        self.debuffs_table: BuffsTableData = None
        self.damage_done_table: CastsTableData = None
        self.graphs: List[GraphData] = []

    async def execute(self):
        buffs = asyncio.create_task(self._request_buffs())
        debuffs = asyncio.create_task(self._request_debuffs())
        damage_done = asyncio.create_task(self._request_damage_done())
        graphs = asyncio.create_task(self._request_graphs())
        await asyncio.gather(buffs, debuffs, damage_done, graphs)

    def _generate_filter(self, ability_ids: Set[int]):
        return 'ability.id IN ({0})'.format(', '.join(map(str, ability_ids)))

    async def _request_buffs(self):
        if not self._tracked_info.buffs or self.buffs_table:
            return

        buff_ids = {bf.id for bf in self._tracked_info.buffs}
        filter_exp = self._generate_filter(buff_ids)

        logger.info('Requesting buffs table from API')
        logger.debug(filter_exp)

        response = await self._api.query_table(
            log=self._log,
            fight_id=self._fight_id,
            data_type='Buffs',
            start_time=self._start_time,
            end_time=self._end_time,
            source_id=self._char_id,
            filter_exp=filter_exp,
        )
        response = response.get('reportData')
        response = response.get('report')
        response = response.get('table')
        response = response.get('data')
        decoded = BuffsTableData.from_dict(response)

        for aura in decoded.auras:
            logger.debug(aura)

        self.buffs_table = decoded

    async def _request_debuffs(self):
        if not self._tracked_info.debuffs or self.debuffs_table:
            return

        debuff_ids = {db.id for db in self._tracked_info.debuffs}
        filter_exp = self._generate_filter(debuff_ids)

        logger.info('Requesting debuffs table from API')
        logger.debug(filter_exp)

        response = await self._api.query_table(
            log=self._log,
            fight_id=self._fight_id,
            data_type='Debuffs',
            start_time=self._start_time,
            end_time=self._end_time,
            target_id=self._char_id,
            hostility_type='Enemies',
            filter_exp=filter_exp,
        )

        response = response.get('reportData')
        response = response.get('report')
        response = response.get('table')
        response = response.get('data')
        decoded = BuffsTableData.from_dict(response)

        for aura in decoded.auras:
            logger.debug(aura)

        self.debuffs_table = decoded

    async def _request_damage_done(self):
        if self.damage_done_table:
            return

        ids = set()
        for skill in self._tracked_info.skills:
            ids.add(skill.id)
            if skill.children:
                for child in skill.children:
                    ids.add(child.id)

        filter_exp = self._generate_filter(ids)

        logger.info('Requesting DamageDone table from API')
        logger.debug(filter_exp)

        response = await self._api.query_table(
            log=self._log,
            fight_id=self._fight_id,
            data_type='DamageDone',
            start_time=self._start_time,
            end_time=self._end_time,
            source_id=self._char_id,
            filter_exp=filter_exp,
        )

        response = response.get('reportData')
        response = response.get('report')
        response = response.get('table')
        response = response.get('data')
        decoded = CastsTableData.from_dict(response)

        logger.info('Got {0} casts'.format(len(decoded.entries)))
        for cast in decoded.entries:
            logger.debug(cast)

        self.damage_done_table = decoded

    async def _request_graphs(self):
        if not self._tracked_info.stacks or self.graphs:
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

        decoded = []
        for raw_graph in response.values():
            decoded.append(GraphData.from_dict(raw_graph.get('data')))

        logger.info('Got {0} graphs'.format(len(decoded)))
        for graph in decoded:
            logger.debug(graph)

        self.graphs = decoded

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
