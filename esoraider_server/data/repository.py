from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

from structlog.stdlib import get_logger

from esoraider_server.data.buffs import Buffs
from esoraider_server.data.debuffs import Debuffs
from esoraider_server.data.encounters import Encounters
from esoraider_server.data.glyphs import Glyphs
from esoraider_server.data.sets import GearSets

if TYPE_CHECKING:
    from esoraider_server.data import core

logger = get_logger()


class ESODataRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_encounter(self, id_: int) -> 'core.Encounter | None':
        raise NotImplementedError

    @abstractmethod
    def get_gear_set(self, id_: int) -> 'core.GearSet | None':
        raise NotImplementedError

    @abstractmethod
    def get_glyph(self, id_: int) -> 'core.Glyph | None':
        raise NotImplementedError

    @abstractmethod
    def get_fight_buffs(self) -> 'list[core.Buff]':
        raise NotImplementedError

    @abstractmethod
    def get_fight_debuffs(self) -> 'list[core.Debuff]':
        raise NotImplementedError


class EnumESODataRepository(ESODataRepository):
    def get_encounter(self, id_: int) -> 'core.Encounter | None':
        try:
            return Encounters(id_).value
        except StopIteration:
            return None

    def get_gear_set(self, id_: int) -> 'core.GearSet | None':
        try:
            return GearSets(id_).value
        except StopIteration:
            return None

    def get_glyph(self, id_: int) -> 'core.Glyph | None':
        try:
            return Glyphs(id_).value
        except StopIteration:
            return None

    def get_fight_buffs(self) -> 'list[core.Buff]':
        return [
            Buffs.MAJOR_COURAGE.value,  # Spell Power Cure, Olorime
            Buffs.MAJOR_FORCE.value,  # Saxhleel, Aggressive Horn
            # BUFFS.MAJOR_PROPHECY.value,  # Potions
            Buffs.MAJOR_RESOLVE.value,  # Frost Cloak
            # BUFFS.MAJOR_SAVAGERY.value,  # Potions
            Buffs.MAJOR_SLAYER.value,  # Master Architect, War Machine, Roaring
            Buffs.MAJOR_SORCERY.value,  # Potions, Igneous Weapons
            Buffs.MINOR_BERSERK.value,  # Combat Prayer
            Buffs.MINOR_PROPHECY.value,  # Sorc passive
            Buffs.MINOR_SAVAGERY.value,  # NB passive
            Buffs.MINOR_SORCERY.value,  # Templar passive
            Buffs.AGGRESSIVE_HORN.value,
        ]

    def get_fight_debuffs(self) -> 'list[core.Debuff]':
        return [
            Debuffs.MAJOR_BREACH.value,
            Debuffs.MAJOR_VULNERABILITY.value,
            Debuffs.MINOR_BREACH.value,
            Debuffs.MINOR_BRITTLE.value,
            Debuffs.MINOR_LIFESTEAL.value,
            Debuffs.MINOR_MAGICKASTEAL.value,
            Debuffs.MINOR_MAIM.value,
            Debuffs.MINOR_VULNERABILITY.value,
            Debuffs.CRUSHER.value,
        ]
