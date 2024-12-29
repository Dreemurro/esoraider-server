from msgspec import convert

from esoraider_server.esologs.consts import DataType
from esoraider_server.esologs.responses.base import (
    ReportDataResponse,
    WorldDataResponse,
)
from esoraider_server.esologs.responses.report_data.casts import CastsTableData
from esoraider_server.esologs.responses.report_data.effects import (
    EffectsTableData,
)
from esoraider_server.esologs.responses.report_data.fight import BaseFight
from esoraider_server.esologs.responses.report_data.graph import (
    Event,
    GraphData,
)
from esoraider_server.esologs.responses.report_data.log import Log
from esoraider_server.esologs.responses.report_data.report import (
    RawReportData,
    Report,
    TableData,
)
from esoraider_server.esologs.responses.report_data.summary import (
    SummaryTableData,
)
from esoraider_server.esologs.responses.world_data.encounter import Encounter


def convert_events(obj: dict) -> list[Event]:
    response = convert(obj, ReportDataResponse)
    raw_report = convert(response.report_data.report, RawReportData)
    if not raw_report.events:
        raise ValueError

    return [convert(_, Event) for _ in raw_report.events.data]


def convert_report(obj: dict) -> Report:
    response = convert(obj, ReportDataResponse)
    raw_report = convert(response.report_data.report, RawReportData)
    if not raw_report.table:
        raise ValueError

    return Report(
        table=convert(raw_report.table.data, SummaryTableData),
        fights=convert(raw_report.fights, list[BaseFight]),
    )


def convert_table(obj: dict, data_type: DataType) -> TableData:
    response = convert(obj, ReportDataResponse)
    raw_report = convert(response.report_data.report, RawReportData)
    if not raw_report.table:
        raise ValueError

    if data_type == DataType.SUMMARY:
        return convert(raw_report.table.data, SummaryTableData)
    elif data_type in {DataType.BUFFS, DataType.DEBUFFS}:
        return convert(raw_report.table.data, EffectsTableData)
    elif data_type == DataType.DAMAGE_DONE:
        return convert(raw_report.table.data, CastsTableData)
    raise ValueError


def convert_encounter(obj: dict) -> Encounter | None:
    response = convert(obj, WorldDataResponse)

    if not response.world_data:
        raise ValueError('WorldData is empty')

    return response.world_data.encounter


def convert_log(obj: dict) -> Log:
    response = convert(obj, ReportDataResponse)
    return convert(response.report_data.report, Log)


def encode_graph_id(id_: int) -> str:
    return f'id_{id_}'


def decode_graph_id(id_: str) -> int:
    return int(id_.split('_')[1])


def convert_graphs(obj: dict) -> dict[int, GraphData]:
    response = convert(obj, ReportDataResponse)

    return {
        decode_graph_id(id_): convert(graph.get('data'), GraphData)
        for id_, graph in response.report_data.report.items()
    }
