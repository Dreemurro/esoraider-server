from esoraider_server.data.core import Buff, EsoEnum


class SORCERER_BUFFS(EsoEnum):
    CRITICAL_SURGE = Buff(
        name='Critical Surge',
        id=23678,  # Matches skill ID
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_critical_surge.png',
    )
    HURRICANE = Buff(
        name='Hurricane',
        id=23231,  # Matches skill ID
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_thundering_presence.png',
    )
