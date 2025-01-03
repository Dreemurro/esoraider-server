from esoraider_server.data.core import Buff, EsoEnum


class WardenBuffs(EsoEnum):
    BLUE_BETTY = Buff(
        name='Blue Betty',
        id=86054,  # Matches skill ID
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_017.png',
    )
    BULL_NETCH = Buff(
        name='Bull Netch',
        id=86058,  # Matches skill ID
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_017_b.png',
    )
    LOTUS_BLOSSOM = Buff(
        name='Lotus Blossom',
        id=85855,  # Matches skill ID
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_009_b.png',
    )
