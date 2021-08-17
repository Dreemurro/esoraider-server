from data.core import Buff, EsoEnum


class BUFFS(EsoEnum):
    # type 2 - Damage Buffs?
    """
    Minor / Major
    """
    """
    MINOR BERSERK
    KNOWN IDS 
    - 80471
    """
    MINOR_BERSERK = Buff(
        name='Minor Berserk',
        id=61744,  # Overall uptime?
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_berserk.png'
    )
    MINOR_BERSERK_COMBAT_PRAYER = Buff(
        name='Minor Berserk',
        id=62636,
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

    """
    MINOR RESOLVE
    KNOWN IDS 
    - 61693 (overall uptime?)
    """
    MINOR_RESOLVE_COMBAT_PRAYER = Buff(
        name='Minor Resolve',
        id=62634,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_buff_minor_resolve.png',
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

    """
    MAJOR SORCERY
    KNOWN IDS: 
    - 61747 (overall duration?) 
    - 61687 
    - 72933 (potion?)
    - 63227
    - 92503
    """
    MAJOR_SORCERY = Buff(
        name='Major Sorcery',
        id=61687,
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
    - 68632 (probably Barbed Trap)
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
    MAJOR_SLAYER_ROARING_OPPORTUNIST = Buff(
        name='Major Slayer',
        id=137986,
        icon='https://assets.rpglogs.com/img/eso/abilities/procs_006.png',
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

    """
    From glyphs
    """
    BERSERKER = Buff(
        name='Berserker',
        id=21230,
        icon='https://assets.rpglogs.com/img/eso/abilities/ava_artifact_006.png',
    )
