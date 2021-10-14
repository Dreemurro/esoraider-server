"""Main body of any response."""

from dataclasses import dataclass
from typing import Optional

from esologs.responses.core import EsoLogsDataClass
from esologs.responses.report_data.report import Report
from esologs.responses.world_data.encounter import Encounter


@dataclass
class ReportData(EsoLogsDataClass):
    report: Optional[Report] = None


@dataclass
class WorldData(EsoLogsDataClass):
    encounter: Optional[Encounter] = None


@dataclass
class BaseResponseData(EsoLogsDataClass):
    report_data: Optional[ReportData] = None
    world_data: Optional[WorldData] = None
