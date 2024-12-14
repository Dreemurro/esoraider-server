from typing import List, Optional

from msgspec import convert, field

from esoraider_server.esologs.responses.common import Gear, Talent
from esoraider_server.esologs.responses.core import EsoLogsDataClass
from esoraider_server.esologs.responses.report_data.effects import Aura


class Event(EsoLogsDataClass):
    timestamp: int
    type: str
    source_id: int = field(name='sourceID')

    source_is_friendly: Optional[bool] = None
    target_id: Optional[int] = field(default=None, name='targetID')
    target_is_friendly: Optional[bool] = None
    ability: Optional[Talent] = None
    extra_ability: Optional[Talent] = None
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


class Series(EsoLogsDataClass):
    name: str
    id: int
    guid: int
    type: str
    # 0 - time, 1 - stack
    data: List[List[int]]  # noqa: WPS110
    _events: list[list | dict] = field(default_factory=list, name='events')

    current_values: Optional[List[int]] = None
    max_values: Optional[List[int]] = None

    @property
    def events(self) -> list[Event]:
        # First and last elements are empty lists for some reason
        # + there is an occasional combatantinfo in there
        # Skipping such stuff for now
        final = []
        for item in self._events:
            if isinstance(item, list):
                continue
            if item.get('type') == 'combatantinfo':
                continue
            final.append(item)
        return [convert(_, Event) for _ in final]


class GraphData(EsoLogsDataClass):
    series: List[Series]

    start_time: Optional[int] = None
    end_time: Optional[int] = None
    use_targets: Optional[bool] = None
