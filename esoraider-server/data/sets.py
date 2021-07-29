from data.classes.general import BUFFS, DEBUFFS
from data.core import EsoEnum, GearSet


class GEAR_SETS(EsoEnum):
    PERFECTED_CRUSHING_WALL = GearSet(
        name='Perfected Crushing Wall',
        id=526,
        buffs=[BUFFS.CRUSHING_WALL.value],
        link='https://eso-hub.com/en/sets/perfected-crushing-wall',
        icon='https://eso-hub.com/storage/icons/gear_dwarvenscavenged_staff_a.png',
    )
    HARPOONERS_WADING_KILT = GearSet(
        name='Harpooner\'s Wading Kilt',
        id=594,
        buffs=[BUFFS.HUNTERS_FOCUS.value],
        link='https://eso-hub.com/en/sets/harpooners-wading-kilt',
        icon='https://eso-hub.com/storage/icons/gear_kothringikilt_a.png',
    )
    ELEMENTAL_CATALYST = GearSet(
        name='Elemental Catalyst',
        id=516,
        debuffs=[
            DEBUFFS.FROST_WEAKNESS.value,
            DEBUFFS.FLAME_WEAKNESS.value,
            DEBUFFS.SHOCK_WEAKNESS.value,
        ],
        link='https://eso-hub.com/en/sets/elemental-catalyst',
        icon='https://eso-hub.com/storage/icons/gear_northlandsalchlgt_head_a.png',
    )
    PERFECTED_CLAW_OF_YOLNAHKRIIN = GearSet(
        name='Perfected Claw of Yolnahkriin',
        id=451,
        buffs=[BUFFS.MINOR_COURAGE.value],
        link='https://eso-hub.com/en/sets/perfected-claw-of-yolnahkriin',
        icon='https://eso-hub.com/storage/icons/gear_sunspire_heavy_helmet_a.png',
    )
    ENCRATISS_BEHEMOTH = GearSet(
        name='Encratis\'s Behemoth',
        id=577,
        buffs=[BUFFS.BEHEMOTHS_AURA.value],
        link='https://eso-hub.com/en/sets/encratiss-behemoth',
        icon='https://eso-hub.com/storage/icons/gear_undfiregiant_head_a.png',
    )
    SPELL_POWER_CURE = GearSet(
        name='Spell Power Cure',
        id=185,
        buffs=[BUFFS.MAJOR_COURAGE.value],
        link='https://eso-hub.com/en/sets/spell-power-cure',
        icon='https://eso-hub.com/storage/icons/gear_imperialdaedric_light_head_a.png',
    )
    MASTER_ARCHITECT = GearSet(
        name='Master Architect',
        id=332,
        buffs=[BUFFS.MAJOR_SLAYER.value],
        link='https://eso-hub.com/en/sets/master-architect',
        icon='https://eso-hub.com/storage/icons/gear_clockwork_light_head_a.png',
    )
    SAXHLEEL_CHAMPION = GearSet(
        name='Saxhleel Champion',
        id=585,
        buffs=[BUFFS.MAJOR_FORCE.value],
        link='https://eso-hub.com/en/sets/saxhleel-champion',
        icon='https://eso-hub.com/storage/icons/gear_rockgrove_heavy_head_a.png',
    )
