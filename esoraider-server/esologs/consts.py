from enum import IntEnum, unique


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
