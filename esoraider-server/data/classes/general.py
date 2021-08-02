from data.core import Buff, Debuff, EsoEnum, Skill


class BUFFS(EsoEnum):
    # type 2 - Damage Buffs?
    """
    Minor / Major
    """
    MINOR_BERSERK = Buff(
        name='Minor Berserk',
        id=61744,  # Another ID - 80471
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_berserk.png'
    )

    """
    MAJOR RESOLVE
    KNOWN IDS - 80160, 88758, 61694
    """
    MAJOR_RESOLVE_BALANCE = Buff(
        name='Major Resolve',
        id=80160,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_resolve.png',
    )
    MAJOR_RESOLVE_FROST_CLOAK = Buff(
        name='Major Resolve',
        id=88758,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_resolve.png',
    )

    MINOR_HEROISM = Buff(
        name='Minor Heroism',
        id=62505,  # Another ID - 61708
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_heroism.png',
    )
    MAJOR_BRUTALITY = Buff(
        name='Major Brutality',
        id=61665,  # Another ID - 76518
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_brutality.png',
    )
    MAJOR_SORCERY = Buff(
        name='Major Sorcery',
        id=61687,  # Another ID - 92503
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_sorcery.png',
    )

    """
    MAJOR FORCE
    KNOWN IDS: 
    - 61747 (overall duration?) 
    """
    MAJOR_FORCE = Buff(
        name='Major Force',
        id=40225,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_force.png',
    )
    MAJOR_FORCE_SAXHLEEL_CHAMPION = Buff(
        name='Major Force',
        id=154830,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_force.png',
    )

    """
    MINOR FORCE
    KNOWN IDS: 
    - 103708
    """
    MINOR_FORCE = Buff(
        name='Minor Force',
        id=61746,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_force.png',
    )

    MINOR_COURAGE = Buff(
        name='Minor Courage',
        id=147417,  # Another ID - 121878
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_courage.png',
    )
    MAJOR_COURAGE = Buff(
        name='Major Courage',
        id=66902,  # Source - Tier Bonus (4pc), type - 2, flag - 7
        # Another ID = 109966, source - Active Ability, type - 2, flag - 1
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_045.png',
    )
    MAJOR_SLAYER = Buff(
        name='Major Slayer',
        id=93109,  # Source - Tier Bonus (4pc), type - 2, flag - 1
        # Another ID - 93120, source - Active Ability, type - 2, flag - 5
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_slayer.png',
    )

    """
    From skills
    """
    # FIRE_WALL_DAMAGE_BONUS = Buff(
    #     name='Fire Wall Damage Bonus',
    #     id=43192,
    # )
    AGGRESSIVE_HORN = Buff(
        name='Aggressive Horn',
        id=40224,  # Another ID - 94800
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_ava_003_a.png',
    )

    """
    From sets
    """
    CRUSHING_WALL = Buff(
        name='Crushing Wall',
        id=100155,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_065.png',
    )
    HUNTERS_FOCUS = Buff(
        name='Hunter\'s Focus',
        id=155150,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_rogue_066.png',
    )
    BEHEMOTHS_AURA = Buff(
        name='Behemoth\'s Aura',
        id=151033,
        icon='https://assets.rpglogs.com/img/eso/abilities/death_recap_fire_dot_heavy.png',
    )
    POWERFUL_ASSAULT = Buff(
        name='Powerful Assault',
        id=61771,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_healer_019.png',
    )
    RANGE_SUPREMACY = Buff(
        name='Range Supremacy',
        id=154571,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_rogue_042.png',
    )
    MELEE_SUPREMACY = Buff(
        name='Melee Supremacy',
        id=154574,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_rogue_026.png',
    )


class DEBUFFS(EsoEnum):
    """
    Minor / Major
    """
    # TODO: Lots of IDs here, probably source-depended
    MINOR_MAIM = Debuff(
        name='Minor Maim',
        id=0,
    )
    # Example - 6qyxtA9LNYmhgP7T#fight=3&type=auras&hostility=1&spells=debuffs&target=11
    MINOR_MAIM_TOTAL = Debuff(
        name='Minor Maim',
        id=61723,
    )
    MINOR_MAIM_HEROIC_SLASH = Debuff(
        name='Minor Maim',
        id=62504,
    )
    # TODO: Lots of IDs here, probably source-depended
    MINOR_LIFESTEAL = Debuff(
        name='Minor Lifesteal',
        id=0,
    )
    MINOR_VULNERABILITY = Debuff(
        name='Minor Vulnerability',
        id=79717,  # Another ID - 130168
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_debuff_minor_vulnerability.png',
    )

    """
    From sets
    """
    FROST_WEAKNESS = Debuff(
        name='Frost Weakness',
        id=142652,
        icon='https://assets.rpglogs.com/img/eso/abilities/death_recap_cold_melee.png',
    )
    FLAME_WEAKNESS = Debuff(
        name='Flame Weakness',
        id=142610,
        icon='https://assets.rpglogs.com/img/eso/abilities/death_recap_fire_melee.png',
    )
    SHOCK_WEAKNESS = Debuff(
        name='Shock Weakness',
        id=142653,
        icon='https://assets.rpglogs.com/img/eso/abilities/death_recap_shock_melee.png',
    )
    WAY_OF_MARTIAL_KNOWLEDGE = Debuff(
        name='Way of Martial Knowledge',
        id=127070,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_044.png',
    )
    TOUCH_OF_ZEN = Debuff(
        name='Touch of Z\'en',
        id=126597,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_healer_006.png',
    )

    """
    From glyphs
    """
    CRUSHER = Debuff(
        name='Crusher',
        id=17906,
        icon='https://assets.rpglogs.com/img/eso/abilities/ava_artifact_004.png',
    )
    WEAKENING = Debuff(
        name='Weakening',
        id=17945,
        icon='https://assets.rpglogs.com/img/eso/abilities/ava_artifact_005.png',
    )


class GENERAL_SKILLS(EsoEnum):
    BLOCKADE_OF_FROST_DAMAGE = Skill(
        name='Blockade of Frost',
        id=39028,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_002b.png',
    )
    BLOCKADE_OF_FROST = Skill(
        name='Blockade of Frost',
        id=62951,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_002b.png',
    )
    ELEMENTAL_BLOCKADE = Skill(
        name='Elemental Blockade',
        id=39011,
        children=[
            BLOCKADE_OF_FROST,
            BLOCKADE_OF_FROST_DAMAGE,
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
        buffs=[BUFFS.MINOR_BERSERK.value],
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
        buffs=[BUFFS.AGGRESSIVE_HORN.value, BUFFS.MAJOR_FORCE.value],
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
