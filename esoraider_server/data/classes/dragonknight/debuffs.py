from esoraider_server.data.core import Debuff, EsoEnum


class DRAGONKNIGHT_DEBUFFS(EsoEnum):
    ENGULFING_FLAMES_DAMAGE = Debuff(
        name='Engulfing Flames',
        id=31104,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_004_b.png',
    )
    BURNING_EMBERS = Debuff(
        name='Burning Embers',
        id=44373,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_003_b.png',
    )
