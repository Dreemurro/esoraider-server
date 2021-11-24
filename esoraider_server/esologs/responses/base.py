"""Main body of any response."""

from dataclasses import dataclass
from typing import Optional

from esoraider_server.esologs.responses.core import EsoLogsDataClass
from esoraider_server.esologs.responses.report_data.report import Report
from esoraider_server.esologs.responses.world_data.encounter import Encounter


@dataclass
class ReportData(EsoLogsDataClass):
    report: Report


@dataclass
class WorldData(EsoLogsDataClass):
    encounter: Encounter


@dataclass
class BaseResponseData(EsoLogsDataClass):
    report_data: Optional[ReportData] = None
    world_data: Optional[WorldData] = None
