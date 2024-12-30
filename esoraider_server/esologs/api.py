from typing import TYPE_CHECKING

from gql.dsl import DSLQuery, dsl_gql  # type: ignore
from structlog.stdlib import get_logger

from esoraider_server.esologs.base import ApiWrapperBase
from esoraider_server.esologs.consts import DataType, HostilityType
from esoraider_server.esologs.converters import (
    convert_encounter,
    convert_events,
    convert_graphs,
    convert_log,
    convert_report,
    convert_table,
    encode_graph_id,
)
from esoraider_server.esologs.exceptions import (
    NonexistentFightError,
    ZeroLengthFightError,
)

if TYPE_CHECKING:
    from gql.dsl import DSLField

    from esoraider_server.esologs.responses.report_data.graph import (
        Event,
        GraphData,
    )
    from esoraider_server.esologs.responses.report_data.log import Log
    from esoraider_server.esologs.responses.report_data.report import (
        Report,
        TableData,
    )
    from esoraider_server.esologs.responses.world_data.encounter import (
        Encounter,
    )

logger = get_logger()


class ApiWrapper(ApiWrapperBase):
    async def query_encounter_info(
        self, encounter_id: int,
    ) -> 'Encounter | None':
        await logger.ainfo(f'Requesting info on encounter = {encounter_id}')
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

        return convert_encounter(await self.execute(dsl_gql(DSLQuery(query))))

    async def query_log(self, log: str) -> 'Log':
        await logger.ainfo(f'Requesting log {log}')
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

        return convert_log(await self.execute(dsl_gql(DSLQuery(query))))

    async def query_fight_times(
        self, log: str, fight_id: int,
    ) -> tuple[int, int]:
        await logger.ainfo('Requesting fight times')
        await logger.ainfo(f'Log = {log}')
        await logger.ainfo(f'Fight ID = {fight_id}')

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
        fights = response.get('reportData').get('report').get('fights')
        if not fights:
            raise NonexistentFightError
        response = fights[0]
        return response.get('startTime'), response.get('endTime')

    async def query_table(
        self,
        log: str,
        fight_id: int,
        data_type: DataType = DataType.SUMMARY,
        hostility_type: HostilityType = HostilityType.FRIENDLIES,
        start_time: int | None = None,
        end_time: int | None = None,
        source_id: int | None = None,
        target_id: int | None = None,
        filter_exp: str | None = None,
    ) -> 'TableData':
        await logger.ainfo('Requesting reportData')
        await logger.ainfo(f'Log = {log}')
        await logger.ainfo(f'Fight ID = {fight_id}')
        await logger.ainfo(f'Data Type = {data_type}')
        await logger.ainfo(f'Hostility Type = {hostility_type}')
        await logger.ainfo(f'Start Time = {start_time}')
        await logger.ainfo(f'End Time = {end_time}')
        await logger.ainfo(f'Source ID = {source_id}')
        await logger.ainfo(f'Target ID = {target_id}')
        await logger.ainfo(f'Filter = {filter_exp}')

        if not start_time or not end_time:
            start_time, end_time = await self.query_fight_times(log, fight_id)
        if start_time == end_time:
            raise ZeroLengthFightError

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

        return convert_table(
            obj=await self.execute(dsl_gql(DSLQuery(query))),
            data_type=data_type,
        )

    async def query_char_table(
        self,
        log: str,
        fight_id: int,
        char_id: int,
        start_time: int | None = None,
        end_time: int | None = None,
    ) -> 'Report':
        await logger.ainfo('Requesting char summary table')
        await logger.ainfo(f'Log = {log}')
        await logger.ainfo(f'Fight ID = {fight_id}')
        await logger.ainfo(f'Char ID = {char_id}')
        await logger.ainfo(f'Start Time = {start_time}')
        await logger.ainfo(f'End Time = {end_time}')

        if not start_time or not end_time:
            start_time, end_time = await self.query_fight_times(log, fight_id)
        if start_time == end_time:
            raise ZeroLengthFightError

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

        return convert_report(await self.execute(dsl_gql(DSLQuery(query))))

    async def query_events(
        self,
        log: str,
        char_id: int,
        start_time: int,
        end_time: int,
        data_type: DataType = DataType.COMBATANT_INFO,
    ) -> list['Event']:
        await logger.ainfo('Requesting events')
        await logger.ainfo(f'Log = {log}')
        await logger.ainfo(f'Char ID = {char_id}')
        await logger.ainfo(f'Start Time = {start_time}')
        await logger.ainfo(f'End Time = {end_time}')
        await logger.ainfo(f'Data Type = {data_type}')

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

        return convert_events(await self.execute(dsl_gql(DSLQuery(query))))

    async def query_graph(
        self,
        log: str,
        char_id: int | None = None,
        ability_id: int | None = None,
        fight_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        data_type: DataType = DataType.BUFFS,
        hostility_type: HostilityType = HostilityType.FRIENDLIES,
        graphs: dict[str, 'DSLField'] | None = None,
    ) -> dict[int, 'GraphData']:
        if graphs:
            await logger.ainfo('Requesting multiple graphs')
        else:
            await logger.ainfo('Requesting graph')
        await logger.ainfo(f'Log = {log}')

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
                raise ZeroLengthFightError

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
                'Either graphs or fight_id & char_id & ability_id '
                + 'must be provided',
            )

        query.select(report_fields)

        return convert_graphs(await self.execute(dsl_gql(DSLQuery(query))))

    async def partial_query_graph(
        self,
        data_type: DataType,
        ability_id: int,
        start_time: int,
        end_time: int,
        hostility_type: HostilityType = HostilityType.FRIENDLIES,
        char_id: int | None = None,
    ) -> dict[str, 'DSLField']:
        await logger.ainfo('Building partial graph request')
        await logger.ainfo(f'Char ID = {char_id}')
        await logger.ainfo(f'Start Time = {start_time}')
        await logger.ainfo(f'End Time = {end_time}')
        await logger.ainfo(f'Data Type = {data_type}')
        await logger.ainfo(f'Ability ID = {ability_id}')
        await logger.ainfo(f'Hostility Type = {hostility_type}')

        source_id = None
        target_id = None
        if hostility_type == HostilityType.FRIENDLIES:
            source_id = char_id
        elif hostility_type == HostilityType.ENEMIES:
            target_id = char_id

        return {
            encode_graph_id(ability_id): self.ds.Report.graph(
                startTime=start_time,
                endTime=end_time,
                abilityID=ability_id,
                hostilityType=hostility_type.value,
                dataType=data_type.value,
                sourceID=source_id,
                targetID=target_id,
            ),
        }
