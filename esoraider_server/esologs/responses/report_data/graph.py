from msgspec import convert, field

from esoraider_server.esologs.responses.common import Gear, Talent
from esoraider_server.esologs.responses.core import EsoLogsDataClass
from esoraider_server.esologs.responses.report_data.effects import Aura


class Event(EsoLogsDataClass):
    timestamp: int
    type: str
    source_id: int = field(name='sourceID')

    source_is_friendly: bool | None = None
    target_id: int | None = field(default=None, name='targetID')
    target_is_friendly: bool | None = None
    ability: Talent | None = None
    extra_ability: Talent | None = None
    fight: int | None = None

    stack: int | None = None
    target_instance: int | None = None
    absorb: int | None = None

    gear: list[Gear] | None = None
    auras: list[Aura] | None = None

    resource_change: int | None = None
    resource_change_type: int | None = None
    other_resource_change: int | None = None
    max_resource_amount: int | None = None
    waste: int | None = None


class Series(EsoLogsDataClass):
    name: str
    id: int
    guid: int
    type: str
    # 0 - time, 1 - stack
    data: list[list[int]]  # noqa: WPS110
    _events: list[list | dict] = field(default_factory=list, name='events')

    current_values: list[int] | None = None
    max_values: list[int] | None = None

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
    series: list[Series]

    start_time: int | None = None
    end_time: int | None = None
    use_targets: bool | None = None
