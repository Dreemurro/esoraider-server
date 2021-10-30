from data.core import Buff, EsoEnum


class RacialPassives(EsoEnum):
    # Breton (excluding Opportunist & Gift of Magnus)
    MAGICKA_MASTERY = Buff(
        name='Magicka Mastery',
        id=45264,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_005.png',
        link='https://eso-hub.com/en/skills/racial/breton-skills/magicka-mastery',
    )
    SPELL_ATTUNEMENT = Buff(
        name='Spell Attunement',
        id=45262,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_013.png',
        link='https://eso-hub.com/en/skills/racial/breton-skills/spell-attunement',
    )

    # Dark Elf (excluding Ashlander)
    DYNAMIC = Buff(
        name='Dynamic',
        id=45267,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_weapon_023.png',
        link='https://eso-hub.com/en/skills/racial/dark-elf-skills/dynamic',
    )
    RESIST_FLAME = Buff(
        name='Resist Flame',
        id=45270,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_062.png',
        link='https://eso-hub.com/en/skills/racial/dark-elf-skills/resist-flame',
    )
    RUINATION = Buff(
        name='Ruination',
        id=45272,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_010.png',
        link='https://eso-hub.com/en/skills/racial/dark-elf-skills/ruination',
    )

    # High Elf (excluding Highborn)
    SPELL_RECHARGE = Buff(
        name='Spell Recharge',
        id=45274,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_063.png',
        link='https://eso-hub.com/en/skills/racial/high-elf-skills/spell-recharge',
    )
    SYRABANES_BOON = Buff(  # Potentially bugged - only tracked on log's owner
        name="Syrabane's Boon",
        id=117970,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_004.png',
        link='https://eso-hub.com/en/skills/racial/high-elf-skills/elemental-talent',
    )
    ELEMENTAL_TALENT = Buff(
        name='Elemental Talent',
        id=45276,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_005.png',
        link='https://eso-hub.com/en/skills/racial/high-elf-skills/elemental-talent',
    )

    # Imperial (excluding Diplomat)
    TOUGH = Buff(
        name='Tough',
        id=50907,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_020.png',
        link='https://eso-hub.com/en/skills/racial/imperial-skills/tough',
    )
    IMPERIAL_METTLE = Buff(
        name='Imperial Mettle',
        id=45280,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_021.png',
        link='https://eso-hub.com/en/skills/racial/imperial-skills/imperial-mettle',
    )
    RED_DIAMOND = Buff(
        name='Red Diamond',
        id=45293,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_028.png',
        link='https://eso-hub.com/en/skills/racial/imperial-skills/red-diamond',
    )
