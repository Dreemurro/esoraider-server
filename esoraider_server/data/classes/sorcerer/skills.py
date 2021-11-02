from data.classes.sorcerer.debuffs import SORCERER_DEBUFFS
from data.core import EsoEnum, Skill


class SORCERER_SKILLS(EsoEnum):
    DAEDRIC_PREY = Skill(
        name='Daedric Prey',
        id=24328,
        debuffs=[SORCERER_DEBUFFS.DAEDRIC_PREY.value],
        link='https://eso-hub.com/en/skills/sorcerer/daedric-summoning/daedric-prey',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_explosive_curse.png',
    )
