from data.buffs import BUFFS
from data.classes.dragonknight.debuffs import DRAGONKNIGHT_DEBUFFS
from data.core import EsoEnum, Skill
from data.stacks import DEBUFFS_WITH_STACKS


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
