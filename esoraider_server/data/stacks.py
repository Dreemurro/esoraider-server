from esoraider_server.data.classes.dragonknight.debuffs import (
    DRAGONKNIGHT_DEBUFFS,
)
from esoraider_server.data.classes.templar.debuffs import TEMPLAR_DEBUFFS
from esoraider_server.data.classes.warden.debuffs import WARDEN_DEBUFFS
from esoraider_server.data.core import Buff, Debuff, EsoEnum, Stack
from esoraider_server.data.debuffs import DEBUFFS
from esoraider_server.esologs.consts import DataType


class STACKS(EsoEnum):
    #
    # Sets
    #
    HUNTERS_FOCUS = Stack(
        name='Hunter\'s Focus',
        id=155150,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_rogue_066.png',
        max_stacks=10,
        type_=DataType.BUFFS,
    )
    TOUCH_OF_ZEN = Stack(
        name='Touch of Z\'en',
        id=126597,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_healer_006.png',
        max_stacks=5,
        type_=DataType.DEBUFFS,
        debuffs=[
            # This list is initially based on a work of Pandamime & Seaunicorn
            # Enchants
            DEBUFFS.POISONED.value,
            DEBUFFS.BURNING.value,
            # Poisons
            DEBUFFS.CREEPING_RAVAGE_HEALTH.value,
            DEBUFFS.RAVAGE_HEALTH.value,
            # Soul Magic
            DEBUFFS.CONSUMING_TRAP.value,
            # DEBUFFS Soul Splitting Trap

            # Fighters Guild
            DEBUFFS.BARBED_TRAP.value,
            DEBUFFS.LIGHTWEIGHT_BEAST_TRAP.value,

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
            DEBUFFS.CARVE.value,

            # Destruction Staff
            DEBUFFS.FROST_REACH.value,
            DEBUFFS.SHOCK_REACH.value,
            DEBUFFS.FLAME_REACH.value,

            DRAGONKNIGHT_DEBUFFS.ENGULFING_FLAMES_DAMAGE.value,
            DRAGONKNIGHT_DEBUFFS.NOXIOUS_BREATH.value,
            DRAGONKNIGHT_DEBUFFS.BURNING_EMBERS.value,
            DRAGONKNIGHT_DEBUFFS.VENOMOUS_CLAW.value,
            DRAGONKNIGHT_DEBUFFS.BURNING_TALONS.value,
            WARDEN_DEBUFFS.FETCHER_INFECTION.value,
            WARDEN_DEBUFFS.GROWING_SWARM.value,
            TEMPLAR_DEBUFFS.VAMPIRES_BANE.value,
            # TEMPLAR_DEBUFFS Reflective Light
        ],
    )
    ARMS_OF_RELEQUEN = Stack(
        name='Arms of Relequen',
        id=107203,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_003.png',
        max_stacks=10,
        type_=DataType.DEBUFFS,
    )
    SIRORIAS_BOON = Stack(
        name='Siroria\'s Boon',
        id=110118,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_010.png',
        max_stacks=10,
        type_=DataType.BUFFS,
    )
    BERSERKING_WARRIOR = Stack(
        name='Berserking Warrior',
        id=50978,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warrior_005.png',
        max_stacks=10,
        type_=DataType.BUFFS,
    )
    PRICE_OF_PRIDE = Stack(
        name='Price of Pride',
        id=163404,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_065.png',
        max_stacks=6,
        type_=DataType.BUFFS,
    )
    THUNDEROUS_VOLLEY = Stack(
        name='Thunderous Volley',
        id=99853,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_065.png',
        max_stacks=8,
        type_=DataType.BUFFS,
    )
    BAHSEIS_MANIA = Stack(
        name="Bahsei's Mania",
        id=100,  # Resource ID of magicka
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_065.png',
        max_stacks=15,
        type_=DataType.RESOURCES,
        modifier=lambda x: round((100 - x) * 0.15),
    )
    TRUE_SWORN_FURY = Stack(
        name='True-Sworn Fury',
        id=1000,  # Resource ID of health
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_065.png',
        max_stacks=3,
        type_=DataType.RESOURCES,
        modifier=lambda x:
            3 if x in range(50)
            else (2 if x in range(50, 75) else 1),
    )

    #
    # General skills
    #
    CARVE = Stack(
        name='Carve',
        id=38747,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_2handed_002_a.png',
        max_stacks=3,
        type_=DataType.DEBUFFS,
    )

    """
    Dragonknight
    """
    STAGGER = Stack(
        name='Stagger',
        id=134336,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_013_a.png',
        max_stacks=3,
        type_=DataType.DEBUFFS,
    )

    """
    Nightblade
    """
    MERCILESS_RESOLVE = Stack(
        name='Merciless Resolve',
        id=61920,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_005_b.png',
        max_stacks=5,
        type_=DataType.BUFFS,
    )
    RELENTLESS_FOCUS = Stack(
        name='Relentless Focus',
        id=61928,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_005_a.png',
        max_stacks=5,
        type_=DataType.BUFFS,
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
    PRICE_OF_PRIDE = Buff(
        name='Price of Pride',
        id=163404,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_065.png',
        stack=STACKS.PRICE_OF_PRIDE.value,
    )
    THUNDEROUS_VOLLEY = Buff(
        name='Thunderous Volley',
        id=99853,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_065.png',
        stack=STACKS.THUNDEROUS_VOLLEY.value,
    )
    BAHSEIS_MANIA = Buff(
        name="Bahsei's Mania",
        id=100,  # Resource ID of magicka
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_065.png',
        stack=STACKS.BAHSEIS_MANIA.value,
    )
    TRUE_SWORN_FURY = Buff(
        name='True-Sworn Fury',
        id=1000,  # Resource ID of health
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_065.png',
        stack=STACKS.TRUE_SWORN_FURY.value,
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

    #
    # General skills
    #
    CARVE = Debuff(
        name='Carve',
        id=38747,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_2handed_002_a.png',
        stack=STACKS.CARVE.value,
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
