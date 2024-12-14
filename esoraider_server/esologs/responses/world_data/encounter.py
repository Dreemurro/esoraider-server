from esoraider_server.esologs.responses.core import EsoLogsDataClass


class Difficulty(EsoLogsDataClass):
    id: int
    name: str | None = None


class Zone(EsoLogsDataClass):
    difficulties: list[Difficulty] | None = None


class Encounter(EsoLogsDataClass):
    id: int
    name: str
    zone: Zone | None = None
