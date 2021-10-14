from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json import config
from esologs.responses.core import EsoLogsDataClass


@dataclass
class Talent(EsoLogsDataClass):
    name: str
    guid: int
    type: int
    ability_icon: str
    flags: int


@dataclass
class Gear(EsoLogsDataClass):
    id: int
    slot: int
    quality: int
    icon: str
    champion_points: int
    trait: int
    enchant_type: int
    enchant_quality: int
    set_id: int = field(metadata=config(field_name='setID'))

    name: Optional[str] = None
    type: Optional[int] = None
    set_name: Optional[str] = None
