from esoraider_server.data.buffs import Buffs
from esoraider_server.data.classes.arcanist.buffs import ArcanistBuffs
from esoraider_server.data.classes.arcanist.debuffs import ArcanistDebuffs
from esoraider_server.data.core import EsoEnum, Skill


class ArcanistSkills(EsoEnum):
    CEPHALIARCHS_FLAIL  = Skill(
        name="Cephaliarch's Flail",
        id=183006,
        buffs=[ArcanistBuffs.CRUX.value],
        link='https://eso-hub.com/en/skills/arcanist/herald-of-the-tome/cephaliarchs-flail',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_arcanist_003_a.png',
    )
    FULMINATING_RUNE_DAMAGE = Skill(
        name='Fulminating Rune',
        id=182989,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_arcanist_004_b.png',
    )
    FULMINATING_RUNE = Skill(
        name='Fulminating Rune',
        id=182988,
        children=[FULMINATING_RUNE_DAMAGE],
        debuffs=[
            ArcanistDebuffs.FULMINATING_RUNE_DAMAGE.value,
            ArcanistDebuffs.FULMINATING_RUNE_LINGER.value,
        ],
        link='https://eso-hub.com/en/skills/arcanist/herald-of-the-tome/fulminating-rune',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_arcanist_004_b.png',
    )
    INSPIRED_SCHOLARSHIP_DAMAGE = Skill(
        name='Inspired Scholarship',
        id=185843,
        tick=3,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_arcanist_005_a.png',
    )
    INSPIRED_SCHOLARSHIP = Skill(
        name='Inspired Scholarship',
        id=185842,
        tick=3,
        children=[INSPIRED_SCHOLARSHIP_DAMAGE],
        buffs=[
            ArcanistBuffs.INSPIRED_SCHOLARSHIP.value,
            ArcanistBuffs.CRUX.value,
            Buffs.MAJOR_BRUTALITY.value,
            Buffs.MAJOR_SORCERY.value,
        ],
        link='https://eso-hub.com/en/skills/arcanist/herald-of-the-tome/inspired-scholarship',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_arcanist_005_a.png',
    )
