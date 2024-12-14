from typing import List, Optional

from esoraider_server.esologs.responses.core import EsoLogsDataClass


class Difficulty(EsoLogsDataClass):
    id: int
    name: Optional[str] = None


class Zone(EsoLogsDataClass):
    difficulties: Optional[List[Difficulty]] = None


class Encounter(EsoLogsDataClass):
    id: int
    name: str
    zone: Optional[Zone] = None
