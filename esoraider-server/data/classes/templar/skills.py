from data.classes.templar.debuffs import TEMPLAR_DEBUFFS
from data.core import EsoEnum, Skill


class TEMPLAR_SKILLS(EsoEnum):
    VAMPIRES_BANE = Skill(
        # 21729 - skill and initial damage (debuff), 21731 - DoT (also debuff)
        # Mark them as children or move to debuffs?
        name='Vampire\'s Bane',
        id=21729,
        debuffs=[TEMPLAR_DEBUFFS.VAMPIRES_BANE.value],
        link='https://eso-hub.com/en/skills/templar/dawns-wrath/vampires-bane',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_vampire_bane.png',
    )
