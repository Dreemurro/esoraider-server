from dataclasses import dataclass, field
from typing import List, Optional

from dataclasses_json import config
from esologs.responses.common import Talent
from esologs.responses.core import EsoLogsDataClass


@dataclass
class Event(EsoLogsDataClass):
    timestamp: int
    type: str
    source_id: int = field(metadata=config(field_name='sourceID'))
    source_is_friendly: bool
    target_id: int = field(metadata=config(field_name='targetID'))
    target_is_friendly: bool
    ability: Talent
    fight: int

    stack: Optional[int] = None
    target_instance: Optional[int] = None
    absorb: Optional[int] = None


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


@dataclass
class GraphData(EsoLogsDataClass):
    series: List[Series]
    start_time: int
    end_time: int
    use_targets: bool
