from esoraider_server.data.core import Buff, EsoEnum


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

    # Khajiit (excluding Cutpurse)
    ROBUSTNESS = Buff(
        name='Robustness',
        id=70390,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_018.png',
        link='https://eso-hub.com/en/skills/racial/khajiit-skills/robustness',
    )
    LUNAR_BLESSINGS = Buff(
        name='Lunar Blessings',
        id=117848,
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_khajiit_01.png',
        link='https://eso-hub.com/en/skills/racial/khajiit-skills/lunar-blessings',
    )
    FELINE_AMBUSH = Buff(
        name='Feline Ambush',
        id=45301,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_006.png',
        link='https://eso-hub.com/en/skills/racial/khajiit-skills/feline-ambush',
    )

    # Nord (excluding Reveler)
    RESIST_FROST = Buff(
        name='Resist Frost',
        id=45304,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_012.png',
        link='https://eso-hub.com/en/skills/racial/nord-skills/resist-frost',
    )
    STALWART = Buff(
        name='Stalwart',
        id=45298,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_018.png',
        link='https://eso-hub.com/en/skills/racial/nord-skills/stalwart',
    )
    RUGGED = Buff(
        name='Rugged',
        id=45306,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_020.png',
        link='https://eso-hub.com/en/skills/racial/nord-skills/rugged',
    )

    # Orc (excluding Craftsman)
    BRAWNY = Buff(
        name='Brawny',
        id=45309,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dragonknight_020.png',
        link='https://eso-hub.com/en/skills/racial/orc-skills/brawny',
    )
    UNFLINCHING_RAGE = Buff(
        name='Unflinching Rage',
        id=84672,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_018.png',
        link='https://eso-hub.com/en/skills/racial/orc-skills/unflinching-rage',
    )
