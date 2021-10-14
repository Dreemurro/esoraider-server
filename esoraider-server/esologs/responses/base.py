"""Main body of any response."""

from dataclasses import dataclass
from typing import Optional

from esologs.responses.core import EsoLogsDataClass
from esologs.responses.report_data.report import Report


@dataclass
class ReportData(EsoLogsDataClass):
    report: Optional[Report] = None


@dataclass
class BaseResponseData(EsoLogsDataClass):
    report_data: Optional[ReportData] = None
