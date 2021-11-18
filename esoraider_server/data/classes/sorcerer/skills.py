from esoraider_server.data.buffs import BUFFS
from esoraider_server.data.classes.sorcerer.buffs import SORCERER_BUFFS
from esoraider_server.data.classes.sorcerer.debuffs import SORCERER_DEBUFFS
from esoraider_server.data.core import EsoEnum, Skill


class SORCERER_SKILLS(EsoEnum):
    DAEDRIC_PREY = Skill(
        name='Daedric Prey',
        id=24328,
        debuffs=[SORCERER_DEBUFFS.DAEDRIC_PREY.value],
        link='https://eso-hub.com/en/skills/sorcerer/daedric-summoning/daedric-prey',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_explosive_curse.png',
    )
    CRITICAL_SURGE = Skill(
        name='Critical Surge',
        id=23678,
        buffs=[
            SORCERER_BUFFS.CRITICAL_SURGE.value,
            BUFFS.MAJOR_BRUTALITY_CRITICAL_SURGE.value,
            BUFFS.MAJOR_SORCERY_CRITICAL_SURGE.value,
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
