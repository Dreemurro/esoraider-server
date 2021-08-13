from data.core import EsoEnum, Skill
from data.classes.nightblade.buffs import NIGHTBLADE_BUFFS


class NIGHTBLADE_SKILLS(EsoEnum):
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
        buffs=[NIGHTBLADE_BUFFS.MERCILESS_RESOLVE.value],
        link='https://eso-hub.com/en/skills/nightblade/assassination/merciless-resolve',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_005_b.png',
    )
    SIPHONING_ATTACKS = Skill(
        name='Siphoning Attacks',
        id=36935,
        buffs=[NIGHTBLADE_BUFFS.SIPHONING_ATTACKS.value],
        link='https://eso-hub.com/en/skills/nightblade/siphoning/siphoning-attacks',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_003_b.png',
    )
    # DARK_SHADE = Skill()  # Pet handling is needed
