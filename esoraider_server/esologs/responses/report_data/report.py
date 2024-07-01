from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union

from dataclasses_json import config
from dataclasses_json.undefined import UndefinedParameterError

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
from esoraider_server.esologs.responses.report_data.summary import (
    SummaryTableData,
)

TableData = Union[SummaryTableData, CastsTableData, EffectsTableData]


def events_decoder(raw_events: Optional[Dict]) -> Optional[List[Event]]:
    if not raw_events:
        return None
    return [Event.from_dict(raw_event) for raw_event in raw_events['data']]


def graph_decoder(raw_graph: Optional[Dict]) -> Optional[GraphData]:
    if not raw_graph:
        return None
    return GraphData.from_dict(raw_graph['data'])


def table_decoder(raw_table: Optional[Dict]) -> Optional[TableData]:
    if not raw_table:
        return None

    for table in (SummaryTableData, CastsTableData, EffectsTableData):
        try:
            return table.from_dict(raw_table['data'])  # type: ignore
        except UndefinedParameterError:
            continue
    raise RuntimeError('Failed to decode table:\n{0}'.format(raw_table))


@dataclass
class Report(EsoLogsDataClass):
    events: Optional[List[Event]] = field(
        default=None,
        metadata=config(decoder=events_decoder),
    )
    fights: Optional[List[Fight]] = None
    graph: Optional[GraphData] = field(
        default=None,
        metadata=config(decoder=graph_decoder),
    )
    table: Optional[TableData] = field(
        default=None,
        metadata=config(decoder=table_decoder),
    )
