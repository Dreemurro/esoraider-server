from esoraider_server.data.core import Buff, EsoEnum


class Buffs(EsoEnum):
    #
    # Minor / Major
    #

    # Major Berserk
    MAJOR_BERSERK = Buff(
        name='Major Berserk',
        id=61745,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_berserk.png',
    )
    MAJOR_BERSERK_KINRAS_WRATH = Buff(
        name='Major Berserk',
        id=150757,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_berserk.png',
    )

    # Minor Berserk
    MINOR_BERSERK = Buff(
        name='Minor Berserk',
        id=61744,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_berserk.png',
    )
    MINOR_BERSERK_CAMOUFLAGED_HUNTER = Buff(
        name='Minor Berserk',
        id=80471,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_berserk.png',
    )
    MINOR_BERSERK_COMBAT_PRAYER = Buff(
        name='Minor Berserk',
        id=62636,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_berserk.png',
    )
    MINOR_BERSERK_KINRAS_WRATH = Buff(
        name='Minor Berserk',
        id=150782,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_berserk.png',
    )

    # Major Resolve
    MAJOR_RESOLVE = Buff(
        name='Major Resolve',
        id=61694,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_resolve.png',
    )
    MAJOR_RESOLVE_RESTORING_FOCUS = Buff(
        name='Major Resolve',
        id=44836,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_resolve.png',
    )
    MAJOR_RESOLVE_CHANNELED_FOCUS = Buff(
        name='Major Resolve',
        id=44828,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_resolve.png',
    )
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
    MAJOR_RESOLVE_ICE_FORTRESS = Buff(
        name='Major Resolve',
        id=88761,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_resolve.png',
    )
    MAJOR_RESOLVE_BECKONING_ARMOR = Buff(
        name='Major Resolve',
        id=118239,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_resolve.png',
    )
    MAJOR_RESOLVE_SUMMONERS_ARMOR = Buff(
        name='Major Resolve',
        id=118246,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_resolve.png',
    )
    MAJOR_RESOLVE_HARDENED_ARMOR = Buff(
        name='Major Resolve',
        id=61827,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_resolve.png',
    )
    MAJOR_RESOLVE_UNSTOPPABLE_BRUTE = Buff(
        name='Major Resolve',
        id=63134,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_resolve.png',
    )
    MAJOR_RESOLVE_IMMOVABLE = Buff(
        name='Major Resolve',
        id=63119,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_resolve.png',
    )
    MAJOR_RESOLVE_HURRICANE = Buff(
        name='Major Resolve',
        id=62168,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_resolve.png',
    )
    MAJOR_RESOLVE_BOUNDLESS_STORM = Buff(
        name='Major Resolve',
        id=62175,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_resolve.png',
    )

    # Minor Resolve
    MINOR_RESOLVE = Buff(
        name='Minor Resolve',
        id=61693,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_resolve.png',
    )
    MINOR_RESOLVE_BLESSING_OF_RESTORATION = Buff(
        name='Minor Resolve',
        id=62626,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_resolve.png',
    )
    MINOR_RESOLVE_COMBAT_PRAYER = Buff(
        name='Minor Resolve',
        id=62634,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_resolve.png',
    )

    # Major Heroism
    MAJOR_HEROISM = Buff(
        name='Major Heroism',
        id=61709,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_heroism.png',
    )
    MAJOR_HEROISM_DRAKES_RUSH = Buff(
        name='Major Heroism',
        id=150974,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_heroism.png',
    )

    # Minor Heroism
    MINOR_HEROISM = Buff(
        name='Minor Heroism',
        id=61708,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_heroism.png',
    )
    MINOR_HEROISM_HEROIC_SLASH = Buff(
        name='Minor Heroism',
        id=62505,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_heroism.png',
    )

    # Major Brutality
    # Known IDs:
    # - 72936
    MAJOR_BRUTALITY = Buff(
        name='Major Brutality',
        id=61665,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_brutality.png',
    )
    MAJOR_BRUTALITY_IGNEOUS_WEAPONS = Buff(
        name='Major Brutality',
        id=76518,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_brutality.png',
    )
    MAJOR_BRUTALITY_BLUE_BETTY = Buff(
        name='Major Brutality',
        id=131350,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_brutality.png',
    )
    MAJOR_BRUTALITY_BULL_NETCH = Buff(
        name='Major Brutality',
        id=89110,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_brutality.png',
    )
    MAJOR_BRUTALITY_POWER_SURGE = Buff(
        name='Major Brutality',
        id=62060,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_brutality.png',
    )
    MAJOR_BRUTALITY_CRITICAL_SURGE = Buff(
        name='Major Brutality',
        id=62147,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_brutality.png',
    )

    # Major Sorcery
    # Known IDs:
    # - 61747 (overall duration?)
    # - 72933 (potion?)
    MAJOR_SORCERY = Buff(
        name='Major Sorcery',
        id=61687,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_sorcery.png',
    )
    MAJOR_SORCERY_IGNEOUS_WEAPONS = Buff(
        name='Major Sorcery',
        id=92503,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_sorcery.png',
    )
    MAJOR_SORCERY_BLUE_BETTY = Buff(
        name='Major Sorcery',
        id=89107,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_sorcery.png',
    )
    MAJOR_SORCERY_BULL_NETCH = Buff(
        name='Major Sorcery',
        id=95125,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_sorcery.png',
    )
    MAJOR_SORCERY_DEGENERATION = Buff(
        name='Major Sorcery',
        id=63227,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_sorcery.png',
    )
    MAJOR_SORCERY_POWER_SURGE = Buff(
        name='Major Sorcery',
        id=62062,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_sorcery.png',
    )
    MAJOR_SORCERY_CRITICAL_SURGE = Buff(
        name='Major Sorcery',
        id=131311,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_sorcery.png',
    )

    # Minor Sorcery
    # Known IDs:
    # - 62800
    MINOR_SORCERY = Buff(
        name='Minor Sorcery',
        id=61685,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_sorcery.png',
    )

    # Major Force
    MAJOR_FORCE = Buff(
        name='Major Force',
        id=61747,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_force.png',
    )
    MAJOR_FORCE_AGGRESSIVE_HORN = Buff(
        name='Major Force',
        id=40225,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_force.png',
    )
    MAJOR_FORCE_SAXHLEEL_CHAMPION = Buff(
        name='Major Force',
        id=154830,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_force.png',
    )

    # Minor Force
    # Known IDs:
    # - 85611 (Medusa set)
    MINOR_FORCE = Buff(
        name='Minor Force',
        id=61746,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_force.png',
    )
    MINOR_FORCE_BARBED_TRAP = Buff(
        name='Minor Force',
        id=68632,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_force.png',
    )
    MINOR_FORCE_LIGHTWEIGHT_BEAST_TRAP = Buff(
        name='Minor Force',
        id=68628,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_force.png',
    )
    MINOR_FORCE_CHANNELED_ACCELERATION = Buff(
        name='Minor Force',
        id=103708,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_force.png',
    )
    MINOR_FORCE_RACE_AGAINST_TIME = Buff(
        name='Minor Force',
        id=103712,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_force.png',
    )
    MINOR_FORCE_TZOGVINS_WARBAND = Buff(
        name='Minor Force',
        id=116775,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_force.png',
    )
    MINOR_FORCE_STALWART_GUARD = Buff(
        name='Minor Force',
        id=80986,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_force.png',
    )

    MINOR_COURAGE = Buff(
        name='Minor Courage',
        id=147417,  # Another ID - 121878
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_courage.png',
    )

    # Major Courage
    # Known IDs:
    # - 110020
    MAJOR_COURAGE = Buff(
        name='Major Courage',
        id=109966,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_045.png',
    )
    MAJOR_COURAGE_SPELL_POWER_CURE = Buff(
        name='Major Courage',
        id=66902,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_045.png',
    )
    MAJOR_COURAGE_OLORIME = Buff(
        name='Major Courage',
        id=109994,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_courage.png',
    )

    """
    MAJOR SLAYER
    KNOWN IDS:
    - 93120
    - 93442
    """
    MAJOR_SLAYER = Buff(
        name='Major Slayer',
        id=93109,  # Probably overall uptime, occurs both with WM and RO
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_slayer.png',
    )
    MAJOR_SLAYER_MASTER_ARCHITECT = Buff(
        name='Major Slayer',
        id=93120,
        icon='https://assets.rpglogs.com/img/eso/abilities/procs_006.png',
    )
    MAJOR_SLAYER_ROARING_OPPORTUNIST = Buff(
        name='Major Slayer',
        id=135923,
        icon='https://assets.rpglogs.com/img/eso/abilities/procs_006.png',
    )

    # Major Evasion
    MAJOR_EVASION = Buff(
        name='Major Evasion',
        id=61716,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_evasion.png',
    )
    MAJOR_EVASION_ELUDE = Buff(
        name='Major Evasion',
        id=63030,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_evasion.png',
    )
    MAJOR_EVASION_DEADLY_CLOAK = Buff(
        name='Major Evasion',
        id=123653,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_evasion.png',
    )
    MAJOR_EVASION_GOSSAMER = Buff(
        name='Major Evasion',
        id=84341,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_evasion.png',
    )

    # Major Prophecy
    # Known IDs:
    # - 64570 (potion?)
    # - 77945 (inner light?)
    # - 137006 (alliance potion?)
    MAJOR_PROPHECY = Buff(
        name='Major Prophecy',
        id=61689,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_prophecy.png',
    )
    MAJOR_PROPHECY_FLAMES_OF_OBLIVION = Buff(
        name='Major Prophecy',
        id=76420,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_prophecy.png',
    )
    MAJOR_PROPHECY_REFLECTIVE_LIGHT = Buff(
        name='Major Prophecy',
        id=62755,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_prophecy.png',
    )
    MAJOR_PROPHECY_LOTUS_BLOSSOM = Buff(
        name='Major Prophecy',
        id=86303,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_prophecy.png',
    )

    # Minor Prophecy
    # Known IDs:
    # - 62320
    MINOR_PROPHECY = Buff(
        name='Minor Prophecy',
        id=61691,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_prophecy.png',
    )

    # Major Savagery
    # Known IDs:
    # - 61898
    MAJOR_SAVAGERY = Buff(
        name='Major Savagery',
        id=61667,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_savagery.png',
    )
    MAJOR_SAVAGERY_FLAMES_OF_OBLIVION = Buff(
        name='Major Savagery',
        id=76426,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_savagery.png',
    )

    # Minor Savagery
    # Known IDs:
    # - 61898
    MINOR_SAVAGERY = Buff(
        name='Minor Savagery',
        id=61666,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_savagery.png',
    )

    # Minor Vitality
    MINOR_VITALITY = Buff(
        name='Minor Vitality',
        id=61549,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_vitality.png',
    )
    MINOR_VITALITY_MYSTIC_GUARD = Buff(
        name='Minor Vitality',
        id=64080,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_vitality.png',
    )

    # Minor Expedition
    MINOR_EXPEDITION = Buff(
        name='Minor Expedition',
        id=61735,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_expedition.png',
    )
    MINOR_EXPEDITION_HURRICANE = Buff(
        name='Minor Expedition',
        id=82797,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_expedition.png',
    )

    # Minor Intellect
    MINOR_INTELLECT = Buff(
        name='Minor Intellect',
        id=61706,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_expedition.png',
    )
    MINOR_INTELLECT_EMPOWERED_WARD = Buff(
        name='Minor Intellect',
        id=77418,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_intellect.png',
    )

    # Minor Protection
    MINOR_PROTECTION = Buff(
        name='Minor Protection',
        id=61721,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_protection.png',
    )
    MINOR_PROTECTION_ICE_FORTRESS = Buff(
        name='Minor Protection',
        id=87194,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_protection.png',
    )

    #
    # From skills
    #
    # FIRE_WALL_DAMAGE_BONUS = Buff(
    #     name='Fire Wall Damage Bonus',
    #     id=43192,
    # )
    AGGRESSIVE_HORN = Buff(
        name='Aggressive Horn',
        id=40224,  # Another ID - 94800
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_ava_003_a.png',
    )
    STALWART_GUARD = Buff(
        name='Stalwart Guard',
        id=80983,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_ava_stalwart_guard.png',
    )
    MYSTIC_GUARD = Buff(
        name='Mystic Guard',
        id=80947,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_ava_mystic_guard.png',
    )
    ELUDE = Buff(
        name='Elude',
        id=126958,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_065.png',
    )
    DEADLY_CLOAK = Buff(
        name='Deadly Cloak',
        id=38906,  # Matches skill ID
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dualwield_004_b.png',
    )

    #
    # From sets
    #
    CRUSHING_WALL = Buff(
        name='Crushing Wall',
        id=100155,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_065.png',
    )
    BEHEMOTHS_AURA = Buff(
        name="Behemoth's Aura",
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
    CAUSTIC_ARROW = Buff(
        name='Caustic Arrow',
        id=100105,  # Another ID - 99766, lower uptime
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_065.png',
    )
    VIRULENT_SHOT = Buff(
        name='Virulent Shot',
        id=113619,  # Another ID - 113628, lower uptime
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_065.png',
    )
    WRATH_OF_ELEMENTS = Buff(  # This one has stacks
        name='Wrath of Elements',
        id=149413,  # Another ID - 147828, lower uptime
        icon='https://assets.rpglogs.com/img/eso/abilities/gear_reachv2_staff_a.png',
    )
    SPECTRAL_CLOAK = Buff(
        # Additional IDs:
        # - 141875 - probably tied with Blade Cloak activation
        # - 113616 - probably uptime of front/back bar with this set equipped
        name='Spectral Cloak',
        id=113617,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_rogue_053.png',
    )
    DESTRUCTIVE_IMPACT = Buff(
        name='Destructive Impact',
        id=140334,  # Another ID - 99774, lower uptime
        icon='https://eso-hub.com/storage/icons/ability_mage_023.png',
    )
    KINRAS_WRATH = Buff(
        name="Kinras's Wrath",
        id=150780,  # Another ID - 150749 (having set equipped)
        icon='https://eso-hub.com/storage/icons/ability_mage_065.png',
    )
    FORCE_OVERFLOW = Buff(
        name='Force Overflow',
        id=147875,  # Another ID - 147871 (having set equipped)
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_065.png',
    )
    SUL_XAN_SOULBOUND = Buff(
        name='Sul-Xan Soulbound',
        id=154737,
        icon='https://assets.rpglogs.com/img/eso/abilities/u30_trial_soulrip.png',
    )
    BURNING_SPELLWEAVE = Buff(
        name='Burning Spellweave',
        id=61459,  # Additional ID - 60418
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_007.png',
    )

    """
    From glyphs
    """
    BERSERKER = Buff(
        name='Berserker',
        id=21230,
        icon='https://assets.rpglogs.com/img/eso/abilities/ava_artifact_006.png',
    )

    #
    # Misc
    #
    EMPOWER = Buff(
        name='Empower',
        id=61737,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_empower.png',
    )
    EMPOWER_MIGHT_OF_THE_GUILD = Buff(
        name='Empower',
        id=65541,  # Passive, 50% proc from casting Mages' Guild skill
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_empower.png',
    )
    EMPOWER_EMPOWERING_GRASP = Buff(
        name='Empower',
        id=118366,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_empower.png',
    )
    EMPOWER_SOLAR_BARRAGE = Buff(
        name='Empower',
        id=109420,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_major_empower.png',
    )
