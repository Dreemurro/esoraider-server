from dataclasses import dataclass, field
from typing import Optional, Union

from dataclasses_json import config
from esologs.consts import GearSlot, GearType, PoisonType, WeaponType
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
    quality: int
    icon: str
    champion_points: int
    trait: int
    enchant_type: int
    enchant_quality: int
    set_id: int = field(metadata=config(field_name='setID'))

    slot: Optional[GearSlot] = None
    name: Optional[str] = None
    type: Union[GearType, WeaponType, PoisonType, None] = None
    set_name: Optional[str] = None
