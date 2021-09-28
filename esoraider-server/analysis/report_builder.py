"""Performance analysis report building."""

from dataclasses import asdict
from typing import Dict, List, Optional

from analysis.data_request import DataRequest
from analysis.tracked_info import TrackedInfo
from analysis.uptimes import Uptimes
from api.api import ApiWrapper
from api.response import Aura, Series, SummaryTableData
from loguru import logger


class ReportBuilder(object):
    """Performance analysis report builder."""

    def __init__(
        self,
        api: ApiWrapper,
        log: str,
        fight_id: int,
        summary_table: Optional[SummaryTableData] = None,
        char_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
    ) -> None:
        self._api = api

        self.log = log
        self.fight_id = fight_id
        self.start_time = start_time
        self.end_time = end_time

        self._summary_table = summary_table

        self._tracked_info: Optional[TrackedInfo] = None
        self._requested_data: Optional[DataRequest] = None
        self._uptimes: Optional[Uptimes] = None

        self.char_id = char_id
        self._char_class: Optional[str] = None
        self._char_spec: Optional[str] = None
        self._char_name: Optional[str] = None
        self._char_buffs: List[Aura] = []
        self._char_debuffs: List[Aura] = []
        self._char_graphs: List[Series] = []

        self.report: Dict = {}

    async def build(self) -> Dict:
        """Execute report building steps."""
        if self.char_id:
            self._get_char_info()

        self._tracked_info = TrackedInfo(
            summary_table=self._summary_table,
            char_class=self._char_class,
        )
        self._tracked_info.extract()

        self._requested_data = DataRequest(
            api=self._api,
            log=self.log,
            fight_id=self.fight_id,
            start_time=self.start_time,
            end_time=self.end_time,
            char_id=self.char_id,
            tracked_info=self._tracked_info,
        )
        await self._requested_data.execute()

        if self.char_id:
            self._get_char_buffs()
            self._get_char_debuffs()
            self._get_char_graphs()

        self._uptimes = Uptimes(
            tracked_info=self._tracked_info,
            requested_info=self._requested_data,
            char_buffs=self._char_buffs,
            char_debuffs=self._char_debuffs,
            char_graphs=self._char_graphs,
        )
        self._uptimes.calculate()

        self._build_report()

        return self.report

    def _get_char_info(self):
        logger.info('Getting char class and spec')
        combatant = list(filter(
            lambda char: char.id == self.char_id,
            self._summary_table.composition,
        ))
        self._char_class = combatant[0].type
        self._char_spec = combatant[0].specs[0].spec
        self._char_name = combatant[0].name
        logger.debug('{0} - {1}'.format(self._char_class, self._char_spec))

    def _get_char_buffs(self):
        if not self._tracked_info.buffs:
            logger.error('No buffs were found. The log is probably broken')
            return

        logger.info('Extracting tracked buffs from buffs table')
        buff_ids = {buff.id for buff in self._tracked_info.buffs}
        for buff in self._requested_data.buffs_table.auras:
            if buff.guid in buff_ids:
                logger.debug(buff.name)
                self._char_buffs.append(buff)

    def _get_char_debuffs(self):
        if not self._requested_data.debuffs_table:
            logger.debug('No debuffs were found. The log is probably broken')
            return

        logger.info('Extracting tracked debuffs from debuffs table')
        debuff_ids = {debuff.id for debuff in self._tracked_info.debuffs}
        for debuff in self._requested_data.debuffs_table.auras:
            if debuff.guid in debuff_ids:
                logger.debug(debuff.name)
                self._char_debuffs.append(debuff)

    def _get_char_graphs(self):
        if not self._requested_data.graphs:
            logger.debug('No graphs were found. The log is probably broken')
            return

        logger.info('Extracting tracked stacks from graphs')
        for graph in self._requested_data.graphs:
            for series in graph.series:
                if series:
                    self._char_graphs.append(series)

    def _build_report(self):
        # TODO: Separate dataclass
        self.report = {
            'char': {
                'id': self.char_id,
                'name': self._char_name,
                'class': self._char_class,
                'spec': self._char_spec,
            } if self.char_id else {},
            'skills':
                [asdict(skill) for skill in self._uptimes.skills]
                if self._uptimes.skills
                else [],
            'sets':
                [asdict(gear_set) for gear_set in self._uptimes.sets]
                if self._uptimes.sets
                else [],
            'glyphs':
                [asdict(glyph) for glyph in self._uptimes.glyphs]
                if self._uptimes.glyphs
                else [],
            'buffs':
                [asdict(buff) for buff in self._uptimes.buffs]
                if not self.char_id and self._uptimes.buffs
                else [],
            'debuffs':
                [asdict(debuff) for debuff in self._uptimes.debuffs]
                if not self.char_id and self._uptimes.debuffs
                else [],
        }
