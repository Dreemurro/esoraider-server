"""Summary table (dataType: Summary) response."""

from msgspec import field

from esoraider_server.esologs.consts import CharClass
from esoraider_server.esologs.responses.common import Gear, Talent
from esoraider_server.esologs.responses.core import EsoLogsDataClass


class CombatantInfo(EsoLogsDataClass):
    stats: list
    talents: list[Talent]
    gear: list[Gear] = field(default_factory=list)

    spec_ids: list | None = field(default=None, name='specIDs')
    artifact: list | None = None
    talent_tree: list | None = None

    def skill_ids(self):
        return [t.guid for t in self.talents]


class PlayerDetails(EsoLogsDataClass):
    name: str
    id: int
    guid: int
    type: CharClass
    icon: str

    server: str | None = None
    display_name: str | None = None
    anonymous: bool | None = None
    min_item_level: int | None = None
    max_item_level: int | None = None
    specs: list[str] | None = None
    potion_use: int | None = None
    healthstone_use: int | None = None
    # CombatantInfo can be an empty list if requested log is broken
    combatant_info: CombatantInfo | list[None] | None = None


class PlayerDetailsBySpec(EsoLogsDataClass):
    dps: list[PlayerDetails] | None = None
    healers: list[PlayerDetails] | None = None
    tanks: list[PlayerDetails] | None = None


class DoneByAbility(EsoLogsDataClass):
    name: str
    guid: int
    type: int
    ability_icon: str
    total: int

    composite: bool | None = None
    flags: int | None = None


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
    type: int | str  # str - for summary table, int - for char table
    total: int

    id: int | None = None
    icon: str | None = None
    ability_icon: str | None = None
    composite: bool | None = None
    flags: int | None = None


class Spec(EsoLogsDataClass):
    spec: str
    role: str


class Composition(EsoLogsDataClass):
    name: str
    id: int
    guid: int
    type: CharClass
    specs: list[Spec]


class SummaryTableData(EsoLogsDataClass):
    total_time: int
    item_level: float
    log_version: int
    game_version: int
    composition: list[Composition]
    damage_done: list[DoneByChar]
    healing_done: list[DoneByChar]
    damage_taken: list[DoneByAbility]
    death_events: list[DeathEvent]

    combatant_info: CombatantInfo | None = None
    player_details: PlayerDetailsBySpec | None = None
