from esoraider_server.data.core import Debuff, EsoEnum


class ArcanistDebuffs(EsoEnum):
    FULMINATING_RUNE_DAMAGE = Debuff(
        name='Fulminating Rune',
        id=182989, # matches skill ID
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_arcanist_004_b.png',
    )
    FULMINATING_RUNE_LINGER = Debuff(
        name='Fulminating Rune',
        id=184258,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_arcanist_004_b.png',
    )
