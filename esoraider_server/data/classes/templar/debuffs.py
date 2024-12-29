from esoraider_server.data.core import Debuff, EsoEnum


class TEMPLAR_DEBUFFS(EsoEnum):
    VAMPIRES_BANE = Debuff(
        name="Vampire's Bane",
        id=21731,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_vampire_bane.png',
    )
    REFLECTIVE_LIGHT = Debuff(
        name='Reflective Light',
        id=21734,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_reflective_light.png',
    )
    PURIFYING_LIGHT = Debuff(
        name='Purifying Light',
        id=21765,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_purifying_light.png',
    )
