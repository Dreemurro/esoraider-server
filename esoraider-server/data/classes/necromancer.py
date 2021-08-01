from data.core import EsoEnum, Skill


class NECROMANCER_BUFFS(EsoEnum):
    pass


class NECROMANCER_DEBUFFS(EsoEnum):
    pass


class NECROMANCER_SKILLS(EsoEnum):
    UNNERVING_BONEYARD_DAMAGE = Skill(
        name='Unnerving Boneyard',
        id=117809,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_necromancer_004_a.png',
    )
    UNNERVING_BONEYARD = Skill(
        name='Unnerving Boneyard',
        id=117805,
        link='https://eso-hub.com/en/skills/necromancer/grave-lord/unnerving-boneyard',
        children=[UNNERVING_BONEYARD_DAMAGE],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_necromancer_004_a.png',
    )
    DETONATING_SIPHON_EXPLOSION = Skill(
        name='Detonating Siphon',
        id=123082,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_necromancer_005_b.png',
    )
    DETONATING_SIPHON_DAMAGE = Skill(
        name='Detonating Siphon',
        id=118766,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_necromancer_005_b.png',
    )
    DETONATING_SIPHON = Skill(
        name='Detonating Siphon',
        id=118763,
        link='https://eso-hub.com/en/skills/necromancer/grave-lord/detonating-siphon',
        children=[DETONATING_SIPHON_DAMAGE, DETONATING_SIPHON_EXPLOSION],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_necromancer_005_b.png',
    )
