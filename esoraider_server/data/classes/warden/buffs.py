from esoraider_server.data.core import Buff, EsoEnum


class WARDEN_BUFFS(EsoEnum):
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
