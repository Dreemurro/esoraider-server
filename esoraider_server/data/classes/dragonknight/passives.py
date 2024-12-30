from esoraider_server.data.core import Buff, EsoEnum


class DragonknightPassives(EsoEnum):
    # Ardent Flame
    COMBUSTION = Buff(
        name='Combustion',
        id=45011,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_011.png',
        link='https://eso-hub.com/en/skills/dragonknight/ardent-flame/combustion',
    )
    WARMTH = Buff(
        name='Warmth',
        id=45012,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_023.png',
        link='https://eso-hub.com/en/skills/dragonknight/ardent-flame/warmth',
    )
    SEARING_HEAT = Buff(  # Potentially bugged - only tracked on log's owner
        name='Searing Heat',
        id=45023,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_028.png',
        link='https://eso-hub.com/en/skills/dragonknight/ardent-flame/searing-heat',
    )
    WORLD_IN_RUIN = Buff(  # Potentially bugged - only tracked on log's owner
        name='World in Ruin',
        id=45029,
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_necromancer_005.png',
        link='https://eso-hub.com/en/skills/dragonknight/ardent-flame/world-in-ruin',
    )

    # Draconic Power
    IRON_SKIN = Buff(
        name='Iron Skin',
        id=44922,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_021.png',
        link='https://eso-hub.com/en/skills/dragonknight/draconic-power/iron-skin',
    )
    ELDER_DRAGON = Buff(
        name='Elder Dragon',
        id=44951,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_025.png',
        link='https://eso-hub.com/en/skills/dragonknight/draconic-power/elder-dragon',
    )
    SCALED_ARMOR = Buff(  # Potentially bugged - only tracked on log's owner
        name='Scaled Armor',
        id=44953,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_020.png',
        link='https://eso-hub.com/en/skills/dragonknight/draconic-power/scaled-armor',
    )

    # Earthen Heart
    ETERNAL_MOUNTAIN = Buff(
        name='Eternal Mountain',
        id=44996,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_023.png',
        link='https://eso-hub.com/en/skills/dragonknight/earthen-heart/eternal-mountain',
    )
    BATTLE_ROAR = Buff(
        name='Battle Roar',
        id=44984,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_031.png',
        link='https://eso-hub.com/en/skills/dragonknight/earthen-heart/battle-roar',
    )
