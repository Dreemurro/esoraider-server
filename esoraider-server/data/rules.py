from data.core import Rule, EsoEnum
from data.races import RacialPassives


class Rules(EsoEnum):
    # |-----------------------------------------------------------------------|
    # | Racial passives check                                                 |
    # |-----------------------------------------------------------------------|
    BRETON = Rule(
        name='Breton passives',
        icon='https://images.uesp.net/9/94/ON-icon-Breton.png',
        buffs=[
            RacialPassives.MAGICKA_MASTERY.value,
            RacialPassives.SPELL_ATTUNEMENT.value,
        ],
    )
    DARK_ELF = Rule(
        name='Dark elf passives',
        icon='https://images.uesp.net/8/86/ON-icon-Dunmer.png',
        buffs=[
            RacialPassives.DYNAMIC.value,
            RacialPassives.RESIST_FLAME.value,
            RacialPassives.RUINATION.value,
        ],
    )
    HIGH_ELF = Rule(
        name='High elf passives',
        icon='https://images.uesp.net/5/5e/ON-icon-Altmer.png',
        buffs=[
            RacialPassives.SPELL_RECHARGE.value,
            RacialPassives.ELEMENTAL_TALENT.value,
        ],
    )
    IMPERIAL = Rule(
        name='Imperial passives',
        icon='https://images.uesp.net/4/4d/ON-concept-Imperial_symbol.png',
        buffs=[
            RacialPassives.TOUGH.value,
            RacialPassives.IMPERIAL_METTLE.value,
            RacialPassives.RED_DIAMOND.value,
        ],
    )
    KHAJIIT = Rule(
        name='Khajiit passives',
        icon='https://images.uesp.net/d/d1/ON-icon-Khajiit.png',
        buffs=[
            RacialPassives.ROBUSTNESS.value,
            RacialPassives.LUNAR_BLESSINGS.value,
            RacialPassives.FELINE_AMBUSH.value,
        ],
    )
    NORD = Rule(
        name='Nord passives',
        icon='https://images.uesp.net/5/5f/ON-icon-Nord.png',
        buffs=[
            RacialPassives.RESIST_FROST.value,
            RacialPassives.STALWART.value,
            RacialPassives.RUGGED.value,
        ],
    )
    ORC = Rule(
        name='Orc passives',
        icon='https://images.uesp.net/6/64/ON-icon-Orc.png',
        buffs=[
            RacialPassives.BRAWNY.value,
            RacialPassives.UNFLINCHING_RAGE.value,
        ],
    )
