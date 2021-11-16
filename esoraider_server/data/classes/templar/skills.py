from esoraider_server.data.buffs import BUFFS
from esoraider_server.data.classes.templar.buffs import TEMPLAR_BUFFS
from esoraider_server.data.classes.templar.debuffs import TEMPLAR_DEBUFFS
from esoraider_server.data.core import EsoEnum, Skill
from esoraider_server.data.debuffs import DEBUFFS


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
    RESTORING_FOCUS = Skill(
        name='Restoring Focus',
        id=22237,
        buffs=[BUFFS.MAJOR_RESOLVE_RESTORING_FOCUS.value],
        link='https://eso-hub.com/en/skills/templar/restoring-light/restoring-focus',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_uninterrupted_focus.png',
    )
    CHANNELED_FOCUS = Skill(
        name='Channeled Focus',
        id=22240,
        buffs=[BUFFS.MAJOR_RESOLVE_CHANNELED_FOCUS.value],
        link='https://eso-hub.com/en/skills/templar/restoring-light/channeled-focus',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_channeled_focus.png',
    )
    SOLAR_BARRAGE_DAMAGE = Skill(
        name='Solar Barrage',
        id=100218,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_solar_power.png',
    )
    SOLAR_BARRAGE = Skill(
        name='Solar Barrage',
        id=22095,
        tick=2,
        children=[SOLAR_BARRAGE_DAMAGE],
        buffs=[
            TEMPLAR_BUFFS.SOLAR_BARRAGE.value,
            BUFFS.EMPOWER_SOLAR_BARRAGE.value,
        ],
        link='https://eso-hub.com/en/skills/templar/dawns-wrath/solar-barrage',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_solar_power.png',
    )
    RITUAL_OF_RETRIBUTION_DAMAGE = Skill(
        name='Ritual of Retribution',
        id=80172,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_cleansing_ritual.png',
    )
    RITUAL_OF_RETRIBUTION = Skill(
        name='Ritual of Retribution',
        id=22259,
        tick=2,
        children=[RITUAL_OF_RETRIBUTION_DAMAGE],
        link='https://eso-hub.com/en/skills/templar/restoring-light/ritual-of-retribution',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_purifying_ritual.png',
    )
