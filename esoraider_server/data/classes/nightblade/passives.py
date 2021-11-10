from esoraider_server.data.core import Buff, EsoEnum


class NIGHTBLADE_PASSIVES(EsoEnum):
    # Assassination
    MASTER_ASSASSIN = Buff(
        name='Master Assassin',
        id=45038,
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_weapon_026.png',
        link='https://eso-hub.com/en/skills/nightblade/assassination/master-assassin',
    )
    EXECUTIONER = Buff(
        name='Executioner',
        id=45048,
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_weapon_018.png',
        link='https://eso-hub.com/en/skills/nightblade/assassination/executioner',
    )
    PRESSURE_POINTS = Buff(
        name='Pressure Points',
        id=45053,
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_weapon_015.png',
        link='https://eso-hub.com/en/skills/nightblade/assassination/pressure-points',
    )
    HEMORRHAGE = Buff(
        name='Hemorrhage',
        id=45060,
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_weapon_017.png',
        link='https://eso-hub.com/en/skills/nightblade/assassination/hemorrhage',
    )

    # Shadow
    REFRESHING_SHADOWS = Buff(
        name='Refreshing Shadows',
        id=45103,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_038.png',
        link='https://eso-hub.com/en/skills/nightblade/shadow/refreshing-shadows',
    )
    SHADOW_BARRIER = Buff(
        name='Shadow Barrier',
        id=45071,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_022.png',
        link='https://eso-hub.com/en/skills/nightblade/shadow/shadow-barrier',
    )
    DARK_VIGOR = Buff(
        name='Dark Vigor',
        id=45084,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_044.png',
        link='https://eso-hub.com/en/skills/nightblade/shadow/dark-vigor',
    )
    DARK_VEIL = Buff(
        name='Dark Veil',
        id=45115,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_036.png',
        link='https://eso-hub.com/en/skills/nightblade/shadow/dark-veil',
    )

    # Siphoning
    CATALYST = Buff(
        name='Catalyst',
        id=45135,
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_sorcerer_046.png',
        link='https://eso-hub.com/en/skills/nightblade/siphoning/catalyst',
    )
    SOUL_SIPHONER = Buff(
        name='Soul Siphoner',
        id=45155,
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_sorcerer_036.png',
        link='https://eso-hub.com/en/skills/nightblade/siphoning/soul-siphoner',
    )
