from esoraider_server.data.core import Debuff, EsoEnum


class DragonknightDebuffs(EsoEnum):
    ENGULFING_FLAMES_DAMAGE = Debuff(
        name='Engulfing Flames',
        id=31104,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_004_b.png',
    )
    NOXIOUS_BREATH = Debuff(
        name='Noxious Breath',
        id=31103,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_004_a.png',
    )
    BURNING_EMBERS = Debuff(
        name='Burning Embers',
        id=44373,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_003_b.png',
    )
    VENOMOUS_CLAW = Debuff(
        name='Venomous Claw',
        id=44369,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_003_a.png',
    )
    BURNING_TALONS = Debuff(
        name='Burning Talons',
        id=31898,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_010_b.png',
    )
