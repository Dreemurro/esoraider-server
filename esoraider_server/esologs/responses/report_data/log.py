from esoraider_server.esologs.responses.core import EsoLogsDataClass
from esoraider_server.esologs.responses.report_data.fight import Fight


class Owner(EsoLogsDataClass):
    name: str


class Log(EsoLogsDataClass):
    code: str
    title: str
    end_time: int

    owner: Owner | None = None
    fights: list[Fight] | None = None
