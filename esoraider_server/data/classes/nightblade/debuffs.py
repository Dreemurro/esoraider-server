from esoraider_server.data.core import Debuff, EsoEnum


class NightbladeDebuffs(EsoEnum):
    DEBILITATE = Debuff(
        name='Debilitate',
        id=36947,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_006_a.png',
    )
    CRIPPLING_GRASP = Debuff(
        name='Crippling Grasp',
        id=36960,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_nightblade_006_b.png',
    )
