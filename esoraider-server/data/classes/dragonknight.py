from data.classes.general import BUFFS
from data.core import Debuff, EsoEnum, Skill


class DRAGONKNIGHT_BUFFS(EsoEnum):
    pass


class DRAGONKNIGHT_DEBUFFS(EsoEnum):
    STAGGER = Debuff(
        name='Stagger',
        id=134336,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_013_a.png',
    )
    ENGULFING_FLAMES_DAMAGE = Debuff(
        name='Engulfing Flames',
        id=31104,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_004_b.png',
    )
    BURNING_EMBERS = Debuff(
        name='Burning Embers',
        id=44373,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_003_b.png',
    )


class DRAGONKNIGHT_SKILLS(EsoEnum):
    # TODO: Appears on uptimes list, its not a DoT
    # TODO: Has multiple IDs - 133027, 134355, 134340
    STONE_GIANT = Skill(
        name='Stone Giant',
        id=31816,
        debuffs=[DRAGONKNIGHT_DEBUFFS.STAGGER.value],
        link='https://eso-hub.com/en/skills/dragonknight/earthen-heart/stone-giant',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_013_a.png',
    )
    # TODO: Any way to track percentage of additional damage taken?
    # TODO: Wrong uptime (probably shows initial hit, not the DoT)
    ENGULFING_FLAMES = Skill(
        name='Engulfing Flames',
        id=20930,
        debuffs=[DRAGONKNIGHT_DEBUFFS.ENGULFING_FLAMES_DAMAGE.value],
        link='https://eso-hub.com/en/skills/dragonknight/ardent-flame/engulfing-flames',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_004_b.png',
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
