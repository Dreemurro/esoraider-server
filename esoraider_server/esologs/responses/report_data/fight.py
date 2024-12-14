from msgspec import field

from esoraider_server.esologs.responses.core import EsoLogsDataClass


class GameZone(EsoLogsDataClass):
    name: str


class BaseFight(EsoLogsDataClass):
    encounter_id: int = field(name='encounterID')
    difficulty: int | None


class Fight(BaseFight):
    id: int
    name: str
    start_time: int
    end_time: int
    game_zone: GameZone
    friendly_players: list[int]

    fight_percentage: float | None = None
    kill: bool | None = None
