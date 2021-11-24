from typing import Dict, List, Optional, Tuple

from gql.dsl import DSLField, DSLQuery, dsl_gql  # type: ignore
from loguru import logger

from esoraider_server.esologs.base import ApiWrapperBase
from esoraider_server.esologs.consts import DataType, HostilityType
from esoraider_server.esologs.responses.base import BaseResponseData
from esoraider_server.esologs.responses.report_data.graph import (
    Event,
    GraphData,
)
from esoraider_server.esologs.responses.report_data.report import (
    Report,
    TableData,
)
from esoraider_server.esologs.responses.world_data.encounter import Encounter


class ZeroLengthFightException(Exception):
    def __init__(self):
        message = "This fight's duration is zero"
        super().__init__(message)


def _encode_id(id_: int) -> str:
    return 'id_{0}'.format(id_)


def _decode_id(id_: str) -> int:
    return int(id_.split('_')[1])


class ApiWrapper(ApiWrapperBase):
    async def query_encounter_info(
        self, encounter_id: int,
    ) -> Optional[Encounter]:
        logger.info('Requesting info on encounter = {0}'.format(encounter_id))
        query = self.ds.Query.worldData

        encounter = self.ds.WorldData.encounter(id=encounter_id)
        difficulties_fields = self.ds.Zone.difficulties.select(
            self.ds.Difficulty.id,
            self.ds.Difficulty.name,
        )
        zone_fields = self.ds.Encounter.zone.select(
            difficulties_fields,
        )
        encounter_fields = encounter.select(
            self.ds.Encounter.id,
            self.ds.Encounter.name,
            zone_fields,
        )

        query.select(encounter_fields)

        response = BaseResponseData.from_dict(
            await self.execute(dsl_gql(DSLQuery(query))),
        )

        if not response.world_data:
            raise ValueError('WorldData is empty')

        return response.world_data.encounter

    async def query_log(self, log: str):
        logger.info('Requesting log {0}'.format(log))
        query = self.ds.Query.reportData

        report = self.ds.ReportData.report(code=log)
        fight_fields = self.ds.Report.fights.select(
            self.ds.ReportFight.id,
            self.ds.ReportFight.name,
            self.ds.ReportFight.difficulty,
            self.ds.ReportFight.fightPercentage,
            self.ds.ReportFight.encounterID,
            self.ds.ReportFight.kill,
            self.ds.ReportFight.startTime,
            self.ds.ReportFight.endTime,
            self.ds.ReportFight.gameZone.select(self.ds.GameZone.name),
            self.ds.ReportFight.friendlyPlayers,
        )
        report_fields = report.select(
            self.ds.Report.code,
            self.ds.Report.title,
            self.ds.Report.endTime,
            # self.ds.Report.rankings, # for so-called partition aka patch
            self.ds.Report.owner.select(self.ds.User.name),
            fight_fields,
        )

        query.select(report_fields)
        return await self.execute(dsl_gql(DSLQuery(query)))

    async def query_fight_times(
        self, log: str, fight_id: int,
    ) -> Tuple[int, int]:
        logger.info('Requesting fight times')
        logger.info('Log = {0}'.format(log))
        logger.info('Fight ID = {0}'.format(fight_id))

        query = self.ds.Query.reportData
        report = self.ds.ReportData.report(code=log)
        fight = self.ds.Report.fights(fightIDs=fight_id)
        fight_fields = fight.select(
            self.ds.ReportFight.startTime,
            self.ds.ReportFight.endTime,
        )
        report_fields = report.select(fight_fields)

        query.select(report_fields)

        response = await self.execute(dsl_gql(DSLQuery(query)))
        response = response.get('reportData').get('report').get('fights')[0]
        return response.get('startTime'), response.get('endTime')

    async def query_table(
        self,
        log: str,
        fight_id: int,
        data_type: DataType = DataType.SUMMARY,
        hostility_type: HostilityType = HostilityType.FRIENDLIES,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        source_id: Optional[int] = None,
        target_id: Optional[int] = None,
        filter_exp: Optional[str] = None,
    ) -> TableData:
        logger.info('Requesting reportData')
        logger.info('Log = {0}'.format(log))
        logger.info('Fight ID = {0}'.format(fight_id))
        logger.info('Data Type = {0}'.format(data_type))
        logger.info('Hostility Type = {0}'.format(hostility_type))
        logger.info('Start Time = {0}'.format(start_time))
        logger.info('End Time = {0}'.format(end_time))
        logger.info('Source ID = {0}'.format(source_id))
        logger.info('Target ID = {0}'.format(target_id))
        logger.info('Filter = {0}'.format(filter_exp))

        if not start_time or not end_time:
            start_time, end_time = await self.query_fight_times(log, fight_id)
        if start_time == end_time:
            raise ZeroLengthFightException

        query = self.ds.Query.reportData

        report = self.ds.ReportData.report(code=log)
        table = self.ds.Report.table(
            startTime=start_time,
            endTime=end_time,
            dataType=data_type.value,
            hostilityType=hostility_type.value,
            sourceID=source_id,
            targetID=target_id,
            filterExpression=filter_exp,
        )
        report_fields = report.select(table)

        query.select(report_fields)

        response = BaseResponseData.from_dict(
            await self.execute(dsl_gql(DSLQuery(query))),
        )

        if not response.report_data:
            raise ValueError('ReportData is empty')
        if not response.report_data.report.table:
            raise ValueError('Table is empty')

        return response.report_data.report.table

    async def query_char_table(
        self,
        log: str,
        fight_id: int,
        char_id: int,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
    ) -> Report:
        logger.info('Requesting char summary table')
        logger.info('Log = {0}'.format(log))
        logger.info('Fight ID = {0}'.format(fight_id))
        logger.info('Char ID = {0}'.format(char_id))
        logger.info('Start Time = {0}'.format(start_time))
        logger.info('End Time = {0}'.format(end_time))

        if not start_time or not end_time:
            start_time, end_time = await self.query_fight_times(log, fight_id)
        if start_time == end_time:
            raise ZeroLengthFightException

        query = self.ds.Query.reportData

        report = self.ds.ReportData.report(code=log)
        fights = self.ds.Report.fights(fightIDs=fight_id).select(
            self.ds.ReportFight.encounterID,
            self.ds.ReportFight.difficulty,
        )
        table = self.ds.Report.table(
            startTime=start_time,
            endTime=end_time,
            dataType=DataType.SUMMARY.value,
            sourceID=char_id,
        )
        report_fields = report.select(table).select(fights)

        query.select(report_fields)

        response = BaseResponseData.from_dict(
            await self.execute(dsl_gql(DSLQuery(query))),
        )

        if not response.report_data:
            raise ValueError('ReportData is empty')

        return response.report_data.report

    async def query_events(
        self,
        log: str,
        char_id: int,
        start_time: int,
        end_time: int,
        data_type: DataType = DataType.COMBATANT_INFO,
    ) -> List[Event]:
        logger.info('Requesting events')
        logger.info('Log = {0}'.format(log))
        logger.info('Char ID = {0}'.format(char_id))
        logger.info('Start Time = {0}'.format(start_time))
        logger.info('End Time = {0}'.format(end_time))
        logger.info('Data Type = {0}'.format(data_type))

        query = self.ds.Query.reportData

        report = self.ds.ReportData.report(code=log)
        events = self.ds.Report.events(
            # ********************** GQL forbidden magic **********************
            # GQL will turn numbers into scientific notation, which means
            # number '6951757' will turn into '6.95176e+06'. As you can see,
            # last digit got rounded which will potentially skip needed events.
            # So we will substract one second (1000) from start_time
            # just to avoid this loss
            startTime=start_time - 1000,
            endTime=end_time,
            sourceID=char_id,
            dataType=data_type.value,
        ).select(self.ds.ReportEventPaginator.data)

        report_fields = report.select(events)

        query.select(report_fields)

        response = BaseResponseData.from_dict(
            await self.execute(dsl_gql(DSLQuery(query))),
        )

        if not response.report_data:
            raise ValueError('ReportData is empty')
        if not response.report_data.report.events:
            raise ValueError('No events found')

        return response.report_data.report.events

    async def query_graph(
        self,
        log: str,
        char_id: Optional[int] = None,
        ability_id: Optional[int] = None,
        fight_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        data_type: DataType = DataType.BUFFS,
        hostility_type: HostilityType = HostilityType.FRIENDLIES,
        graphs: Optional[Dict[str, DSLField]] = None,
    ) -> Dict[int, GraphData]:
        if graphs:
            logger.info('Requesting multiple graphs')
        else:
            logger.info('Requesting graph')
        logger.info('Log = {0}'.format(log))

        query = self.ds.Query.reportData

        report = self.ds.ReportData.report(code=log)

        if graphs:
            report_fields = report.select(**graphs)
        elif ability_id and char_id and fight_id:
            if not start_time or not end_time:
                start_time, end_time = await self.query_fight_times(
                    log, fight_id,
                )
            if start_time == end_time:
                raise ZeroLengthFightException

            graph = await self.partial_query_graph(
                data_type=data_type,
                ability_id=ability_id,
                start_time=start_time,
                end_time=end_time,
                hostility_type=hostility_type,
                char_id=char_id,
            )
            report_fields = report.select(**graph)
        else:
            raise TypeError(
                'Either graphs or fight_id & char_id & ability_id ' +
                'must be provided',
            )

        query.select(report_fields)

        response = await self.execute(dsl_gql(DSLQuery(query)))
        response = response.get('reportData')
        response = response.get('report')

        return {
            _decode_id(id_): GraphData.from_dict(graph.get('data'))
            for id_, graph in response.items()
        }

    async def partial_query_graph(
        self,
        data_type: DataType,
        ability_id: int,
        start_time: int,
        end_time: int,
        hostility_type: HostilityType = HostilityType.FRIENDLIES,
        char_id: Optional[int] = None,
    ) -> Dict[str, DSLField]:
        logger.info('Building partial graph request')
        logger.info('Char ID = {0}'.format(char_id))
        logger.info('Start Time = {0}'.format(start_time))
        logger.info('End Time = {0}'.format(end_time))
        logger.info('Data Type = {0}'.format(data_type))
        logger.info('Ability ID = {0}'.format(ability_id))
        logger.info('Hostility Type = {0}'.format(hostility_type))

        source_id = None
        target_id = None
        if hostility_type == HostilityType.FRIENDLIES:
            source_id = char_id
        elif hostility_type == HostilityType.ENEMIES:
            target_id = char_id

        return {
            _encode_id(ability_id): self.ds.Report.graph(
                startTime=start_time,
                endTime=end_time,
                abilityID=ability_id,
                hostilityType=hostility_type.value,
                dataType=data_type.value,
                sourceID=source_id,
                targetID=target_id,
            ),
        }
