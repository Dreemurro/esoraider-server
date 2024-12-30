from esoraider_server.data.buffs import Buffs
from esoraider_server.data.classes.sorcerer.buffs import SorcererBuffs
from esoraider_server.data.classes.sorcerer.debuffs import SorcererDebuffs
from esoraider_server.data.core import EsoEnum, Skill


class SorcererSkills(EsoEnum):
    DAEDRIC_PREY = Skill(
        name='Daedric Prey',
        id=24328,
        debuffs=[SorcererDebuffs.DAEDRIC_PREY.value],
        link='https://eso-hub.com/en/skills/sorcerer/daedric-summoning/daedric-prey',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_explosive_curse.png',
    )
    POWER_SURGE = Skill(
        name='Power Surge',
        id=23674,
        buffs=[
            SorcererBuffs.POWER_SURGE.value,
            Buffs.MAJOR_BRUTALITY_POWER_SURGE.value,
            Buffs.MAJOR_SORCERY_POWER_SURGE.value,
        ],
        link='https://eso-hub.com/en/skills/sorcerer/storm-calling/power-surge',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_power_surge.png',
    )
    CRITICAL_SURGE = Skill(
        name='Critical Surge',
        id=23678,
        buffs=[
            SorcererBuffs.CRITICAL_SURGE.value,
            Buffs.MAJOR_BRUTALITY_CRITICAL_SURGE.value,
            Buffs.MAJOR_SORCERY_CRITICAL_SURGE.value,
        ],
        link='https://eso-hub.com/en/skills/sorcerer/storm-calling/critical-surge',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_critical_surge.png',
    )
    LIGHTNING_FLOOD_DAMAGE = Skill(
        name='Lightning Flood',
        id=23208,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_lightning_flood.png',
    )
    LIGHTNING_FLOOD = Skill(
        name='Lightning Flood',
        id=23205,
        children=[LIGHTNING_FLOOD_DAMAGE],
        link='https://eso-hub.com/en/skills/sorcerer/storm-calling/lightning-flood',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_lightning_flood.png',
    )
    BOUNDLESS_STORM_DAMAGE = Skill(
        name='Boundless Storm',
        id=23214,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_boundless_storm.png',
    )
    BOUNDLESS_STORM = Skill(
        name='Boundless Storm',
        id=23213,
        children=[BOUNDLESS_STORM_DAMAGE],
        buffs=[
            SorcererBuffs.BOUNDLESS_STORM.value,
            Buffs.MAJOR_RESOLVE_BOUNDLESS_STORM.value,
        ],
        link='https://eso-hub.com/en/skills/sorcerer/storm-calling/boundless-storm',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_boundless_storm.png',
    )
    HURRICANE_DAMAGE = Skill(
        name='Hurricane',
        id=23232,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_thundering_presence.png',
    )
    HURRICANE = Skill(
        name='Hurricane',
        id=23231,
        children=[HURRICANE_DAMAGE],
        buffs=[
            SorcererBuffs.HURRICANE.value,
            Buffs.MAJOR_RESOLVE_HURRICANE.value,
            Buffs.MINOR_EXPEDITION_HURRICANE.value,
        ],
        link='https://eso-hub.com/en/skills/sorcerer/storm-calling/hurricane',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_thundering_presence.png',
    )
    EMPOWERED_WARD = Skill(
        name='Empowered Ward',
        id=29482,
        buffs=[
            SorcererBuffs.EMPOWERED_WARD.value,
            Buffs.MINOR_INTELLECT_EMPOWERED_WARD.value,
        ],
        link='https://eso-hub.com/en/skills/sorcerer/daedric-summoning/empowered-ward',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_tempest.png',
    )
