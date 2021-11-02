from dataclasses import dataclass
from typing import List, Optional, Union

from esologs.responses.core import EsoLogsDataClass
from esologs.responses.report_data.casts import CastsTableData
from esologs.responses.report_data.effects import EffectsTableData
from esologs.responses.report_data.fight import Fight
from esologs.responses.report_data.graph import Event, GraphData


@dataclass
class BaseData(EsoLogsDataClass):
    data: Union[  # noqa: WPS110
        CastsTableData,
        EffectsTableData,
        GraphData,
        List[Event],
        None,
    ] = None


@dataclass
class Report(EsoLogsDataClass):
    events: Optional[BaseData] = None
    fights: Optional[List[Fight]] = None
    graph: Optional[BaseData] = None
    table: Optional[BaseData] = None
