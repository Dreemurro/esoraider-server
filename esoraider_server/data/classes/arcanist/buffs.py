from esoraider_server.data.core import Buff, EsoEnum


class ArcanistBuffs(EsoEnum):
    # TODO: add stacks [3] and move to stacks.py
    CRUX = Buff(
        name='Crux',
        id=184220,
        icon='https://assets.rpglogs.com/img/eso/abilities/class_buff_arcanist_crux.png',
    )
    INSPIRED_SCHOLARSHIP = Buff(
        name='Inspired Scholarship',
        id=185842,  # matches skill ID
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_arcanist_005_a.png',
    )
