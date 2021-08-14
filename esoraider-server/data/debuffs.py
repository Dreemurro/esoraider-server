from data.core import Debuff, EsoEnum


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
