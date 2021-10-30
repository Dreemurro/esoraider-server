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
