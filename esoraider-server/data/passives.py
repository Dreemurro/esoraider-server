from data.core import Buff, EsoEnum


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

    # |-----------------------------------------------------------------------|
    # | Guild                                                                 |
    # |-----------------------------------------------------------------------|
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
