from esoraider_server.data.core import Buff, EsoEnum


class NecromancerBuffs(EsoEnum):
    SKELETAL_ARCHER = Buff(
        name='Skeletal Archer',
        id=118680,  # ID matches skill, it's a pet
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_necromancer_003_a.png',
    )
    SKELETAL_ARCANIST = Buff(
        name='Skeletal Arcanist',
        id=118726,  # ID matches skill, it's a pet
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_necromancer_003_b.png',
    )
