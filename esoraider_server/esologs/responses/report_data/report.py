from dataclasses import dataclass
from typing import List, Optional, Union

from esoraider_server.esologs.responses.core import EsoLogsDataClass
from esoraider_server.esologs.responses.report_data.casts import CastsTableData
from esoraider_server.esologs.responses.report_data.effects import (
    EffectsTableData,
)
from esoraider_server.esologs.responses.report_data.fight import Fight
from esoraider_server.esologs.responses.report_data.graph import (
    Event,
    GraphData,
)


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
