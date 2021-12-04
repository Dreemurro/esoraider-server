from esoraider_server.data.core import Buff, EsoEnum


class Passives(EsoEnum):
    # |-----------------------------------------------------------------------|
    # | Armor                                                                 |
    # |-----------------------------------------------------------------------|
    # |-------------|
    # | Light Armor |
    # |-------------|
    CONCENTRATION = Buff(
        name='Concentration',
        id=45562,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_060.png',
        link='https://eso-hub.com/en/skills/armor/light-armor/concentration',
    )
    GRACE = Buff(
        name='Grace',
        id=45549,  # Another ID - 45548 (yes, one digit diff)
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_004.png',
        link='https://eso-hub.com/en/skills/armor/light-armor/grace',
    )
    EVOCATION = Buff(
        name='Evocation',
        id=45557,  # Another ID - 29665
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_005.png',
        link='https://eso-hub.com/en/skills/armor/light-armor/evocation',
    )
    SPELL_WARDING = Buff(  # Potentially bugged - only tracked on log's owner
        name='Spell Warding',
        id=45559,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_006.png',
        link='https://eso-hub.com/en/skills/armor/light-armor/spell-warding',
    )
    PRODIGY = Buff(  # Potentially bugged - only tracked on log's owner
        name='Prodigy',
        id=45561,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_038.png',
        link='https://eso-hub.com/en/skills/armor/light-armor/prodigy',
    )
    # |--------------|
    # | Medium Armor | (excluding Improved Sneak)
    # |--------------|
    DEXTERITY = Buff(  # Potentially bugged - only tracked on log's owner
        name='Dexterity',
        id=45564,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_008.png',
        link='https://eso-hub.com/en/skills/armor/medium-armor/dexterity',
    )
    WIND_WALKER = Buff(
        name='Wind Walker',
        id=45565,  # Another ID - 29687
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_011.png',
        link='https://eso-hub.com/en/skills/armor/medium-armor/wind-walker',
    )
    AGILITY = Buff(  # Potentially bugged - only tracked on log's owner
        name='Agility',
        id=45572,  # Another ID - 29686
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_010.png',
        link='https://eso-hub.com/en/skills/armor/medium-armor/agility',
    )
    # |-------------|
    # | Heavy Armor | (COMPLETELY BUGGED AS OF NOW)
    # |-------------|
    RESOLVE = Buff(  # Potentially bugged - only tracked on log's owner
        name='Resolve',
        id=45533,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_020.png',
        link='https://eso-hub.com/en/skills/armor/heavy-armor/resolve',
    )
    CONSTITUTION = Buff(  # Potentially bugged - only tracked on log's owner
        name='Constitution',
        id=45526,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_014.png',
        link='https://eso-hub.com/en/skills/armor/heavy-armor/constitution',
    )
    JUGGERNAUT = Buff(  # Potentially bugged - only tracked on log's owner
        name='Juggernaut',
        id=45546,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_012.png',
        link='https://eso-hub.com/en/skills/armor/heavy-armor/juggernaut',
    )
    REVITALIZE = Buff(  # Potentially bugged - only tracked on log's owner
        name='Revitalize',
        id=45528,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_013.png',
        link='https://eso-hub.com/en/skills/armor/heavy-armor/revitalize',
    )
    RAPID_MENDING = Buff(  # Potentially bugged - only tracked on log's owner
        name='Rapid Mending',
        id=45529,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_015.png',
        link='https://eso-hub.com/en/skills/armor/heavy-armor/rapid-mending',
    )

    # |-----------------------------------------------------------------------|
    # | Weapon                                                                |
    # |-----------------------------------------------------------------------|
    # |-----|
    # | Bow |
    # |-----|
    HAWK_EYE = Buff(
        name='Hawk Eye',
        id=45497,  # Additional IDs - 78855, 30936
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_armor_002.png',
        link='https://eso-hub.com/en/skills/weapon/bow/hawk-eye',
    )
    # |-------------------|
    # | Destruction Staff |
    # |-------------------|
    TRI_FOCUS = Buff(
        name='Tri Focus',
        id=45500,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_weapon_001.png',
        link='https://eso-hub.com/en/skills/weapon/destruction-staff/tri-focus',
    )
    PENETRATING_MAGIC = Buff(
        name='Penetrating Magic',
        id=45509,  # Additional IDs - 69773, 30948
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_weapon_008.png',
        link='https://eso-hub.com/en/skills/weapon/destruction-staff/penetrating-magic',
    )
    ANCIENT_KNOWLEDGE = Buff(
        name='Ancient Knowledge',
        id=45513,  # Another ID - 30959
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_weapon_003.png',
        link='https://eso-hub.com/en/skills/weapon/destruction-staff/ancient-knowledge',
    )
    DESTRUCTION_EXPERT = Buff(
        name='Destruction Expert',
        id=45514,  # Another ID - 30965
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_weapon_006.png',
        link='https://eso-hub.com/en/skills/weapon/destruction-staff/destruction-expert',
    )
    # |------------|
    # | Dual Wield | (COMPLETELY BUGGED AS OF NOW)
    # |------------|
    DUAL_WIELD_EXPERT = Buff(  # Potentially bugged - only tracked on log's owner
        name='Dual Wield Expert',
        id=45477,  # Additional ID - 30873
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_weapon_013.png',
        link='https://eso-hub.com/en/skills/weapon/dual-wield/dual-wield-expert',
    )
    CONTROLLED_FURY = Buff(  # Potentially bugged - only tracked on log's owner
        name='Controlled Fury',
        id=45478,  # Additional ID - 30872
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_weapon_018.png',
        link='https://eso-hub.com/en/skills/weapon/dual-wield/controlled-fury',
    )
    TWIN_BLADE_AND_BLUNT = Buff(  # Potentially bugged - only tracked on log's owner
        name='Twin Blade and Blunt',
        id=45482,  # Additional ID - 30893
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_weapon_016.png',
        link='https://eso-hub.com/en/skills/weapon/dual-wield/twin-blade-and-blunt',
    )
    # |------------|
    # | Two Handed |
    # |------------|
    FORCEFUL = Buff(
        name='Forceful',
        id=45444,  # Additional ID - 29387
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_weapon_027.png',
        link='https://eso-hub.com/en/skills/weapon/two-handed/forceful',
    )
    FOLLOW_UP = Buff(
        name='Follow Up',
        id=45446,  # Additional ID - 29389
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_dragonknight_016.png',
        link='https://eso-hub.com/en/skills/weapon/two-handed/follow-up',
    )

    # |-----------------------------------------------------------------------|
    # | Guild                                                                 |
    # |-----------------------------------------------------------------------|
    # |----------------|
    # | Fighters Guild |
    # |----------------|
    SLAYER = Buff(
        name='Slayer',
        id=45596,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_025.png',
        link='https://eso-hub.com/en/skills/guild/fighters-guild/slayer',
    )
    SKILLED_TRACKER = Buff(  # Potentially bugged - only tracked on log's owner
        name='Skilled Tracker',
        id=40393,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_007.png',
        link='https://eso-hub.com/en/skills/guild/fighters-guild/skilled-tracker',
    )
    # |-------------|
    # | Mages Guild |
    # |-------------|
    MAGICKA_CONTROLLER = Buff(
        name='Magicka Controller',
        id=45603,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_044.png',
        link='https://eso-hub.com/en/skills/guild/mages-guild/magicka-controller',
    )
    MIGHT_OF_THE_GUILD = Buff(
        name='Might of the Guild',
        id=45607,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_038.png',
        link='https://eso-hub.com/en/skills/guild/mages-guild/might-of-the-guild',
    )
    # |--------------|
    # | Psijic Order |
    # |--------------|
    CLAIRVOYANCE = Buff(
        name='Clairvoyance',
        id=103811,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_psijic_008.png',
        link='https://eso-hub.com/en/skills/guild/psijic-order/clairvoyance',
    )
    SPELL_ORB = Buff(
        name='Spell Orb',
        id=103879,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_psijic_009.png',
        link='https://eso-hub.com/en/skills/guild/psijic-order/spell-orb',
    )
    CONCENTRATED_BARRIER = Buff(
        name='Concentrated Barrier',
        id=103964,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_psijic_010.png',
        link='https://eso-hub.com/en/skills/guild/psijic-order/concentrated-barrier',
    )
    DELIBERATION = Buff(
        name='Deliberation',
        id=103972,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_psijic_011.png',
        link='https://eso-hub.com/en/skills/guild/psijic-order/deliberation',
    )
    # |-----------|
    # | Undaunted |
    # |-----------|
    UNDAUNTED_COMMAND = Buff(
        name='Undaunted Command',
        id=55676,  # Another ID - 55584
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_templar_003.png',
        link='https://eso-hub.com/en/skills/guild/undaunted/undaunted-command',
    )
    UNDAUNTED_METTLE = Buff(
        name='Undaunted Mettle',
        id=55386,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_014.png',
        link='https://eso-hub.com/en/skills/guild/undaunted/undaunted-mettle',
    )
