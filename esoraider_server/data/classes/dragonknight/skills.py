from esoraider_server.data.buffs import BUFFS
from esoraider_server.data.classes.dragonknight.buffs import DRAGONKNIGHT_BUFFS
from esoraider_server.data.classes.dragonknight.debuffs import (
    DRAGONKNIGHT_DEBUFFS,
)
from esoraider_server.data.core import EsoEnum, Skill
from esoraider_server.data.stacks import DEBUFFS_WITH_STACKS


class DRAGONKNIGHT_SKILLS(EsoEnum):
    # Has multiple IDs - 133027, 134355, 134340
    STONE_GIANT = Skill(
        name='Stone Giant',
        id=31816,
        debuffs=[DEBUFFS_WITH_STACKS.STAGGER.value],
        link='https://eso-hub.com/en/skills/dragonknight/earthen-heart/stone-giant',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_013_a.png',
    )
    # TODO: Any way to track percentage of additional damage taken?
    ENGULFING_FLAMES = Skill(
        name='Engulfing Flames',
        id=20930,
        debuffs=[DRAGONKNIGHT_DEBUFFS.ENGULFING_FLAMES_DAMAGE.value],
        link='https://eso-hub.com/en/skills/dragonknight/ardent-flame/engulfing-flames',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_004_b.png',
    )
    NOXIOUS_BREATH = Skill(
        name='Noxious Breath',
        id=20944,
        debuffs=[DRAGONKNIGHT_DEBUFFS.NOXIOUS_BREATH.value],
        link='https://eso-hub.com/en/skills/dragonknight/ardent-flame/noxious-breath',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_004_a.png',
    )
    IGNEOUS_WEAPONS = Skill(
        name='Igneous Weapons',
        id=31874,
        buffs=[BUFFS.MAJOR_BRUTALITY.value, BUFFS.MAJOR_SORCERY.value],
        link='https://eso-hub.com/en/skills/dragonknight/earthen-heart/igneous-weapons',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_015_a.png',
    )
    BURNING_EMBERS = Skill(
        name='Burning Embers',
        id=20660,
        debuffs=[DRAGONKNIGHT_DEBUFFS.BURNING_EMBERS.value],
        link='https://eso-hub.com/en/skills/dragonknight/ardent-flame/burning-embers',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_003_b.png',
    )
    VENOMOUS_CLAW = Skill(
        name='Venomous Claw',
        id=20668,
        debuffs=[DRAGONKNIGHT_DEBUFFS.VENOMOUS_CLAW.value],
        link='https://eso-hub.com/en/skills/dragonknight/ardent-flame/venomous-claw',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_003_a.png',
    )
    ERUPTION_INITIAL_DAMAGE = Skill(
        name='Eruption',
        id=32714,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_016b.png',
    )
    ERUPTION_DAMAGE = Skill(
        name='Eruption',
        id=32711,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_016b.png',
    )
    ERUPTION = Skill(
        name='Eruption',
        id=32710,
        children=[ERUPTION_INITIAL_DAMAGE, ERUPTION_DAMAGE],
        link='https://eso-hub.com/en/skills/dragonknight/earthen-heart/eruption',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_016b.png',
    )
    FLAMES_OF_OBLIVION_DAMAGE = Skill(
        name='Flames of Oblivion',
        id=61945,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_002_a.png',
    )
    FLAMES_OF_OBLIVION = Skill(
        name='Flames of Oblivion',
        id=32853,
        tick=5,
        buffs=[
            BUFFS.MAJOR_PROPHECY_FLAMES_OF_OBLIVION.value,
            BUFFS.MAJOR_SAVAGERY_FLAMES_OF_OBLIVION.value,
        ],
        children=[FLAMES_OF_OBLIVION_DAMAGE],
        link='https://eso-hub.com/en/skills/dragonknight/ardent-flame/flames-of-oblivion',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_002_a.png',
    )
    HARDENED_ARMOR = Skill(
        name='Hardened Armor',
        id=20328,  # Additional ID - 31808, probably 6 sec shield
        buffs=[
            DRAGONKNIGHT_BUFFS.HARDENED_ARMOR.value,
            BUFFS.MAJOR_RESOLVE_HARDENED_ARMOR.value,
        ],
        link='https://eso-hub.com/en/skills/dragonknight/draconic-power/hardened-armor',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_007_b.png',
    )
