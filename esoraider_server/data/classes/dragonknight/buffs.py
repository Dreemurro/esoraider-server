from esoraider_server.data.core import Buff, EsoEnum


class DRAGONKNIGHT_BUFFS(EsoEnum):
    HARDENED_ARMOR = Buff(
        name='Hardened Armor',
        id=20328,  # Matches skill ID
        link='https://eso-hub.com/en/skills/dragonknight/draconic-power/hardened-armor',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_007_b.png',
    )
