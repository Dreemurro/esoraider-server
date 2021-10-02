from data.classes.dragonknight.debuffs import DRAGONKNIGHT_DEBUFFS
from data.classes.templar.debuffs import TEMPLAR_DEBUFFS
from data.classes.warden.debuffs import WARDEN_DEBUFFS
from data.core import Buff, Debuff, EsoEnum, Stack
from data.debuffs import DEBUFFS


class STACKS(EsoEnum):
    #
    # Sets
    #
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
            DEBUFFS.POISON_INJECTION.value,

            # DW
            # Twin Blade and Blunt Bleed
            DEBUFFS.RENDING_SLASHES.value,

            # 2H
            # Heavy Weapons Bleed
            # Carve

            # Destruction Staff
            DEBUFFS.FROST_REACH.value,
            # DEBUFFS Shock Reach
            DEBUFFS.FLAME_REACH.value,

            DRAGONKNIGHT_DEBUFFS.ENGULFING_FLAMES_DAMAGE.value,
            DRAGONKNIGHT_DEBUFFS.BURNING_EMBERS.value,
            WARDEN_DEBUFFS.FETCHER_INFECTION.value,
            WARDEN_DEBUFFS.GROWING_SWARM.value,
            TEMPLAR_DEBUFFS.VAMPIRES_BANE.value,
            # TEMPLAR_DEBUFFS Reflective Light
        ]
    )
    ARMS_OF_RELEQUEN = Stack(
        name='Arms of Relequen',
        id=107203,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_003.png',
        max_stacks=10,
        type_='Debuff',
    )
    IDEAL_ARMS_OF_RELEQUEN = Stack(
        name='Ideal Arms of Relequen',
        id=109086,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_003.png',
        max_stacks=10,
        type_='Debuff',
    )
    SIRORIAS_BOON = Stack(
        name='Siroria\'s Boon',
        id=110118,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_010.png',
        max_stacks=10,
        type_='Buff',
    )
    BERSERKING_WARRIOR = Stack(
        name='Berserking Warrior',
        id=50978,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warrior_005.png',
        max_stacks=10,
        type_='Buff',
    )

    """
    Dragonknight
    """
    STAGGER = Stack(
        name='Stagger',
        id=134336,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_013_a.png',
        max_stacks=3,
        type_='Debuff',
    )

    """
    Nightblade
    """
    MERCILESS_RESOLVE = Stack(
        name='Merciless Resolve',
        id=61920,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_005_b.png',
        max_stacks=5,
        type_='Buff',
    )
    RELENTLESS_FOCUS = Stack(
        name='Relentless Focus',
        id=61928,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_005_a.png',
        max_stacks=5,
        type_='Buff',
    )


class BUFFS_WITH_STACKS(EsoEnum):
    #
    # Sets
    #
    HUNTERS_FOCUS = Buff(
        name='Hunter\'s Focus',
        id=155150,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_rogue_066.png',
        stack=STACKS.HUNTERS_FOCUS.value,
    )
    SIRORIAS_BOON = Buff(
        name='Siroria\'s Boon',
        id=110118,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_010.png',
        stack=STACKS.SIRORIAS_BOON.value,
    )
    BERSERKING_WARRIOR = Buff(
        name='Berserking Warrior',
        id=50978,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warrior_005.png',
        stack=STACKS.BERSERKING_WARRIOR.value,
    )

    """
    Nightblade
    """
    MERCILESS_RESOLVE = Buff(
        name='Merciless Resolve',
        id=61919,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_005_b.png',
        stack=STACKS.MERCILESS_RESOLVE.value,
    )
    RELENTLESS_FOCUS = Buff(
        name='Relentless Focus',
        id=61927,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_005_a.png',
        stack=STACKS.RELENTLESS_FOCUS.value,
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
    ARMS_OF_RELEQUEN = Debuff(
        name='Arms of Relequen',
        id=107203,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_003.png',
        stack=STACKS.ARMS_OF_RELEQUEN.value,
    )
    IDEAL_ARMS_OF_RELEQUEN = Debuff(
        name='Ideal Arms of Relequen',
        id=109086,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_003.png',
        stack=STACKS.IDEAL_ARMS_OF_RELEQUEN.value,
    )

    """
    Dragonknight
    """
    STAGGER = Debuff(
        name='Stagger',
        id=134336,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_013_a.png',
        stack=STACKS.STAGGER.value,
    )
