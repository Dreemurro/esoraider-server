"""Summary table (dataType: Summary) response."""

from typing import Any, List, Optional, Union

from msgspec import field

from esoraider_server.esologs.consts import CharClass
from esoraider_server.esologs.responses.common import Gear, Talent
from esoraider_server.esologs.responses.core import EsoLogsDataClass


class CombatantInfo(EsoLogsDataClass):
    stats: List[Any]
    talents: List[Talent]
    gear: List[Gear] = field(default_factory=list)

    spec_ids: Optional[List[Any]] = field(default=None, name='specIDs')
    artifact: Optional[List[Any]] = None
    talent_tree: Optional[List[Any]] = None

    def skill_ids(self):
        return [t.guid for t in self.talents]


class PlayerDetails(EsoLogsDataClass):
    name: str
    id: int
    guid: int
    type: CharClass
    icon: str

    server: Optional[str] = None
    display_name: Optional[str] = None
    anonymous: Optional[bool] = None
    min_item_level: Optional[int] = None
    max_item_level: Optional[int] = None
    specs: Optional[List[str]] = None
    potion_use: Optional[int] = None
    healthstone_use: Optional[int] = None
    # CombatantInfo can be an empty list if requested log is broken
    combatant_info: CombatantInfo | list[None] | None = None


class PlayerDetailsBySpec(EsoLogsDataClass):
    dps: Optional[List[PlayerDetails]] = None
    healers: Optional[List[PlayerDetails]] = None
    tanks: Optional[List[PlayerDetails]] = None


class DoneByAbility(EsoLogsDataClass):
    name: str
    guid: int
    type: int
    ability_icon: str
    total: int

    composite: Optional[bool] = None
    flags: Optional[int] = None


class DeathFromAbility(EsoLogsDataClass):
    name: str
    guid: int
    type: int
    ability_icon: str
    flags: int


class DeathEvent(EsoLogsDataClass):
    name: str
    id: int
    guid: int
    type: str
    icon: str
    death_time: int
    ability: DeathFromAbility


class DoneByChar(EsoLogsDataClass):
    name: str
    guid: int
    type: Union[int, str]  # str - for summary table, int - for char table
    total: int

    id: Optional[int] = None
    icon: Optional[str] = None
    ability_icon: Optional[str] = None
    composite: Optional[bool] = None
    flags: Optional[int] = None


class Spec(EsoLogsDataClass):
    spec: str
    role: str


class Composition(EsoLogsDataClass):
    name: str
    id: int
    guid: int
    type: CharClass
    specs: List[Spec]


class SummaryTableData(EsoLogsDataClass):
    total_time: int
    item_level: float
    log_version: int
    game_version: int
    composition: List[Composition]
    damage_done: List[DoneByChar]
    healing_done: List[DoneByChar]
    damage_taken: List[DoneByAbility]
    death_events: List[DeathEvent]

    combatant_info: Optional[CombatantInfo] = None
    player_details: Optional[PlayerDetailsBySpec] = None
