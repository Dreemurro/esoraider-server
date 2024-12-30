from esoraider_server.data.classes.dragonknight.passives import (
    DragonknightPassives,
)
from esoraider_server.data.classes.general import GeneralSkills
from esoraider_server.data.classes.necromancer.passives import (
    NecromancerPassives,
)
from esoraider_server.data.classes.nightblade.passives import NightbladePassives
from esoraider_server.data.classes.sorcerer.passives import SorcererPassives
from esoraider_server.data.classes.templar.passives import TemplarPassives
from esoraider_server.data.classes.warden.passives import WardenPassives
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
        ],
    )
    MEDIUM_ARMOR = Rule(
        name='Medium armor passives',
        icon='https://eso-hub.com/storage/icons/ability_armor_002.webp',
        buffs=[
            Passives.WIND_WALKER.value,
            # Next 2 are bugged
            # Passives.DEXTERITY.value,
            # Passives.AGILITY.value,
        ],
    )

    # |-----------------------------------------------------------------------|
    # | Weapon passives check                                                 |
    # |-----------------------------------------------------------------------|
    BOW = Rule(
        name='Bow passives',
        icon='https://eso-hub.com/storage/icons/ability_bow_001.webp',
        buffs=[
            Passives.HAWK_EYE.value,
        ],
    )
    DESTRUCTION_STAFF = Rule(
        name='Destruction staff passives',
        icon='https://eso-hub.com/storage/icons/ability_destructionstaff_012.webp',
        buffs=[
            Passives.TRI_FOCUS.value,
            Passives.PENETRATING_MAGIC.value,
            Passives.ANCIENT_KNOWLEDGE.value,
            Passives.DESTRUCTION_EXPERT.value,
        ],
    )
    TWO_HANDED = Rule(
        name='Two Handed passives',
        icon='https://eso-hub.com/storage/icons/ability_2handed_006.webp',
        buffs=[
            Passives.FORCEFUL.value,
            Passives.FOLLOW_UP.value,
        ],
    )

    # |-----------------------------------------------------------------------|
    # | Class passives check                                                  |
    # |-----------------------------------------------------------------------|
    NECROMANCER = Rule(
        name='Necromancer passives',
        icon='https://eso-hub.com/storage/icons/class/gamepad/gp_class_necromancer.png',
        buffs=[
            NecromancerPassives.DEATH_GLEANING.value,
            NecromancerPassives.HEALTH_AVARICE.value,
            NecromancerPassives.LAST_GASP.value,
            # Reusasble Parts is not in combatant info, skipping for now
            # NECROMANCER_PASSIVES.REUSABLE_PARTS.value,
            NecromancerPassives.DISMEMBER.value,
            NecromancerPassives.RAPID_ROT.value,
            NecromancerPassives.CURATIVE_CURSE.value,
            NecromancerPassives.NEAR_DEATH_EXPERIENCE.value,
            NecromancerPassives.CORPSE_CONSUMPTION.value,
            NecromancerPassives.UNDEAD_CONFEDERATE.value,
        ],
    )
    DRAGONKNIGHT = Rule(
        name='Dragonknight passives',
        icon='https://eso-hub.com/storage/icons/class/gamepad/gp_class_dragonknight.png',
        buffs=[
            DragonknightPassives.COMBUSTION.value,
            DragonknightPassives.WARMTH.value,
            # Next 2 are bugged
            # DRAGONKNIGHT_PASSIVES.SEARING_HEAT.value,
            # DRAGONKNIGHT_PASSIVES.WORLD_IN_RUIN.value,
            DragonknightPassives.IRON_SKIN.value,
            DragonknightPassives.ELDER_DRAGON.value,
            # Next one is bugged
            # DRAGONKNIGHT_PASSIVES.SCALED_ARMOR.value,
            DragonknightPassives.ETERNAL_MOUNTAIN.value,
            DragonknightPassives.BATTLE_ROAR.value,
        ],
    )
    WARDEN = Rule(
        name='Warden passives',
        icon='https://eso-hub.com/storage/icons/class/gamepad/gp_class_warden.png',
        buffs=[
            WardenPassives.BOND_WITH_NATURE.value,
            WardenPassives.SAVAGE_BEAST.value,
            WardenPassives.FLOURISH.value,
            WardenPassives.ADVANCED_SPECIES.value,
            WardenPassives.ACCELERATED_GROWTH.value,
            WardenPassives.NATURES_GIFT.value,
            WardenPassives.EMERALD_MOSS.value,
            WardenPassives.MATURATION.value,
            WardenPassives.ICY_AURA.value,
            WardenPassives.PIERCING_COLD.value,
        ],
    )
    NIGHTBLADE = Rule(
        name='Nightblade passives',
        icon='https://eso-hub.com/storage/icons/class/gamepad/gp_class_nightblade.png',
        buffs=[
            NightbladePassives.MASTER_ASSASSIN.value,
            NightbladePassives.EXECUTIONER.value,
            NightbladePassives.PRESSURE_POINTS.value,
            NightbladePassives.HEMORRHAGE.value,
            NightbladePassives.REFRESHING_SHADOWS.value,
            NightbladePassives.SHADOW_BARRIER.value,
            NightbladePassives.DARK_VIGOR.value,
            NightbladePassives.DARK_VEIL.value,
            NightbladePassives.CATALYST.value,
            NightbladePassives.SOUL_SIPHONER.value,
        ],
    )
    SORCERER = Rule(
        name='Sorcerer passives',
        icon='https://eso-hub.com/storage/icons/class/gamepad/gp_class_sorcerer.png',
        buffs=[
            SorcererPassives.REBATE.value,
            SorcererPassives.EXPERT_SUMMONER.value,
            SorcererPassives.BLOOD_MAGIC.value,
            # Only activates on block, skipping for now
            # SORCERER_PASSIVES.PERSISTENCE.value,
            SorcererPassives.EXPLOITATION.value,
            SorcererPassives.ENERGIZED.value,
        ],
    )
    TEMPLAR = Rule(
        name='Templar passives',
        icon='https://eso-hub.com/storage/icons/class/gamepad/gp_class_templar.png',
        buffs=[
            TemplarPassives.PIERCING_SPEAR.value,
            TemplarPassives.SPEAR_WALL.value,
            TemplarPassives.BURNING_LIGHT.value,
            TemplarPassives.ILLUMINATE.value,
            TemplarPassives.RESTORING_SPIRIT.value,
            TemplarPassives.SACRED_GROUND.value,
            TemplarPassives.LIGHT_WEAVER.value,
            TemplarPassives.MASTER_RITUALIST.value,
        ],
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
        ],
    )
    MAGES_GUILD = Rule(
        name='Mages Guild passives',
        icon='https://eso-hub.com/storage/icons/ability_mageguild_005.webp',
        required=[
            GeneralSkills.DEGENERATION.value,
            GeneralSkills.STRUCTURED_ENTROPY.value,
            GeneralSkills.SCALDING_RUNE.value,
            GeneralSkills.BALANCE.value,
        ],
        buffs=[
            Passives.MAGICKA_CONTROLLER.value,
            Passives.MIGHT_OF_THE_GUILD.value,
        ],
    )
    FIGHTERS_GUILD = Rule(
        name='Fighters Guild passives',
        icon='https://eso-hub.com/storage/icons/ability_fightersguild_005.webp',
        required=[
            GeneralSkills.BARBED_TRAP.value,
            GeneralSkills.LIGHTWEIGHT_BEAST_TRAP.value,
            GeneralSkills.CAMOUFLAGED_HUNTER.value,
        ],
        buffs=[
            Passives.SLAYER.value,
        ],
    )
    PSIJIC_ORDER = Rule(
        name='Psijic Order passives',
        icon='https://eso-hub.com/storage/icons/ability_psijic_001.webp',
        required=[
            GeneralSkills.CHANNELED_ACCELERATION.value,
            GeneralSkills.RACE_AGAINST_TIME.value,
        ],
        buffs=[
            Passives.CLAIRVOYANCE.value,
            Passives.SPELL_ORB.value,
            Passives.CONCENTRATED_BARRIER.value,
            Passives.DELIBERATION.value,
        ],
    )
