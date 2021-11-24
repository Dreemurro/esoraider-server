from dataclasses import dataclass, field
from typing import Optional, Union

from dataclasses_json import config

from esoraider_server.esologs.consts import (
    GearSlot,
    GearType,
    PoisonType,
    WeaponType,
)
from esoraider_server.esologs.responses.core import EsoLogsDataClass


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
    # int is only needed for initial decoding, it will be replaced later
    type: Union[GearType, WeaponType, PoisonType, int, None] = None
    set_name: Optional[str] = None
