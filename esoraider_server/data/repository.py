from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

from structlog.stdlib import get_logger

from esoraider_server.data.encounters import Encounters
from esoraider_server.data.glyphs import Glyphs
from esoraider_server.data.sets import GearSets

if TYPE_CHECKING:
    from esoraider_server.data.core import Encounter, GearSet, Glyph

logger = get_logger()


class ESODataRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_encounter(self, id_: int) -> 'Encounter | None':
        raise NotImplementedError

    @abstractmethod
    def get_gear_set(self, id_: int) -> 'GearSet | None':
        raise NotImplementedError

    @abstractmethod
    def get_glyph(self, id_: int) -> 'Glyph | None':
        raise NotImplementedError


class EnumESODataRepository(ESODataRepository):
    def get_encounter(self, id_: int) -> 'Encounter | None':
        try:
            return Encounters(id_).value
        except StopIteration:
            return None

    def get_gear_set(self, id_: int) -> 'GearSet | None':
        try:
            return GearSets(id_).value
        except StopIteration:
            return None

    def get_glyph(self, id_: int) -> 'Glyph | None':
        try:
            return Glyphs(id_).value
        except StopIteration:
            return None
