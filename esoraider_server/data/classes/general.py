from esoraider_server.data.buffs import Buffs
from esoraider_server.data.core import EsoEnum, Skill
from esoraider_server.data.debuffs import Debuffs
from esoraider_server.data.stacks import DebuffsWithStacks


class GeneralSkills(EsoEnum):
    BLOCKADE_OF_STORMS_DAMAGE = Skill(
        name='Blockade of Storms',
        id=62990,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_003_b.png',
    )
    BLOCKADE_OF_STORMS = Skill(
        name='Blockade of Storms',
        id=39018,
        children=[BLOCKADE_OF_STORMS_DAMAGE],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_003_b.png',
    )
    BLOCKADE_OF_FIRE_DAMAGE = Skill(
        name='Blockade of Fire',
        id=62912,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_004_b.png',
    )
    BLOCKADE_OF_FIRE = Skill(
        name='Blockade of Fire',
        id=39012,
        children=[BLOCKADE_OF_FIRE_DAMAGE],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_004_b.png',
    )
    BLOCKADE_OF_FROST_DAMAGE = Skill(
        name='Blockade of Frost',
        id=62951,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_002b.png',
    )
    BLOCKADE_OF_FROST = Skill(
        name='Blockade of Frost',
        id=39028,
        children=[BLOCKADE_OF_FROST_DAMAGE],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_002b.png',
    )
    ELEMENTAL_BLOCKADE = Skill(
        name='Elemental Blockade',
        id=39011,
        children=[
            BLOCKADE_OF_STORMS,
            BLOCKADE_OF_STORMS_DAMAGE,
            BLOCKADE_OF_FROST,
            BLOCKADE_OF_FROST_DAMAGE,
            BLOCKADE_OF_FIRE,
            BLOCKADE_OF_FIRE_DAMAGE,
        ],
        link='https://eso-hub.com/en/skills/weapon/destruction-staff/elemental-blockade',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_002a.png',
    )
    UNSTABLE_WALL_OF_FROST_EXPLOSION = Skill(
        name='Unstable Wall of Frost',
        id=39072,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_002a.png',
    )
    UNSTABLE_WALL_OF_FROST_DAMAGE = Skill(
        name='Unstable Wall of Frost',
        id=39071,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_002a.png',
    )
    UNSTABLE_WALL_OF_FROST = Skill(
        name='Unstable Wall of Frost',
        id=39067,
        link='https://eso-hub.com/en/skills/weapon/destruction-staff/unstable-wall-of-elements',
        children=[
            UNSTABLE_WALL_OF_FROST_DAMAGE,
            UNSTABLE_WALL_OF_FROST_EXPLOSION,
        ],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_002a.png',
    )
    UNSTABLE_WALL_OF_STORMS_EXPLOSION = Skill(
        name='Unstable Wall of Storms',
        id=39080,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_003_a.png',
    )
    UNSTABLE_WALL_OF_STORMS_DAMAGE = Skill(
        name='Unstable Wall of Storms',
        id=39079,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_003_a.png',
    )
    UNSTABLE_WALL_OF_STORMS = Skill(
        name='Unstable Wall of Storms',
        id=39073,
        link='https://eso-hub.com/en/skills/weapon/destruction-staff/unstable-wall-of-elements',
        children=[
            UNSTABLE_WALL_OF_STORMS_DAMAGE,
            UNSTABLE_WALL_OF_STORMS_EXPLOSION,
        ],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_003_a.png',
    )
    UNSTABLE_WALL_OF_FIRE_EXPLOSION = Skill(
        name='Unstable Wall of Fire',
        id=39056,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_004_a.png',
    )
    UNSTABLE_WALL_OF_FIRE_DAMAGE = Skill(
        name='Unstable Wall of Fire',
        id=39054,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_004_a.png',
    )
    UNSTABLE_WALL_OF_FIRE = Skill(
        name='Unstable Wall of Fire',
        id=39053,
        # buffs=[BUFFS.FIRE_WALL_DAMAGE_BONUS],
        link='https://eso-hub.com/en/skills/weapon/destruction-staff/unstable-wall-of-elements',
        children=[
            UNSTABLE_WALL_OF_FIRE_DAMAGE,
            UNSTABLE_WALL_OF_FIRE_EXPLOSION,
        ],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_004_a.png',
    )
    UNSTABLE_WALL_OF_ELEMENTS = Skill(
        name='Unstable Wall of Elements',
        id=39052,
        # buffs=[BUFFS.FIRE_WALL_DAMAGE_BONUS],
        link='https://eso-hub.com/en/skills/weapon/destruction-staff/unstable-wall-of-elements',
        children=[
            UNSTABLE_WALL_OF_FIRE,
            UNSTABLE_WALL_OF_FIRE_DAMAGE,
            UNSTABLE_WALL_OF_FIRE_EXPLOSION,
            UNSTABLE_WALL_OF_STORMS,
            UNSTABLE_WALL_OF_STORMS_DAMAGE,
            UNSTABLE_WALL_OF_STORMS_EXPLOSION,
            UNSTABLE_WALL_OF_FROST,
            UNSTABLE_WALL_OF_FROST_DAMAGE,
            UNSTABLE_WALL_OF_FROST_EXPLOSION,
        ],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_002b.png',
    )
    CAMOUFLAGED_HUNTER = Skill(
        name='Camouflaged Hunter',
        id=40195,
        buffs=[Buffs.MINOR_BERSERK_CAMOUFLAGED_HUNTER.value],
        link='https://eso-hub.com/en/skills/guild/fighters-guild/camouflaged-hunter',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_fightersguild_002_b.png',
    )
    MYSTIC_ORB_DAMAGE = Skill(
        name='Mystic Orb',
        id=42029,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_undaunted_004_a.png',
    )
    MYSTIC_ORB = Skill(
        name='Mystic Orb',
        id=42028,
        link='https://eso-hub.com/en/skills/guild/undaunted/mystic-orb',
        children=[MYSTIC_ORB_DAMAGE],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_undaunted_004_a.png',
    )
    BALANCE = Skill(
        name='Balance',
        id=40441,
        buffs=[Buffs.MAJOR_RESOLVE_BALANCE.value],
        link='https://eso-hub.com/en/skills/guild/mages-guild/balance',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mageguild_003_b.png',
    )
    HEROIC_SLASH = Skill(
        name='Heroic Slash',
        id=38264,
        buffs=[Buffs.MINOR_HEROISM_HEROIC_SLASH.value],
        # debuffs=[DEBUFFS.MINOR_MAIM_HEROIC_SLASH.value],
        link='https://eso-hub.com/en/skills/weapon/one-hand-and-shield/heroic-slash',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_1handed_001_a.png',
    )
    AGGRESSIVE_HORN = Skill(
        name='Aggressive Horn',
        id=40223,
        buffs=[
            Buffs.AGGRESSIVE_HORN.value,
            Buffs.MAJOR_FORCE_AGGRESSIVE_HORN.value,
        ],
        link='https://eso-hub.com/en/skills/alliance-war/assault/aggressive-horn',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_ava_003_a.png',
    )
    QUICK_SIPHON = Skill(
        name='Quick Siphon',
        id=40116,
        debuffs=[Debuffs.MINOR_LIFESTEAL_QUICK_SIPHON.value],
        link='https://eso-hub.com/en/skills/weapon/restoration-staff/quick-siphon',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_restorationstaff_005_b.png',
    )
    CHANNELED_ACCELERATION = Skill(
        name='Channeled Acceleration',
        id=103706,
        buffs=[Buffs.MINOR_FORCE_CHANNELED_ACCELERATION.value],
        link='https://eso-hub.com/en/skills/guild/psijic-order/channeled-acceleration',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_psijic_005_a.png',
    )
    RACE_AGAINST_TIME = Skill(
        name='Race Against Time',
        id=103710,
        buffs=[Buffs.MINOR_FORCE_RACE_AGAINST_TIME.value],
        link='https://eso-hub.com/en/skills/guild/psijic-order/race-against-time',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_psijic_005_b.png',
    )
    BARBED_TRAP = Skill(
        name='Barbed Trap',
        id=40382,
        buffs=[Buffs.MINOR_FORCE_BARBED_TRAP.value],
        debuffs=[Debuffs.BARBED_TRAP.value],
        link='https://eso-hub.com/en/skills/guild/fighters-guild/barbed-trap',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_fightersguild_004_a.png',
    )
    LIGHTWEIGHT_BEAST_TRAP = Skill(
        name='Lightweight Beast Trap',
        id=40372,
        buffs=[Buffs.MINOR_FORCE_LIGHTWEIGHT_BEAST_TRAP.value],
        debuffs=[Debuffs.LIGHTWEIGHT_BEAST_TRAP.value],
        link='https://eso-hub.com/en/skills/guild/fighters-guild/lightweight-beast-trap',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_fightersguild_004_b.png',
    )
    SCALDING_RUNE = Skill(
        name='Scalding Rune',
        id=40465,
        debuffs=[Debuffs.SCALDING_RUNE.value],
        link='https://eso-hub.com/en/skills/guild/mages-guild/scalding-rune',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mageguild_001_b.png',
    )
    DEGENERATION = Skill(
        name='Degeneration',
        id=40457,
        buffs=[Buffs.MAJOR_SORCERY_DEGENERATION.value],
        debuffs=[Debuffs.DEGENERATION.value],
        link='https://eso-hub.com/en/skills/guild/mages-guild/degeneration',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mageguild_004_a.png',
    )
    STRUCTURED_ENTROPY = Skill(
        name='Structured Entropy',
        id=40452,
        debuffs=[Debuffs.STRUCTURED_ENTROPY.value],
        link='https://eso-hub.com/en/skills/guild/mages-guild/structured-entropy',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mageguild_004_b.png',
    )
    FLAME_REACH = Skill(
        name='Flame Reach',
        id=38944,
        debuffs=[Debuffs.FLAME_REACH.value],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_007_b.png',
    )
    FROST_REACH = Skill(
        name='Frost Reach',
        id=38970,
        debuffs=[Debuffs.FROST_REACH.value],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_005_b.png',
    )
    SHOCK_REACH = Skill(
        name='Shock Reach',
        id=38978,
        debuffs=[Debuffs.SHOCK_REACH.value],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_006_b.png',
    )
    DESTRUCTIVE_REACH = Skill(
        name='Destructive Reach',
        id=38937,
        link='https://eso-hub.com/en/skills/weapon/destruction-staff/destructive-reach',
        children=[FLAME_REACH, FROST_REACH, SHOCK_REACH],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_005_b.png',
    )
    CONSUMING_TRAP = Skill(
        name='Consuming Trap',
        id=40317,
        debuffs=[Debuffs.CONSUMING_TRAP.value],
        link='https://eso-hub.com/en/skills/world/soul-magic/consuming-trap',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_otherclass_001_b.png',
    )
    BLESSING_OF_RESTORATION = Skill(
        name='Blessing Of Restoration',
        id=40103,
        buffs=[Buffs.MINOR_RESOLVE_BLESSING_OF_RESTORATION.value],
        link='https://eso-hub.com/en/skills/weapon/restoration-staff/blessing-of-restoration',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_restorationstaff_003_a.png',
    )
    COMBAT_PRAYER = Skill(
        name='Combat Prayer',
        id=40094,
        buffs=[
            Buffs.MINOR_BERSERK_COMBAT_PRAYER.value,
            Buffs.MINOR_RESOLVE_COMBAT_PRAYER.value,
        ],
        link='https://eso-hub.com/en/skills/weapon/restoration-staff/combat-prayer',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_restorationstaff_003_b.png',
    )
    DEADLY_CLOAK_DAMAGE = Skill(
        name='Deadly Cloak',
        id=62547,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dualwield_004_b.png',
    )
    DEADLY_CLOAK = Skill(
        name='Deadly Cloak',
        id=38906,
        children=[DEADLY_CLOAK_DAMAGE],
        buffs=[
            Buffs.DEADLY_CLOAK.value,
            Buffs.MAJOR_EVASION_DEADLY_CLOAK.value,
        ],
        link='https://eso-hub.com/en/skills/weapon/dual-wield/deadly-cloak',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dualwield_004_b.png',
    )
    ANTI_CAVALRY_CALTROPS_DAMAGE = Skill(
        name='Anti-Cavalry Caltrops',
        id=40267,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_ava_001_a.png',
    )
    ANTI_CAVALRY_CALTROPS = Skill(
        name='Anti-Cavalry Caltrops',
        id=40255,
        children=[ANTI_CAVALRY_CALTROPS_DAMAGE],
        link='https://eso-hub.com/en/skills/alliance-war/assault/anti-cavalry-caltrops',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_ava_001_a.png',
    )
    RAZOR_CALTROPS_DAMAGE = Skill(
        name='Razor Caltrops',
        id=40252,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_ava_001_b.png',
    )
    RAZOR_CALTROPS = Skill(
        name='Razor Caltrops',
        id=40242,
        children=[RAZOR_CALTROPS_DAMAGE],
        link='https://eso-hub.com/en/skills/alliance-war/assault/razor-caltrops',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_ava_001_b.png',
    )
    RENDING_SLASHES = Skill(
        name='Rending Slashes',
        id=38839,
        debuffs=[Debuffs.RENDING_SLASHES.value],
        link='https://eso-hub.com/en/skills/weapon/dual-wield/rending-slashes',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dualwield_001_a.png',
    )
    VENOM_ARROW = Skill(
        name='Venom Arrow',
        id=38645,
        debuffs=[Debuffs.VENOM_ARROW.value],
        link='https://eso-hub.com/en/skills/weapon/bow/venom-arrow',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_bow_002_a.png',
    )
    POISON_INJECTION = Skill(
        name='Poison Injection',
        id=38660,
        debuffs=[Debuffs.POISON_INJECTION.value],
        link='https://eso-hub.com/en/skills/weapon/bow/poison-injection',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_bow_002_b.png',
    )
    ENDLESS_HAIL_DAMAGE = Skill(
        name='Endless Hail',
        id=38690,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_bow_003_a.png',
    )
    ENDLESS_HAIL = Skill(
        name='Endless Hail',
        id=38689,
        children=[ENDLESS_HAIL_DAMAGE],
        link='https://eso-hub.com/en/skills/weapon/bow/endless-hail',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_bow_003_a.png',
    )
    ARROW_BARRAGE_DAMAGE = Skill(
        name='Arrow Barrage',
        id=38696,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_bow_003_b.png',
    )
    ARROW_BARRAGE = Skill(
        name='Arrow Barrage',
        id=38695,
        children=[ARROW_BARRAGE_DAMAGE],
        link='https://eso-hub.com/en/skills/weapon/bow/arrow-barrage',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_bow_003_b.png',
    )
    CARVE = Skill(
        name='Carve',
        id=38745,
        debuffs=[DebuffsWithStacks.CARVE.value],
        link='https://eso-hub.com/en/skills/weapon/two-handed/carve',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_2handed_002_a.png',
    )
    STAMPEDE_INITIAL_DAMAGE = Skill(
        name='Stampede',
        id=38792,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_2handed_003_a.png',
    )
    STAMPEDE_DAMAGE = Skill(
        name='Stampede',
        id=126474,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_2handed_003_a.png',
    )
    STAMPEDE = Skill(
        name='Stampede',
        id=38788,
        children=[STAMPEDE_INITIAL_DAMAGE, STAMPEDE_DAMAGE],
        link='https://eso-hub.com/en/skills/weapon/two-handed/stampede',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_2handed_003_a.png',
    )
    UNSTOPPABLE_BRUTE = Skill(
        name='Unstoppable Brute',
        id=39205,
        buffs=[Buffs.MAJOR_RESOLVE_UNSTOPPABLE_BRUTE.value],
        link='https://eso-hub.com/en/skills/armor/heavy-armor/unstoppable-brute',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_001_a.png',
    )
    IMMOVABLE = Skill(
        name='Immovable',
        id=39197,
        buffs=[Buffs.MAJOR_RESOLVE_IMMOVABLE.value],
        link='https://eso-hub.com/en/skills/armor/heavy-armor/immovable',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_001_b.png',
    )
    STALWART_GUARD = Skill(
        name='Stalwart Guard',
        id=61529,
        buffs=[
            Buffs.STALWART_GUARD.value,
            Buffs.MINOR_FORCE_STALWART_GUARD.value,
        ],
        link='https://eso-hub.com/en/skills/alliance-war/support/stalwart-guard',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_ava_stalwart_guard.png',
    )
    MYSTIC_GUARD = Skill(
        name='Mystic Guard',
        id=61536,
        buffs=[
            Buffs.MYSTIC_GUARD.value,
            Buffs.MINOR_VITALITY_MYSTIC_GUARD.value,
        ],
        link='https://eso-hub.com/en/skills/alliance-war/support/mystic-guard',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_ava_mystic_guard.png',
    )
    ELUDE = Skill(
        name='Elude',
        id=39192,
        buffs=[Buffs.ELUDE.value, Buffs.MAJOR_EVASION_ELUDE.value],
        link='https://eso-hub.com/en/skills/armor/medium-armor/elude',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_armor_002_b.png',
    )
    OVERFLOWING_ALTAR = Skill(
        name='Overflowing Altar',
        id=41958,
        debuffs=[Debuffs.MINOR_LIFESTEAL_OVERFLOWING_ALTAR.value],
        link='https://eso-hub.com/en/skills/guild/undaunted/overflowing-altar',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_undaunted_001_a.png',
    )
    ELEMENTAL_DRAIN = Skill(
        name='Elemental Drain',
        id=39095,
        debuffs=[
            Debuffs.MAJOR_BREACH_ELEMENTAL_DRAIN.value,
            Debuffs.MINOR_MAGICKASTEAL_ELEMENTAL_DRAIN.value,
        ],
        link='https://eso-hub.com/en/skills/weapon/destruction-staff/elemental-drain',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_011a.png',
    )
