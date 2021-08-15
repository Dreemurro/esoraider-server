from data.core import Buff, Debuff, EsoEnum, Stack
from data.debuffs import DEBUFFS
from data.classes.dragonknight.debuffs import DRAGONKNIGHT_DEBUFFS
from data.classes.warden.debuffs import WARDEN_DEBUFFS
from data.classes.templar.debuffs import TEMPLAR_DEBUFFS


class STACKS(EsoEnum):
    """
    Sets
    """
    HUNTERS_FOCUS = Stack(
        name='Hunter\'s Focus',
        id=155150,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_rogue_066.png',
        max_stacks=10,
        type_='Buff',
    )
    TOUCH_OF_ZEN = Stack(
        name='Touch of Z\'en',
        id=126597,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_healer_006.png',
        max_stacks=5,
        type_='Debuff',
        debuffs=[
            # This list is initially based on a work of Pandamime & Seaunicorn
            # Enchants
            DEBUFFS.POISONED.value,
            DEBUFFS.BURNING.value,
            # Soul Magic
            DEBUFFS.CONSUMING_TRAP.value,
            # DEBUFFS Soul Splitting Trap

            # Fighters Guild
            DEBUFFS.BARBED_TRAP.value,
            # DEBUFFS Trap Beast

            # Mages Guild
            DEBUFFS.SCALDING_RUNE.value,
            DEBUFFS.DEGENERATION.value,
            DEBUFFS.STRUCTURED_ENTROPY.value,

            # Bow
            # Poison Injection

            # DW
            # Twin Blade and Blunt Bleed
            # Rending Slashes

            # 2H
            # Heavy Weapons Bleed
            # Carve

            # Destruction Staff
            DEBUFFS.FROST_REACH.value,
            # DEBUFFS Shock Reach
            # DEBUFFS Flame Reach

            DRAGONKNIGHT_DEBUFFS.ENGULFING_FLAMES_DAMAGE.value,
            DRAGONKNIGHT_DEBUFFS.BURNING_EMBERS.value,
            WARDEN_DEBUFFS.FETCHER_INFECTION.value,
            # WARDEN_DEBUFFS Growing Swarm
            TEMPLAR_DEBUFFS.VAMPIRES_BANE.value,
            # TEMPLAR_DEBUFFS Reflective Light
        ]
    )


class BUFFS_WITH_STACKS(EsoEnum):
    """
    Sets
    """
    HUNTERS_FOCUS = Buff(
        name='Hunter\'s Focus',
        id=155150,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_rogue_066.png',
        stack=STACKS.HUNTERS_FOCUS.value,
    )


class DEBUFFS_WITH_STACKS(EsoEnum):
    """
    Sets
    """
    TOUCH_OF_ZEN = Debuff(
        name='Touch of Z\'en',
        id=126597,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_healer_006.png',
        stack=STACKS.TOUCH_OF_ZEN.value,
    )
