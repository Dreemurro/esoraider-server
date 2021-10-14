from dataclasses import dataclass, field

from dataclasses_json import config
from esologs.responses.core import EsoLogsDataClass


@dataclass
class Fight(EsoLogsDataClass):
    difficulty: int
    encounter_id: int = field(metadata=config(field_name='encounterID'))
