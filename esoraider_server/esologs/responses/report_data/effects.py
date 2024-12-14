"""Effects table (dataType: Buffs / Debuffs) response."""

from esoraider_server.esologs.responses.common import Talent
from esoraider_server.esologs.responses.core import EsoLogsDataClass


class Band(EsoLogsDataClass):
    start_time: int
    end_time: int


class Aura(EsoLogsDataClass):
    name: str

    guid: int | None = None
    type: int | None = None
    ability_icon: str | None = None
    flags: int | None = None
    total_uptime: int | None = None
    total_uses: int | None = None
    bands: list[Band] | None = None

    source: int | None = None
    ability: int | None = None
    stacks: int | None = None
    icon: str | None = None
    applied_by_abilities: list[Talent] | None = None


class EffectsTableData(EsoLogsDataClass):
    auras: list[Aura]
    use_targets: bool
    total_time: int
    start_time: int
    end_time: int

    category: int | None = None
    log_version: int | None = None
    game_version: int | None = None
