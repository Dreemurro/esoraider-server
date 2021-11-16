from dataclasses import dataclass, field
from typing import List, Optional

from dataclasses_json import config

from esoraider_server.esologs.responses.common import Gear, Talent
from esoraider_server.esologs.responses.core import EsoLogsDataClass
from esoraider_server.esologs.responses.report_data.effects import Aura


@dataclass
class Event(EsoLogsDataClass):
    timestamp: int
    type: str
    source_id: int = field(metadata=config(field_name='sourceID'))

    source_is_friendly: Optional[bool] = None
    target_id: Optional[int] = field(
        default=None,
        metadata=config(field_name='targetID'),
    )
    target_is_friendly: Optional[bool] = None
    ability: Optional[Talent] = None
    fight: Optional[int] = None

    stack: Optional[int] = None
    target_instance: Optional[int] = None
    absorb: Optional[int] = None

    gear: Optional[List[Gear]] = None
    auras: Optional[List[Aura]] = None

    resource_change: Optional[int] = None
    resource_change_type: Optional[int] = None
    other_resource_change: Optional[int] = None
    max_resource_amount: Optional[int] = None
    waste: Optional[int] = None


def skip_events(items: List) -> List[Event]:
    final = []
    for item in items:
        if isinstance(item, list):
            continue
        if item.get('type') == 'combatantinfo':
            continue
        final.append(item)
    return [Event.from_dict(_) for _ in final]


@dataclass
class Series(EsoLogsDataClass):
    name: str
    id: int
    guid: int
    type: str
    # 0 - time, 1 - stack
    data: List[List[int]]  # noqa: WPS110
    events: List[Event] = field(metadata=config(
        # First and last elements are empty lists for some reason
        # + there is an occasional combatantinfo in there
        # Skipping such stuff for now
        decoder=skip_events,
    ))

    current_values: Optional[List[int]] = None
    max_values: Optional[List[int]] = None


@dataclass
class GraphData(EsoLogsDataClass):
    series: List[Series]

    start_time: Optional[int] = None
    end_time: Optional[int] = None
    use_targets: Optional[bool] = None
