from dataclasses import asdict
from typing import Dict, List

from analysis.data_request import DataRequest
from analysis.tracked_info import TrackedInfo
from analysis.uptimes import Uptimes
from api.api import ApiWrapper
from api.response import Aura, Series, SummaryTableData
from loguru import logger


class ReportBuilder:
    def __init__(
        self,
        api: ApiWrapper,
        log: str,
        fight_id: int,
        char_id: int,
        summary_table: SummaryTableData,
        start_time: int = None,
        end_time: int = None,
    ) -> None:
        self.api = api

        self.log = log
        self.fight_id = fight_id
        self.start_time = start_time
        self.end_time = end_time

        self.summary_table = summary_table

        self.tracked_info: TrackedInfo = None
        self.requested_data: DataRequest = None
        self.uptimes: Uptimes = None

        self.char_id = char_id
        self._char_class: str = None
        self._char_spec: str = None
        self._char_name: str = None
        self._char_buffs: List[Aura] = []
        self._char_debuffs: List[Aura] = []
        self._char_graphs: List[Series] = []

        self.report: Dict = None

    async def build(self):
        self._get_char_info()

        self.tracked_info = TrackedInfo(self.summary_table, self._char_class)
        self.tracked_info.extract()

        self.requested_data = DataRequest(
            api=self.api,
            log=self.log,
            fight_id=self.fight_id,
            start_time=self.start_time,
            end_time=self.end_time,
            char_id=self.char_id,
            tracked_info=self.tracked_info,
        )
        await self.requested_data.execute()

        self._get_char_buffs()
        self._get_char_debuffs()
        self._get_char_graphs()

        self.uptimes = Uptimes(
            tracked_info=self.tracked_info,
            requested_info=self.requested_data,
            char_buffs=self._char_buffs,
            char_debuffs=self._char_debuffs,
            char_graphs=self._char_graphs,
        )
        self.uptimes.calculate()

        self._build_report()

        return self.report

    def _get_char_info(self):
        logger.info('Getting char class and spec')
        combatant = list(filter(
            lambda x: x.id == self.char_id, self.summary_table.composition,
        ))
        self._char_class = combatant[0].type
        self._char_spec = combatant[0].specs[0].spec
        self._char_name = combatant[0].name
        logger.debug('{} - {}'.format(self._char_class, self._char_spec))

    def _get_char_buffs(self):
        if not self.tracked_info.buffs:
            logger.error('No buffs were found. The log is probably broken')
            return

        logger.info('Extracting tracked buffs from buffs table')
        buff_ids = {i.id for i in self.tracked_info.buffs}
        for buff in self.requested_data.buffs_table.auras:
            if buff.guid in buff_ids:
                logger.debug(buff.name)
                self._char_buffs.append(buff)

    def _get_char_debuffs(self):
        if not self.requested_data.debuffs_table:
            logger.debug('No debuffs were found. The log is probably broken')
            return

        logger.info('Extracting tracked debuffs from debuffs table')
        debuff_ids = {i.id for i in self.tracked_info.debuffs}
        for debuff in self.requested_data.debuffs_table.auras:
            if debuff.guid in debuff_ids:
                logger.debug(debuff.name)
                self._char_debuffs.append(debuff)

    def _get_char_graphs(self):
        if not self.requested_data.graphs:
            logger.debug('No graphs were found. The log is probably broken')
            return

        logger.info('Extracting tracked stacks from graphs')
        for graph in self.requested_data.graphs:
            for series in graph.series:
                if series:
                    self._char_graphs.append(series)

    def _build_report(self):
        logger.info('Calculating uptimes')
        # TODO: Separate dataclass
        self.report = {
            'char': {
                'id': self.char_id,
                'name': self._char_name,
                'class': self._char_class,
                'spec': self._char_spec,
            },
            'skills': [],
            'sets': [],
            'glyphs': [],
        }

        self.report['skills'].extend([asdict(s) for s in self.uptimes.skills])
        self.report['sets'].extend([asdict(s) for s in self.uptimes.sets])
        self.report['glyphs'].extend([asdict(g) for g in self.uptimes.glyphs])
