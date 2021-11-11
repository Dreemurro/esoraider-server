from esoraider_server.data.core import Buff, EsoEnum


class TEMPLAR_PASSIVES(EsoEnum):
    # Aedric Spear
    PIERCING_SPEAR = Buff(
        name='Piercing Spear',
        id=44046,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_022.png',
        link='https://eso-hub.com/en/skills/templar/aedric-spear/piercing-spear',
    )
    SPEAR_WALL = Buff(
        name='Spear Wall',
        id=44721,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_027.png',
        link='https://eso-hub.com/en/skills/templar/aedric-spear/spear-wall',
    )
    BURNING_LIGHT = Buff(
        name='Burning Light',
        id=44730,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_028.png',
        link='https://eso-hub.com/en/skills/templar/aedric-spear/burning-light',
    )

    # Dawn's Wrath
    ILLUMINATE = Buff(
        name='Illuminate',
        id=45215,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_012.png',
        link='https://eso-hub.com/en/skills/templar/dawns-wrath/illuminate',
    )
    RESTORING_SPIRIT = Buff(
        name='Restoring Spirit',
        id=45212,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_014.png',
        link='https://eso-hub.com/en/skills/templar/dawns-wrath/restoring-spirit',
    )

    # Restoring Light
    SACRED_GROUND = Buff(  # Has multiple IDs - 77082, 31759
        name='Sacred Ground',
        id=45207,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_014.png',
        link='https://eso-hub.com/en/skills/templar/restoring-light/sacred-ground',
    )
    LIGHT_WEAVER = Buff(
        name='Light Weaver',
        id=45208,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_012.png',
        link='https://eso-hub.com/en/skills/templar/restoring-light/light-weaver',
    )
    MASTER_RITUALIST = Buff(
        name='Master Ritualist',
        id=45202,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_026.png',
        link='https://eso-hub.com/en/skills/templar/restoring-light/master-ritualist',
    )
