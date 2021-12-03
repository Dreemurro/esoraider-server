from esoraider_server.data.classes.dragonknight.passives import (
    DRAGONKNIGHT_PASSIVES,
)
from esoraider_server.data.classes.general import GENERAL_SKILLS
from esoraider_server.data.classes.necromancer.passives import (
    NECROMANCER_PASSIVES,
)
from esoraider_server.data.classes.nightblade.passives import (
    NIGHTBLADE_PASSIVES,
)
from esoraider_server.data.classes.sorcerer.passives import SORCERER_PASSIVES
from esoraider_server.data.classes.templar.passives import TEMPLAR_PASSIVES
from esoraider_server.data.classes.warden.passives import WARDEN_PASSIVES
from esoraider_server.data.core import EsoEnum, Rule
from esoraider_server.data.passives import Passives
from esoraider_server.data.races import RacialPassives


class Rules(EsoEnum):
    # |-----------------------------------------------------------------------|
    # | Racial passives check                                                 |
    # |-----------------------------------------------------------------------|
    ARGONIAN = Rule(
        name='Argonian passives',
        icon='https://images.uesp.net/f/f9/ON-icon-Argonian.png',
        buffs=[
            RacialPassives.LIFE_MENDER.value,
            RacialPassives.ARGONIAN_RESISTANCE.value,
            RacialPassives.RESOURCEFUL.value,
        ],
    )
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
    REDGUARD = Rule(
        name='Redguard passives',
        icon='https://images.uesp.net/9/9d/ON-icon-Redguard.png',
        buffs=[
            RacialPassives.MARTIAL_TRAINING.value,
            RacialPassives.CONDITIONING.value,
            RacialPassives.ADRENALINE_RUSH.value,
        ],
    )
    WOOD_ELF = Rule(
        name='Wood Elf passives',
        icon='https://images.uesp.net/d/d2/ON-icon-Bosmer.png',
        buffs=[
            RacialPassives.HUNTERS_EYE.value,
            RacialPassives.YFFRES_ENDURANCE.value,
            RacialPassives.RESIST_AFFLICTION.value,
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
    BOW = Rule(
        name='Bow passives',
        icon='https://eso-hub.com/storage/icons/ability_bow_001.webp',
        buffs=[
            Passives.HAWK_EYE.value,
        ]
    )
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
    TWO_HANDED = Rule(
        name='Two Handed passives',
        icon='https://eso-hub.com/storage/icons/ability_2handed_006.webp',
        buffs=[
            Passives.FORCEFUL.value,
            Passives.FOLLOW_UP.value,
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
    DRAGONKNIGHT = Rule(
        name='Dragonknight passives',
        icon='https://eso-hub.com/storage/icons/class/gamepad/gp_class_dragonknight.png',
        buffs=[
            DRAGONKNIGHT_PASSIVES.COMBUSTION.value,
            DRAGONKNIGHT_PASSIVES.WARMTH.value,
            # Next 2 are bugged
            # DRAGONKNIGHT_PASSIVES.SEARING_HEAT.value,
            # DRAGONKNIGHT_PASSIVES.WORLD_IN_RUIN.value,
            DRAGONKNIGHT_PASSIVES.IRON_SKIN.value,
            DRAGONKNIGHT_PASSIVES.ELDER_DRAGON.value,
            # Next one is bugged
            # DRAGONKNIGHT_PASSIVES.SCALED_ARMOR.value,
            DRAGONKNIGHT_PASSIVES.ETERNAL_MOUNTAIN.value,
            DRAGONKNIGHT_PASSIVES.BATTLE_ROAR.value,
        ]
    )
    WARDEN = Rule(
        name='Warden passives',
        icon='https://eso-hub.com/storage/icons/class/gamepad/gp_class_warden.png',
        buffs=[
            WARDEN_PASSIVES.BOND_WITH_NATURE.value,
            WARDEN_PASSIVES.SAVAGE_BEAST.value,
            WARDEN_PASSIVES.FLOURISH.value,
            WARDEN_PASSIVES.ADVANCED_SPECIES.value,
            WARDEN_PASSIVES.ACCELERATED_GROWTH.value,
            WARDEN_PASSIVES.NATURES_GIFT.value,
            WARDEN_PASSIVES.EMERALD_MOSS.value,
            WARDEN_PASSIVES.MATURATION.value,
            WARDEN_PASSIVES.ICY_AURA.value,
            WARDEN_PASSIVES.PIERCING_COLD.value,
        ]
    )
    NIGHTBLADE = Rule(
        name='Nightblade passives',
        icon='https://eso-hub.com/storage/icons/class/gamepad/gp_class_nightblade.png',
        buffs=[
            NIGHTBLADE_PASSIVES.MASTER_ASSASSIN.value,
            NIGHTBLADE_PASSIVES.EXECUTIONER.value,
            NIGHTBLADE_PASSIVES.PRESSURE_POINTS.value,
            NIGHTBLADE_PASSIVES.HEMORRHAGE.value,
            NIGHTBLADE_PASSIVES.REFRESHING_SHADOWS.value,
            NIGHTBLADE_PASSIVES.SHADOW_BARRIER.value,
            NIGHTBLADE_PASSIVES.DARK_VIGOR.value,
            NIGHTBLADE_PASSIVES.DARK_VEIL.value,
            NIGHTBLADE_PASSIVES.CATALYST.value,
            NIGHTBLADE_PASSIVES.SOUL_SIPHONER.value,
        ]
    )
    SORCERER = Rule(
        name='Sorcerer passives',
        icon='https://eso-hub.com/storage/icons/class/gamepad/gp_class_sorcerer.png',
        buffs=[
            SORCERER_PASSIVES.REBATE.value,
            SORCERER_PASSIVES.EXPERT_SUMMONER.value,
            SORCERER_PASSIVES.BLOOD_MAGIC.value,
            # Only activates on block, skipping for now
            # SORCERER_PASSIVES.PERSISTENCE.value,
            SORCERER_PASSIVES.EXPLOITATION.value,
            SORCERER_PASSIVES.ENERGIZED.value,
        ]
    )
    TEMPLAR = Rule(
        name='Templar passives',
        icon='https://eso-hub.com/storage/icons/class/gamepad/gp_class_templar.png',
        buffs=[
            TEMPLAR_PASSIVES.PIERCING_SPEAR.value,
            TEMPLAR_PASSIVES.SPEAR_WALL.value,
            TEMPLAR_PASSIVES.BURNING_LIGHT.value,
            TEMPLAR_PASSIVES.ILLUMINATE.value,
            TEMPLAR_PASSIVES.RESTORING_SPIRIT.value,
            TEMPLAR_PASSIVES.SACRED_GROUND.value,
            TEMPLAR_PASSIVES.LIGHT_WEAVER.value,
            TEMPLAR_PASSIVES.MASTER_RITUALIST.value,
        ]
    )

    # |-----------------------------------------------------------------------|
    # | Guild passives check                                                  |
    # |-----------------------------------------------------------------------|
    UNDAUNTED = Rule(
        name='Undaunted passives',
        icon='https://eso-hub.com/storage/icons/ability_undaunted_001.webp',
        buffs=[
            Passives.UNDAUNTED_COMMAND.value,
            Passives.UNDAUNTED_METTLE.value,
        ]
    )
    MAGES_GUILD = Rule(
        name='Mages Guild passives',
        icon='https://eso-hub.com/storage/icons/ability_mageguild_005.webp',
        required=[
            GENERAL_SKILLS.DEGENERATION.value,
            GENERAL_SKILLS.STRUCTURED_ENTROPY.value,
            GENERAL_SKILLS.SCALDING_RUNE.value,
            GENERAL_SKILLS.BALANCE.value,
        ],
        buffs=[
            Passives.MAGICKA_CONTROLLER.value,
            Passives.MIGHT_OF_THE_GUILD.value,
        ],
    )
