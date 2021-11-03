from esoraider_server.data.core import Debuff, EsoEnum


class SORCERER_DEBUFFS(EsoEnum):
    DAEDRIC_PREY = Debuff(
        name='Daedric Prey',
        id=24328,  # Debuff ID = Skill ID, don't ask ¯\_(ツ)_/¯
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_explosive_curse.png',
    )
