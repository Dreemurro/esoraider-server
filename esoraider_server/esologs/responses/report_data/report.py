from esoraider_server.esologs.responses.core import EsoLogsDataClass
from esoraider_server.esologs.responses.report_data.casts import CastsTableData
from esoraider_server.esologs.responses.report_data.effects import (
    EffectsTableData,
)
from esoraider_server.esologs.responses.report_data.fight import BaseFight
from esoraider_server.esologs.responses.report_data.graph import (
    Event,
    GraphData,
)
from esoraider_server.esologs.responses.report_data.summary import (
    SummaryTableData,
)

TableData = SummaryTableData | CastsTableData | EffectsTableData


class Report(EsoLogsDataClass):
    events: list[Event] | None = None
    fights: list[BaseFight] | None = None
    graph: GraphData | None = None
    table: SummaryTableData | None = None


class RawData(EsoLogsDataClass):
    data: dict | list[dict]


class RawReportData(EsoLogsDataClass):
    events: RawData | None = None
    fights: list[dict] | None = None
    graph: RawData | None = None
    table: RawData | None = None
