"""Effects table (dataType: Buffs / Debuffs) response."""

from dataclasses import dataclass
from typing import List, Optional

from esoraider_server.esologs.responses.common import Talent
from esoraider_server.esologs.responses.core import EsoLogsDataClass


@dataclass
class Band(EsoLogsDataClass):
    start_time: int
    end_time: int


@dataclass
class Aura(EsoLogsDataClass):
    name: str

    guid: Optional[int] = None
    type: Optional[int] = None
    ability_icon: Optional[str] = None
    flags: Optional[int] = None
    total_uptime: Optional[int] = None
    total_uses: Optional[int] = None
    bands: Optional[List[Band]] = None

    source: Optional[int] = None
    ability: Optional[int] = None
    stacks: Optional[int] = None
    icon: Optional[str] = None
    applied_by_abilities: Optional[List[Talent]] = None


@dataclass
class EffectsTableData(EsoLogsDataClass):
    auras: List[Aura]
    use_targets: bool
    total_time: int
    start_time: int
    end_time: int

    category: Optional[int] = None
    log_version: Optional[int] = None
    game_version: Optional[int] = None
