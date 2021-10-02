from data.classes.templar.debuffs import TEMPLAR_DEBUFFS
from data.core import EsoEnum, Skill
from data.buffs import BUFFS
from data.debuffs import DEBUFFS


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
    POWER_OF_THE_LIGHT = Skill(
        name='Power of the Light',
        id=21763,
        # Include PoTL debuff with the same ID?
        debuffs=[DEBUFFS.MINOR_BREACH_POWER_OF_THE_LIGHT.value],
        link='https://eso-hub.com/en/skills/templar/dawns-wrath/power-of-the-light',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_power_of_the_light.png',
    )
    PURIFYING_LIGHT = Skill(
        name='Purifying Light',
        id=21765,
        debuffs=[TEMPLAR_DEBUFFS.PURIFYING_LIGHT.value],
        link='https://eso-hub.com/en/skills/templar/dawns-wrath/purifying-light',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_purifying_light.png',
    )
    BLAZING_SPEAR_INITIAL_DAMAGE = Skill(
        name='Blazing Spear',
        id=26871,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templarsun_thrust.png',
    )
    BLAZING_SPEAR_DAMAGE = Skill(
        name='Blazing Spear',
        id=26879,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templarsun_thrust.png',
    )
    BLAZING_SPEAR = Skill(
        name='Blazing Spear',
        id=26869,
        children=[BLAZING_SPEAR_INITIAL_DAMAGE, BLAZING_SPEAR_DAMAGE],
        link='https://eso-hub.com/en/skills/templar/aedric-spear/blazing-spear',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templarsun_thrust.png',
    )
    CHANNELED_FOCUS = Skill(
        name='Channeled Focus',
        id=22240,
        buffs=[BUFFS.MAJOR_RESOLVE_CHANNELED_FOCUS.value],
        link='https://eso-hub.com/en/skills/templar/restoring-light/channeled-focus',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_channeled_focus.png',
    )
