from data.core import Debuff, EsoEnum


class WARDEN_DEBUFFS(EsoEnum):
    FETCHER_INFECTION = Debuff(
        name='Fetcher Infection',
        id=101904,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_014_a.png',
    )
    GROWING_SWARM = Debuff(
        name='Growing Swarm',
        id=101944,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_014_b.png',
    )
