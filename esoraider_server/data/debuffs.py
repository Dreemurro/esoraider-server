from esoraider_server.data.core import Debuff, EsoEnum


class DEBUFFS(EsoEnum):
    #
    # Minor / Major
    #

    # Major Breach
    # Known IDs:
    # - 108951 (Deep Fissure?)
    MAJOR_BREACH = Debuff(
        name='Major Breach',
        id=61743,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_debuff_major_breach.png',
    )
    MAJOR_BREACH_PIERCE_ARMOR = Debuff(
        name='Major Breach',
        id=62485,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_debuff_major_breach.png',
    )

    # Major Vulnerability
    MAJOR_VULNERABILITY = Debuff(
        name='Major Vulnerability',
        id=106754,  # Another ID - 122389, same uptime
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_debuff_major_vulnerability.png',
    )

    # Minor Maim
    MINOR_MAIM = Debuff(
        name='Minor Maim',
        id=61723,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_debuff_minor_maim.png',
    )
    MINOR_MAIM_HEROIC_SLASH = Debuff(
        name='Minor Maim',
        id=62504,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_debuff_minor_maim.png',
    )
    MINOR_MAIM_CHILL = Debuff(
        name='Minor Maim',
        id=68368,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_debuff_minor_maim.png',
    )

    # Minor Brittle
    # Known IDs:
    # - 146697 (uptime is identical to 145975)
    MINOR_BRITTLE = Debuff(
        name='Minor Brittle',
        id=145975,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_debuff_minor_brittle.png',
    )

    # Minor Lifesteal
    # Known IDs:
    # - 80020 (Overflowing Altar?)
    MINOR_LIFESTEAL = Debuff(
        name='Minor Lifesteal',
        id=86304,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_lifesteal.png',
    )

    # Minor Magickasteal
    # Known IDs:
    # - 148798 (Overcharged?)
    MINOR_MAGICKASTEAL = Debuff(
        name='Minor Magickasteal',
        id=88401,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_magickasteal.png',
    )

    # Minor Vulnerability
    # Known IDs:
    # - 130173 (Growing Swarm?)
    # - 68359
    MINOR_VULNERABILITY = Debuff(
        name='Minor Vulnerability',
        id=79717,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_debuff_minor_vulnerability.png',
    )
    MINOR_VULNERABILITY_FETCHER_INFECTION = Debuff(
        name='Minor Vulnerability',
        id=130168,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_debuff_minor_vulnerability.png',
    )

    # Minor Breach
    # Known IDs:
    # - 148803
    # - 146908
    MINOR_BREACH = Debuff(
        name='Minor Breach',
        id=61742,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_debuff_minor_breach.png',
    )
    MINOR_BREACH_POWER_OF_THE_LIGHT = Debuff(
        name='Minor Breach',
        id=68588,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_debuff_minor_breach.png',
    )

    """
    Elemental status effects
    """
    BURNING = Debuff(
        name='Burning',
        id=18084,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mage_062.png',
    )
    POISONED = Debuff(
        name='Poisoned',
        id=21929,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_rogue_030.png',
    )

    """
    From skills
    """
    BARBED_TRAP = Debuff(
        name='Barbed Trap',
        id=40385,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_fightersguild_004_a.png',
    )
    SCALDING_RUNE = Debuff(
        name='Scalding Rune',
        id=40468,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mageguild_001_b.png',
    )
    DEGENERATION = Debuff(
        name='Degeneration',
        id=126374,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mageguild_004_a.png',
    )
    STRUCTURED_ENTROPY = Debuff(
        name='Structured Entropy',
        id=126371,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_mageguild_004_b.png',
    )
    FLAME_REACH = Debuff(
        name='Flame Reach',
        id=62682,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_007_b.png',
    )
    FROST_REACH = Debuff(
        name='Frost Reach',
        id=62712,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_destructionstaff_005_b.png',
    )
    CONSUMING_TRAP = Debuff(
        name='Consuming Trap',
        id=126898,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_otherclass_001.png',
    )
    RENDING_SLASHES = Debuff(
        name='Rending Slashes',
        id=38841,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_dualwield_001_a.png',
    )
    VENOM_ARROW = Debuff(
        name='Venom Arrow',
        id=44545,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_bow_002_a.png',
    )
    POISON_INJECTION = Debuff(
        name='Poison Injection',
        id=44549,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_bow_002_b.png',
    )

    #
    # From sets
    #
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
    ROAR_OF_ALKOSH = Debuff(
        name='Roar of Alkosh',
        id=76667,
        icon='https://assets.rpglogs.com/img/eso/abilities/gear_dromathra_medium_head_a.png',
    )
    LINE_BREAKER = Debuff(
        name='Line-Breaker',
        id=75753,
        icon='https://assets.rpglogs.com/img/eso/abilities/gear_dromathra_medium_head_a.png',
    )
    THE_MORAG_TONG = Debuff(
        name='The Morag Tong',
        id=34384,  # Also has a personal buff with ID = 29112
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_rogue_021.png',
    )
    TREMORSCALE = Debuff(
        name='Tremorscale',
        id=80866,  # Another ID - 80865, lower uptime
        icon='https://assets.rpglogs.com/img/eso/abilities/gear_undauntedsuneripper_head_a.png',
    )
    WRATH_OF_ELEMENTS = Debuff(
        name='Wrath of Elements',
        id=147843,
        icon='https://assets.rpglogs.com/img/eso/abilities/gear_reachv2_staff_a.png',
    )
    CRIMSON_OATHS_RIVE = Debuff(
        name="Crimson Oath's Rive",
        id=159288,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_debuff_minor_fracture.png',
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
