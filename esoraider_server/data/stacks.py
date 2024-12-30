from esoraider_server.data.classes.dragonknight.debuffs import (
    DragonknightDebuffs,
)
from esoraider_server.data.classes.templar.debuffs import TemplarDebuffs
from esoraider_server.data.classes.warden.debuffs import WardenDebuffs
from esoraider_server.data.core import Buff, Debuff, EsoEnum, Stack
from esoraider_server.data.debuffs import Debuffs
from esoraider_server.esologs.consts import DataType


class Stacks(EsoEnum):
    #
    # Sets
    #
    HUNTERS_FOCUS = Stack(
        name="Hunter's Focus",
        id=155150,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_rogue_066.png',
        max_stacks=10,
        type_=DataType.BUFFS,
    )
    TOUCH_OF_ZEN = Stack(
        name="Touch of Z'en",
        id=126597,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_healer_006.png',
        max_stacks=5,
        type_=DataType.DEBUFFS,
        debuffs=[
            # This list is initially based on a work of Pandamime & Seaunicorn
            # Enchants
            Debuffs.POISONED.value,
            Debuffs.BURNING.value,
            # Poisons
            Debuffs.CREEPING_RAVAGE_HEALTH.value,
            Debuffs.RAVAGE_HEALTH.value,
            # Soul Magic
            Debuffs.CONSUMING_TRAP.value,
            # DEBUFFS Soul Splitting Trap

            # Fighters Guild
            Debuffs.BARBED_TRAP.value,
            Debuffs.LIGHTWEIGHT_BEAST_TRAP.value,

            # Mages Guild
            Debuffs.SCALDING_RUNE.value,
            Debuffs.DEGENERATION.value,
            Debuffs.STRUCTURED_ENTROPY.value,

            # Bow
            Debuffs.POISON_INJECTION.value,

            # DW
            # Twin Blade and Blunt Bleed
            Debuffs.RENDING_SLASHES.value,

            # 2H
            # Heavy Weapons Bleed
            # Carve
            Debuffs.CARVE.value,

            # Destruction Staff
            Debuffs.FROST_REACH.value,
            Debuffs.SHOCK_REACH.value,
            Debuffs.FLAME_REACH.value,

            DragonknightDebuffs.ENGULFING_FLAMES_DAMAGE.value,
            DragonknightDebuffs.NOXIOUS_BREATH.value,
            DragonknightDebuffs.BURNING_EMBERS.value,
            DragonknightDebuffs.VENOMOUS_CLAW.value,
            DragonknightDebuffs.BURNING_TALONS.value,
            WardenDebuffs.FETCHER_INFECTION.value,
            WardenDebuffs.GROWING_SWARM.value,
            TemplarDebuffs.VAMPIRES_BANE.value,
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
        name="Siroria's Boon",
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


class BuffsWithStacks(EsoEnum):
    #
    # Sets
    #
    HUNTERS_FOCUS = Buff(
        name="Hunter's Focus",
        id=155150,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_rogue_066.png',
        stack=Stacks.HUNTERS_FOCUS.value,
    )
    SIRORIAS_BOON = Buff(
        name="Siroria's Boon",
        id=110118,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_010.png',
        stack=Stacks.SIRORIAS_BOON.value,
    )
    BERSERKING_WARRIOR = Buff(
        name='Berserking Warrior',
        id=50978,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warrior_005.png',
        stack=Stacks.BERSERKING_WARRIOR.value,
    )
    PRICE_OF_PRIDE = Buff(
        name='Price of Pride',
        id=163404,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_065.png',
        stack=Stacks.PRICE_OF_PRIDE.value,
    )
    THUNDEROUS_VOLLEY = Buff(
        name='Thunderous Volley',
        id=99853,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_065.png',
        stack=Stacks.THUNDEROUS_VOLLEY.value,
    )
    BAHSEIS_MANIA = Buff(
        name="Bahsei's Mania",
        id=100,  # Resource ID of magicka
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_065.png',
        stack=Stacks.BAHSEIS_MANIA.value,
    )
    TRUE_SWORN_FURY = Buff(
        name='True-Sworn Fury',
        id=1000,  # Resource ID of health
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_065.png',
        stack=Stacks.TRUE_SWORN_FURY.value,
    )

    """
    Nightblade
    """
    MERCILESS_RESOLVE = Buff(
        name='Merciless Resolve',
        id=61919,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_005_b.png',
        stack=Stacks.MERCILESS_RESOLVE.value,
    )
    RELENTLESS_FOCUS = Buff(
        name='Relentless Focus',
        id=61927,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_005_a.png',
        stack=Stacks.RELENTLESS_FOCUS.value,
    )


class DebuffsWithStacks(EsoEnum):
    """
    Sets
    """
    TOUCH_OF_ZEN = Debuff(
        name="Touch of Z'en",
        id=126597,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_healer_006.png',
        stack=Stacks.TOUCH_OF_ZEN.value,
    )
    ARMS_OF_RELEQUEN = Debuff(
        name='Arms of Relequen',
        id=107203,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_003.png',
        stack=Stacks.ARMS_OF_RELEQUEN.value,
    )

    #
    # General skills
    #
    CARVE = Debuff(
        name='Carve',
        id=38747,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_2handed_002_a.png',
        stack=Stacks.CARVE.value,
    )

    """
    Dragonknight
    """
    STAGGER = Debuff(
        name='Stagger',
        id=134336,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_013_a.png',
        stack=Stacks.STAGGER.value,
    )
