"""Effects table (dataType: Buffs / Debuffs) response."""

from dataclasses import dataclass
from typing import List, Optional

from esologs.responses.core import EsoLogsDataClass


@dataclass
class Band(EsoLogsDataClass):
    start_time: int
    end_time: int


@dataclass
class Aura(EsoLogsDataClass):
    name: str
    guid: int
    type: int
    ability_icon: str
    flags: int
    total_uptime: int
    total_uses: int
    bands: List[Band]


@dataclass
class EffectsTableData(EsoLogsDataClass):
    auras: List[Aura]
    use_targets: bool
    total_time: int
    start_time: int
    end_time: int

    category: Optional[int] = None
    log_version: Optional[int] = None
