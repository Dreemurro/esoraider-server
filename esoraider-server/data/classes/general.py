from data.buffs import BUFFS
from data.core import EsoEnum, Skill
from data.debuffs import DEBUFFS


class GENERAL_SKILLS(EsoEnum):
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
            UNSTABLE_WALL_OF_FROST,
            UNSTABLE_WALL_OF_FROST_DAMAGE,
            UNSTABLE_WALL_OF_FROST_EXPLOSION,
        ],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_002b.png',
    )
    CAMOUFLAGED_HUNTER = Skill(
        name='Camouflaged Hunter',
        id=40195,
        buffs=[BUFFS.MINOR_BERSERK_CAMOUFLAGED_HUNTER.value],
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
        buffs=[BUFFS.MAJOR_RESOLVE_BALANCE.value],
        link='https://eso-hub.com/en/skills/guild/mages-guild/balance',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mageguild_003_b.png',
    )
    HEROIC_SLASH = Skill(
        name='Heroic Slash',
        id=38264,
        buffs=[BUFFS.MINOR_HEROISM.value],
        # debuffs=[DEBUFFS.MINOR_MAIM_HEROIC_SLASH.value],
        link='https://eso-hub.com/en/skills/weapon/one-hand-and-shield/heroic-slash',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_1handed_001_a.png',
    )
    AGGRESSIVE_HORN = Skill(
        name='Aggressive Horn',
        id=40223,
        buffs=[
            BUFFS.AGGRESSIVE_HORN.value,
            BUFFS.MAJOR_FORCE_AGGRESSIVE_HORN.value,
        ],
        link='https://eso-hub.com/en/skills/alliance-war/assault/aggressive-horn',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_ava_003_a.png',
    )
    # QUICK_SIPHON = Skill(
    #     name='Quick Siphon',
    #     id=40116,
    #     debuffs=[],
    #     link='https://eso-hub.com/en/skills/weapon/restoration-staff/quick-siphon',
    # )
    CHANNELED_ACCELERATION = Skill(
        name='Channeled Acceleration',
        id=103706,
        buffs=[BUFFS.MINOR_FORCE.value],
        link='https://eso-hub.com/en/skills/guild/psijic-order/channeled-acceleration',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_psijic_005_a.png',
    )
    BARBED_TRAP = Skill(
        name='Barbed Trap',
        id=40382,
        buffs=[BUFFS.MINOR_FORCE.value],
        debuffs=[DEBUFFS.BARBED_TRAP.value],
        link='https://eso-hub.com/en/skills/guild/fighters-guild/barbed-trap',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_fightersguild_004_a.png',
    )
    SCALDING_RUNE = Skill(
        name='Scalding Rune',
        id=40465,
        debuffs=[DEBUFFS.SCALDING_RUNE.value],
        link='https://eso-hub.com/en/skills/guild/mages-guild/scalding-rune',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mageguild_001_b.png',
    )
    DEGENERATION = Skill(
        name='Degeneration',
        id=40457,
        buffs=[BUFFS.MAJOR_SORCERY.value],
        debuffs=[DEBUFFS.DEGENERATION.value],
        link='https://eso-hub.com/en/skills/guild/mages-guild/degeneration',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mageguild_004_a.png',
    )
    STRUCTURED_ENTROPY = Skill(
        name='Structured Entropy',
        id=40452,
        debuffs=[DEBUFFS.STRUCTURED_ENTROPY.value],
        link='https://eso-hub.com/en/skills/guild/mages-guild/structured-entropy',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mageguild_004_b.png',
    )
    FLAME_REACH = Skill(
        name='Flame Reach',
        id=38944,
        debuffs=[DEBUFFS.FLAME_REACH.value],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_007_b.png',
    )
    FROST_REACH = Skill(
        name='Frost Reach',
        id=38970,
        debuffs=[DEBUFFS.FROST_REACH.value],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_005_b.png',
    )
    DESTRUCTIVE_REACH = Skill(
        name='Destructive Reach',
        id=38937,
        link='https://eso-hub.com/en/skills/weapon/destruction-staff/destructive-reach',
        children=[
            FLAME_REACH,
            FROST_REACH,
        ],
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_005_b.png',
    )
    CONSUMING_TRAP = Skill(
        name='Consuming Trap',
        id=40317,
        debuffs=[DEBUFFS.CONSUMING_TRAP.value],
        link='https://eso-hub.com/en/skills/world/soul-magic/consuming-trap',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_otherclass_001_b.png',
    )
    COMBAT_PRAYER = Skill(
        name='Combat Prayer',
        id=40094,
        buffs=[
            BUFFS.MINOR_BERSERK_COMBAT_PRAYER.value,
            BUFFS.MINOR_RESOLVE_COMBAT_PRAYER.value,
        ],
        link='https://eso-hub.com/en/skills/weapon/restoration-staff/combat-prayer',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_restorationstaff_003_b.png',
    )
    DEADLY_CLOAK = Skill(
        name='Deadly Cloak',
        id=38906,
        # + buff ID = 123653 -> Major Evasion (with Deadly Cloak icon O__o)
        buffs=[BUFFS.MAJOR_EVASION.value],
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
    RENDING_SLASHES = Skill(
        name='Rending Slashes',
        id=38839,
        debuffs=[DEBUFFS.RENDING_SLASHES.value],
        link='https://eso-hub.com/en/skills/weapon/dual-wield/rending-slashes',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dualwield_001_a.png',
    )
    POISON_INJECTION = Skill(
        name='Poison Injection',
        id=38660,
        debuffs=[DEBUFFS.POISON_INJECTION.value],
        link='https://eso-hub.com/en/skills/weapon/bow/poison-injection',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_bow_002_b.png',
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
