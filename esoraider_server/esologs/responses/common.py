from typing import Optional, Union

from msgspec import field

from esoraider_server.esologs.consts import (
    GearSlot,
    GearType,
    PoisonType,
    WeaponType,
)
from esoraider_server.esologs.responses.core import EsoLogsDataClass


class Talent(EsoLogsDataClass):
    name: str
    guid: int
    type: int
    ability_icon: str
    flags: int


class Gear(EsoLogsDataClass):
    id: int
    quality: int
    icon: str
    champion_points: int
    trait: int
    enchant_type: int
    enchant_quality: int
    set_id: int = field(name='setID')

    slot: Optional[GearSlot] = None
    name: Optional[str] = None
    # int is only needed for initial decoding, it will be replaced later
    _type: Union[int, None] = field(default=None, name='type')
    set_name: Optional[str] = None

    @property
    def type(self) -> GearType | WeaponType | PoisonType | None:
        if not self._type or not self.slot:
            return None

        if GearSlot.is_armor(self.slot):
            return GearType(self._type)
        elif GearSlot.is_weapon(self.slot):
            return WeaponType(self._type)
        elif GearSlot.is_poison(self.slot):
            return PoisonType(self._type)
        return None
