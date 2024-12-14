"""Main body of any response."""

from typing import Optional

from esoraider_server.esologs.responses.core import EsoLogsDataClass
from esoraider_server.esologs.responses.world_data.encounter import Encounter


class ReportData(EsoLogsDataClass):
    report: dict  # Will decode into necessary format later on


class WorldData(EsoLogsDataClass):
    encounter: Optional[Encounter] = None


class WorldDataResponse(EsoLogsDataClass):
    world_data: WorldData


class ReportDataResponse(EsoLogsDataClass):
    report_data: ReportData
