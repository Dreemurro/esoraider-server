from data.classes.necromancer.buffs import NECROMANCER_BUFFS
from data.core import EsoEnum, Skill
from data.debuffs import DEBUFFS


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
    MYSTIC_SIPHON_DAMAGE = Skill(
        name='Mystic Siphon',
        id=118011,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_necromancer_005_a.png',
    )
    MYSTIC_SIPHON = Skill(
        name='Mystic Siphon',
        id=118008,
        link='https://eso-hub.com/en/skills/necromancer/grave-lord/mystic-siphon',
        children=[MYSTIC_SIPHON_DAMAGE],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_necromancer_005_a.png',
    )
    SKELETAL_ARCANIST = Skill(
        name='Skeletal Arcanist',
        id=118726,
        link='https://eso-hub.com/en/skills/necromancer/grave-lord/skeletal-arcanist',
        buffs=[NECROMANCER_BUFFS.SKELETAL_ARCANIST.value],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_necromancer_003_b.png',
    )
    PESTILENT_COLOSSUS = Skill(
        name='Pestilent Colossus',
        id=122395,
        link='https://eso-hub.com/en/skills/necromancer/grave-lord/pestilent-colossus',
        debuffs=[DEBUFFS.MAJOR_VULNERABILITY.value],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_necromancer_006_b.png',
    )
    GLACIAL_COLOSSUS = Skill(
        name='Glacial Colossus',
        id=122388,
        link='https://eso-hub.com/en/skills/necromancer/grave-lord/glacial-colossus',
        debuffs=[DEBUFFS.MAJOR_VULNERABILITY.value],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_necromancer_006_a.png',
    )
