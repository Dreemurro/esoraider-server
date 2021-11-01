from data.core import Rule, EsoEnum
from data.races import RacialPassives
from data.passives import Passives
from data.classes.necromancer.passives import NECROMANCER_PASSIVES


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

    # |-----------------------------------------------------------------------|
    # | Armor passives check                                                  |
    # |-----------------------------------------------------------------------|
    LIGHT_ARMOR = Rule(
        name='Light armor passives',
        icon='https://eso-hub.com/storage/icons/ability_armor_003.webp',
        buffs=[
            Passives.CONCENTRATION.value,
            Passives.GRACE.value,
            Passives.EVOCATION.value,
            # Next 2 are bugged
            # Passives.SPELL_WARDING.value,
            # Passives.PRODIGY.value,
        ]
    )
    MEDIUM_ARMOR = Rule(
        name='Medium armor passives',
        icon='https://eso-hub.com/storage/icons/ability_armor_002.webp',
        buffs=[
            Passives.WIND_WALKER.value,
            # Next 2 are bugged
            # Passives.DEXTERITY.value,
            # Passives.AGILITY.value,
        ]
    )

    # |-----------------------------------------------------------------------|
    # | Weapon passives check                                                 |
    # |-----------------------------------------------------------------------|
    DESTRUCTION_STAFF = Rule(
        name='Destruction staff passives',
        icon='https://eso-hub.com/storage/icons/ability_destructionstaff_012.webp',
        buffs=[
            Passives.TRI_FOCUS.value,
            Passives.PENETRATING_MAGIC.value,
            Passives.ANCIENT_KNOWLEDGE.value,
            Passives.DESTRUCTION_EXPERT.value,
        ]
    )

    # |-----------------------------------------------------------------------|
    # | Class passives check                                                  |
    # |-----------------------------------------------------------------------|
    NECROMANCER = Rule(
        name='Necromancer passives',
        icon='https://eso-hub.com/storage/icons/class/gamepad/gp_class_necromancer.png',
        buffs=[
            NECROMANCER_PASSIVES.DEATH_GLEANING.value,
            NECROMANCER_PASSIVES.HEALTH_AVARICE.value,
            NECROMANCER_PASSIVES.LAST_GASP.value,
            # Reusasble Parts is not in combatant info, skipping for now
            # NECROMANCER_PASSIVES.REUSABLE_PARTS.value,
            NECROMANCER_PASSIVES.DISMEMBER.value,
            NECROMANCER_PASSIVES.RAPID_ROT.value,
            NECROMANCER_PASSIVES.CURATIVE_CURSE.value,
            NECROMANCER_PASSIVES.NEAR_DEATH_EXPERIENCE.value,
            NECROMANCER_PASSIVES.CORPSE_CONSUMPTION.value,
            NECROMANCER_PASSIVES.UNDEAD_CONFEDERATE.value,
        ]
    )
