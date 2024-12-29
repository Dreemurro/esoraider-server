from enum import Enum, IntEnum, auto, unique


@unique
class CharClass(Enum):
    DRAGONKNIGHT = 'DragonKnight'
    NIGHTBLADE = 'Nightblade'
    SORCERER = 'Sorcerer'
    TEMPLAR = 'Templar'
    WARDEN = 'Warden'
    NECROMANCER = 'Necromancer'
    ARCANIST = 'Arcanist'


@unique
class GearSlot(IntEnum):
    HEAD = 0
    CHEST = 1
    SHOULDERS = 2
    WAIST = 3
    HANDS = 4
    LEGS = 5
    FEET = 6
    NECK = 7
    RING_1 = 8
    RING_2 = 9
    MAIN_HAND = 10
    OFF_HAND = 11
    MAIN_HAND_BACKUP = 12
    OFF_HAND_BACKUP = 13
    MAIN_POISON = 14
    BACKUP_POISON = 15

    @classmethod
    def is_armor(cls, x: 'GearSlot') -> bool:
        return cls.HEAD <= x <= cls.RING_2

    @classmethod
    def is_weapon(cls, x: 'GearSlot') -> bool:
        return cls.MAIN_HAND <= x <= cls.OFF_HAND_BACKUP

    @classmethod
    def is_frontbar_weapon(cls, x: 'GearSlot') -> bool:
        return cls.MAIN_HAND <= x <= cls.OFF_HAND

    @classmethod
    def is_backbar_weapon(cls, x: 'GearSlot') -> bool:
        return cls.MAIN_HAND_BACKUP <= x <= cls.OFF_HAND_BACKUP

    @classmethod
    def is_poison(cls, x: 'GearSlot') -> bool:
        return cls.MAIN_POISON <= x <= cls.BACKUP_POISON


@unique
class GearType(Enum):
    LIGHT_ARMOR = 1
    MEDIUM_ARMOR = 2
    HEAVY_ARMOR = 3
    JEWELRY = 4


@unique
class PoisonType(Enum):
    POISON = 1


@unique
class WeaponType(Enum):
    AXE = 1
    MACE = 2
    SWORD = 3
    TWO_HANDED_SWORD = 4
    TWO_HANDED_AXE = 5
    TWO_HANDED_HAMMER = 6
    BOW = 8
    HEALING_STAFF = 9
    DAGGER = 11
    FIRE_STAFF = 12
    FROST_STAFF = 13
    SHIELD = 14
    LIGHTNING_STAFF = 15

    @classmethod
    def wield_type(cls, first: 'WeaponType', second: 'WeaponType' = None):
        if second:
            if second == cls.SHIELD:
                return WieldType.ONE_HAND_AND_SHIELD
            return WieldType.DUAL_WIELD

        wield = {
            cls.FIRE_STAFF: WieldType.DESTRUCTION_STAFF,
            cls.FROST_STAFF: WieldType.DESTRUCTION_STAFF,
            cls.LIGHTNING_STAFF: WieldType.DESTRUCTION_STAFF,
            cls.HEALING_STAFF: WieldType.RESTORATION_STAFF,
            cls.BOW: WieldType.BOW,
            cls.TWO_HANDED_AXE: WieldType.TWO_HANDED,
            cls.TWO_HANDED_SWORD: WieldType.TWO_HANDED,
            cls.TWO_HANDED_HAMMER: WieldType.TWO_HANDED,
        }
        return wield.get(first, WieldType.INCOMPLETE)


@unique
class WieldType(Enum):
    BOW = auto()
    DESTRUCTION_STAFF = auto()
    DUAL_WIELD = auto()
    ONE_HAND_AND_SHIELD = auto()
    RESTORATION_STAFF = auto()
    TWO_HANDED = auto()

    INCOMPLETE = auto()


@unique
class DataType(Enum):
    SUMMARY = 'Summary'
    DAMAGE_DONE = 'DamageDone'
    CASTS = 'Casts'
    BUFFS = 'Buffs'
    DEBUFFS = 'Debuffs'
    RESOURCES = 'Resources'
    COMBATANT_INFO = 'CombatantInfo'


@unique
class HostilityType(Enum):
    FRIENDLIES = 'Friendlies'
    ENEMIES = 'Enemies'
