from typing import List, Optional, Union

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

TableData = Union[SummaryTableData, CastsTableData, EffectsTableData]


class Report(EsoLogsDataClass):
    events: Optional[List[Event]] = None
    fights: Optional[List[BaseFight]] = None
    graph: Optional[GraphData] = None
    table: SummaryTableData | None = None


class RawData(EsoLogsDataClass):
    data: dict | list[dict]


class RawReportData(EsoLogsDataClass):
    events: RawData | None = None
    fights: list[dict] | None = None
    graph: RawData | None = None
    table: RawData | None = None
