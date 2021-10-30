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
