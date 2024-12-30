from esoraider_server.data.classes.nightblade.buffs import NightbladeBuffs
from esoraider_server.data.classes.nightblade.debuffs import NightbladeDebuffs
from esoraider_server.data.core import EsoEnum, Skill
from esoraider_server.data.stacks import BuffsWithStacks


class NightbladeSkills(EsoEnum):
    TWISTING_PATH_DAMAGE = Skill(
        name='Twisting Path',
        id=36052,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_010_b.png',
    )
    TWISTING_PATH = Skill(
        name='Twisting Path',
        id=36049,
        children=[TWISTING_PATH_DAMAGE],
        link='https://eso-hub.com/en/skills/nightblade/shadow/twisting-path',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_010_b.png',
    )
    MERCILESS_RESOLVE = Skill(
        name='Merciless Resolve',
        id=61919,
        buffs=[BuffsWithStacks.MERCILESS_RESOLVE.value],
        link='https://eso-hub.com/en/skills/nightblade/assassination/merciless-resolve',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_005_b.png',
    )
    RELENTLESS_FOCUS = Skill(
        name='Relentless Focus',
        id=61927,
        buffs=[BuffsWithStacks.RELENTLESS_FOCUS.value],
        link='https://eso-hub.com/en/skills/nightblade/assassination/relentless-focus',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_005_a.png',
    )
    SIPHONING_ATTACKS = Skill(
        name='Siphoning Attacks',
        id=36935,
        buffs=[NightbladeBuffs.SIPHONING_ATTACKS.value],
        link='https://eso-hub.com/en/skills/nightblade/siphoning/siphoning-attacks',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_003_b.png',
    )
    LEECHING_STRIKES = Skill(
        name='Leeching Strikes',
        id=36908,
        buffs=[NightbladeBuffs.LEECHING_STRIKES.value],
        link='https://eso-hub.com/en/skills/nightblade/siphoning/leeching-strikes',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_003_a.png',
    )
    DEBILITATE = Skill(
        name='Debilitate',
        id=36943,
        debuffs=[NightbladeDebuffs.DEBILITATE.value],
        link='https://eso-hub.com/en/skills/nightblade/siphoning/debilitate',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_006_a.png',
    )
    CRIPPLING_GRASP = Skill(
        name='Crippling Grasp',
        id=36957,  # + upfront damage with ID = 369663
        debuffs=[NightbladeDebuffs.CRIPPLING_GRASP.value],
        link='https://eso-hub.com/en/skills/nightblade/siphoning/crippling-grasp',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_006_b.png',
    )
    # DARK_SHADE = Skill()  # Pet handling is needed
