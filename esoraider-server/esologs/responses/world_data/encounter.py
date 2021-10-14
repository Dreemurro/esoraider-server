from dataclasses import dataclass
from typing import List, Optional

from esologs.responses.core import EsoLogsDataClass


@dataclass
class Difficulty(EsoLogsDataClass):
    id: int
    name: Optional[str] = None


@dataclass
class Zone(EsoLogsDataClass):
    difficulties: Optional[List[Difficulty]] = None


@dataclass
class Encounter(EsoLogsDataClass):
    id: int
    name: str
    zone: Optional[Zone] = None
