import asyncio
from typing import Set

from loguru import logger

from analysis.tracked_info import TrackedInfo
from api.api import ApiWrapper
from api.response import BuffsTableData, CastsTableData


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

    async def execute(self):
        buffs = asyncio.create_task(self._request_buffs())
        debuffs = asyncio.create_task(self._request_debuffs())
        damage_done = asyncio.create_task(self._request_damage_done())
        await asyncio.gather(buffs, debuffs, damage_done)

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
        if not self._tracked_info.skills or self.damage_done_table:
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

        logger.info('Got {} casts'.format(len(decoded.entries)))
        for cast in decoded.entries:
            logger.debug(cast)

        self.damage_done_table = decoded
