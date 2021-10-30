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
