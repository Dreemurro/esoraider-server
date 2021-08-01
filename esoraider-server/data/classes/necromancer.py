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
