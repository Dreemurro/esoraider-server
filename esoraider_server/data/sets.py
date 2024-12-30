from esoraider_server.data.buffs import Buffs
from esoraider_server.data.core import EsoEnum, GearSet
from esoraider_server.data.debuffs import Debuffs
from esoraider_server.data.stacks import BuffsWithStacks, DebuffsWithStacks


class GearSets(EsoEnum):
    PERFECTED_CRUSHING_WALL = GearSet(
        name='Perfected Crushing Wall',
        id=526,
        buffs=[Buffs.CRUSHING_WALL.value],
        link='https://eso-hub.com/en/sets/perfected-crushing-wall',
        icon='https://eso-hub.com/storage/icons/gear_dwarvenscavenged_staff_a.png',
    )
    CRUSHING_WALL = GearSet(
        name='Crushing Wall',
        id=373,
        buffs=[Buffs.CRUSHING_WALL.value],
        link='https://eso-hub.com/en/sets/crushing-wall',
        icon='https://eso-hub.com/storage/icons/gear_dwarvenscavenged_staff_a.png',
    )
    HARPOONERS_WADING_KILT = GearSet(
        name="Harpooner's Wading Kilt",
        id=594,
        buffs=[BuffsWithStacks.HUNTERS_FOCUS.value],
        link='https://eso-hub.com/en/sets/harpooners-wading-kilt',
        icon='https://eso-hub.com/storage/icons/gear_kothringikilt_a.png',
    )
    ELEMENTAL_CATALYST = GearSet(
        name='Elemental Catalyst',
        id=516,
        debuffs=[
            Debuffs.FROST_WEAKNESS.value,
            Debuffs.FLAME_WEAKNESS.value,
            Debuffs.SHOCK_WEAKNESS.value,
        ],
        link='https://eso-hub.com/en/sets/elemental-catalyst',
        icon='https://eso-hub.com/storage/icons/gear_northlandsalchlgt_head_a.png',
    )
    PERFECTED_CLAW_OF_YOLNAHKRIIN = GearSet(
        name='Perfected Claw of Yolnahkriin',
        id=451,
        buffs=[Buffs.MINOR_COURAGE.value],
        link='https://eso-hub.com/en/sets/perfected-claw-of-yolnahkriin',
        icon='https://eso-hub.com/storage/icons/gear_sunspire_heavy_helmet_a.png',
    )
    ENCRATISS_BEHEMOTH = GearSet(
        name="Encratis's Behemoth",
        id=577,
        buffs=[Buffs.BEHEMOTHS_AURA.value],
        link='https://eso-hub.com/en/sets/encratiss-behemoth',
        icon='https://eso-hub.com/storage/icons/gear_undfiregiant_head_a.png',
    )
    SPELL_POWER_CURE = GearSet(
        name='Spell Power Cure',
        id=185,
        buffs=[Buffs.MAJOR_COURAGE_SPELL_POWER_CURE.value],
        link='https://eso-hub.com/en/sets/spell-power-cure',
        icon='https://eso-hub.com/storage/icons/gear_imperialdaedric_light_head_a.png',
    )
    MASTER_ARCHITECT = GearSet(
        name='Master Architect',
        id=332,
        buffs=[Buffs.MAJOR_SLAYER_MASTER_ARCHITECT.value],
        link='https://eso-hub.com/en/sets/master-architect',
        icon='https://eso-hub.com/storage/icons/gear_clockwork_light_head_a.png',
    )
    SAXHLEEL_CHAMPION = GearSet(
        name='Saxhleel Champion',
        id=585,
        buffs=[Buffs.MAJOR_FORCE_SAXHLEEL_CHAMPION.value],
        link='https://eso-hub.com/en/sets/saxhleel-champion',
        icon='https://eso-hub.com/storage/icons/gear_rockgrove_heavy_head_a.png',
    )
    PERFECTED_SAXHLEEL_CHAMPION = GearSet(
        name='Perfected Saxhleel Champion',
        id=589,
        buffs=[Buffs.MAJOR_FORCE_SAXHLEEL_CHAMPION.value],
        link='https://eso-hub.com/en/sets/perfected-saxhleel-champion',
        icon='https://eso-hub.com/storage/icons/gear_rockgrove_heavy_head_a.png',
    )
    POWERFULL_ASSAULT = GearSet(
        name='Powerful Assault',
        id=180,
        buffs=[Buffs.POWERFUL_ASSAULT.value],
        link='https://eso-hub.com/en/sets/powerful-assault',
        icon='https://eso-hub.com/storage/icons/gear_breton_medium_head_d.png',
    )
    WAY_OF_MARTIAL_KNOWLEDGE = GearSet(
        name='Way of Martial Knowledge',
        id=147,
        debuffs=[Debuffs.WAY_OF_MARTIAL_KNOWLEDGE.value],
        link='https://eso-hub.com/en/sets/way-of-martial-knowledge',
        icon='https://eso-hub.com/storage/icons/gear_yokudan_light_head_a.png',
    )
    ZENS_REDRESS = GearSet(
        name="Z'en's Redress",
        id=455,
        debuffs=[DebuffsWithStacks.TOUCH_OF_ZEN.value],
        link='https://eso-hub.com/en/sets/zens-redress',
        icon='https://eso-hub.com/storage/icons/gear_stagzenlgt_helmet_a.png',
    )
    DIAMONDS_VICTORY = GearSet(
        name="Diamond's Victory",
        id=584,
        buffs=[Buffs.MELEE_SUPREMACY.value, Buffs.RANGE_SUPREMACY.value],
        link='https://eso-hub.com/en/sets/diamonds-victory',
        icon='https://eso-hub.com/storage/icons/gear_breton_light_head_d.png',
    )
    ROAR_OF_ALKOSH = GearSet(
        name='Roar of Alkosh',
        id=232,
        debuffs=[Debuffs.ROAR_OF_ALKOSH.value, Debuffs.LINE_BREAKER.value],
        link='https://eso-hub.com/en/sets/roar-of-alkosh',
        icon='https://eso-hub.com/storage/icons/gear_dromathra_medium_head_a.png',
    )
    WAR_MACHINE = GearSet(
        name='War Machine',
        id=331,
        buffs=[Buffs.MAJOR_SLAYER.value],
        link='https://eso-hub.com/en/sets/war-machine',
        icon='https://eso-hub.com/storage/icons/gear_clockwork_medium_head_a.png',
    )
    ROARING_OPPORTUNIST = GearSet(
        name='Roaring Opportunist',
        id=496,
        buffs=[Buffs.MAJOR_SLAYER_ROARING_OPPORTUNIST.value],
        link='https://eso-hub.com/en/sets/roaring-opportunist',
        icon='https://eso-hub.com/storage/icons/gear_seagiantlgt_helmet.png',
    )
    PERFECTED_ROARING_OPPORTUNIST = GearSet(
        name='Perfected Roaring Opportunist',
        id=497,
        buffs=[Buffs.MAJOR_SLAYER_ROARING_OPPORTUNIST.value],
        link='https://eso-hub.com/en/sets/perfected-roaring-opportunist',
        icon='https://eso-hub.com/storage/icons/gear_seagiantlgt_helmet.png',
    )
    PERFECTED_CAUSTIC_ARROW = GearSet(
        name='Perfected Caustic Arrow',
        id=531,
        buffs=[Buffs.CAUSTIC_ARROW.value],
        link='https://eso-hub.com/en/sets/perfected-caustic-arrow',
        icon='https://eso-hub.com/storage/icons/gear_bosmer_bow_e.png',
    )
    PERFECTED_VIRULENT_SHOT = GearSet(
        name='Perfected Virulent Shot',
        id=426,
        buffs=[Buffs.VIRULENT_SHOT.value],
        link='https://eso-hub.com/en/sets/perfected-virulent-shot',
        icon='https://eso-hub.com/storage/icons/gear_honorguard_bow_a.png',
    )
    THE_MORAG_TONG = GearSet(
        name='The Morag Tong',
        id=50,
        debuffs=[Debuffs.THE_MORAG_TONG.value],
        link='https://eso-hub.com/en/sets/the-morag-tong',
        icon='https://eso-hub.com/storage/icons/gear_breton_medium_head_d.png',
    )
    TREMORSCALE = GearSet(
        name='Tremorscale',
        id=276,
        debuffs=[Debuffs.TREMORSCALE.value],
        link='https://eso-hub.com/en/sets/tremorscale',
        icon='https://eso-hub.com/storage/icons/gear_undauntedsuneripper_head_a.png',
    )
    PERFECTED_WRATH_OF_ELEMENTS = GearSet(
        name='Perfected Wrath of Elements',
        id=567,
        # Not activated yet, requires stacks tracking
        # buffs=[BUFFS.WRATH_OF_ELEMENTS.value],
        debuffs=[Debuffs.WRATH_OF_ELEMENTS.value],
        link='https://eso-hub.com/en/sets/perfected-wrath-of-elements',
        icon='https://eso-hub.com/storage/icons/gear_reachv2_staff_a.png',
    )
    # TODO: Shown uptime is on set user only, it's not group wide uptime
    PERFECTED_VESTMENT_OF_OLORIME = GearSet(
        name='Perfected Vestment of Olorime',
        id=395,
        buffs=[Buffs.MAJOR_COURAGE_OLORIME.value],
        link='https://eso-hub.com/en/sets/perfected-vestment-of-olorime',
        icon='https://eso-hub.com/storage/icons/gear_welkynar_light_head_a.png',
    )
    SPECTRAL_CLOAK = GearSet(
        name='Spectral Cloak',
        id=413,
        buffs=[Buffs.SPECTRAL_CLOAK.value],
        link='https://eso-hub.com/en/sets/spectral-cloak',
        icon='https://eso-hub.com/storage/icons/gear_honorguard_1hsword_a.png',
    )
    PERFECTED_SPECTRAL_CLOAK = GearSet(
        name='Perfected Spectral Cloak',
        id=425,
        buffs=[Buffs.SPECTRAL_CLOAK.value],
        link='https://eso-hub.com/en/sets/perfected-spectral-cloak',
        icon='https://eso-hub.com/storage/icons/gear_honorguard_1hsword_a.png',
    )
    GOSSAMER = GearSet(
        name='Gossamer',
        id=261,
        buffs=[Buffs.MAJOR_EVASION_GOSSAMER.value],
        link='https://eso-hub.com/en/sets/gossamer',
        icon='https://eso-hub.com/storage/icons/gear_kothringi_light_head_a.png',
    )
    ARMS_OF_RELEQUEN = GearSet(
        name='Arms of Relequen',
        id=389,
        debuffs=[DebuffsWithStacks.ARMS_OF_RELEQUEN.value],
        link='https://eso-hub.com/en/sets/arms-of-relequen',
        icon='https://eso-hub.com/storage/icons/gear_welkynar_medium_head_a.png',
    )
    PERFECTED_ARMS_OF_RELEQUEN = GearSet(
        name='Perfected Arms of Relequen',
        id=393,
        debuffs=[DebuffsWithStacks.ARMS_OF_RELEQUEN.value],
        link='https://eso-hub.com/en/sets/perfected-arms-of-relequen',
        icon='https://eso-hub.com/storage/icons/gear_welkynar_medium_head_a.png',
    )
    MANTLE_OF_SIRORIA = GearSet(
        name='Mantle of Siroria',
        id=390,
        buffs=[BuffsWithStacks.SIRORIAS_BOON.value],
        link='https://eso-hub.com/en/sets/mantle-of-siroria',
        icon='https://eso-hub.com/storage/icons/gear_welkynar_light_head_a.png',
    )
    PERFECTED_MANTLE_OF_SIRORIA = GearSet(
        name='Perfected Mantle of Siroria',
        id=394,
        buffs=[BuffsWithStacks.SIRORIAS_BOON.value],
        link='https://eso-hub.com/en/sets/perfected-mantle-of-siroria',
        icon='https://eso-hub.com/storage/icons/gear_welkynar_light_head_a.png',
    )
    BERSERKING_WARRIOR = GearSet(
        name='Berserking Warrior',
        id=137,
        buffs=[BuffsWithStacks.BERSERKING_WARRIOR.value],
        link='https://eso-hub.com/en/sets/berserking-warrior',
        icon='https://eso-hub.com/storage/icons/gear_craglorn_heavy_head_a.png',
    )
    PERFECTED_DESTRUCTIVE_IMPACT = GearSet(
        name='Perfected Destructive Impact',
        id=532,
        buffs=[Buffs.DESTRUCTIVE_IMPACT.value],
        link='https://eso-hub.com/en/sets/perfected-destructive-impact',
        icon='https://eso-hub.com/storage/icons/gear_nord_staff_e.png',
    )
    SPAULDER_OF_RUIN = GearSet(
        name='Spaulder of Ruin',
        id=627,
        buffs=[BuffsWithStacks.PRICE_OF_PRIDE.value],
        link='https://eso-hub.com/en/sets/spaulder-of-ruin',
        icon='https://eso-hub.com/storage/icons/gear_razorhorndaedric_shoulder_a.png',
    )
    KINRAS_WRATH = GearSet(
        name="Kinras's Wrath",
        id=570,
        buffs=[  # Also has stacking buff Burning Heart (150750)
            Buffs.KINRAS_WRATH.value,
            Buffs.MAJOR_BERSERK_KINRAS_WRATH.value,
        ],
        link='https://eso-hub.com/en/sets/kinrass-wrath',
        icon='https://eso-hub.com/storage/icons/gear_blackdrakevilla_med_head_a.png',
    )
    PERFECTED_FORCE_OVERFLOW = GearSet(
        name='Perfected Force Overflow',
        id=568,
        buffs=[Buffs.FORCE_OVERFLOW.value],
        link='https://eso-hub.com/en/sets/perfected-force-overflow',
        icon='https://eso-hub.com/storage/icons/gear_reachv2_staff_a.png',
    )
    CRIMSON_OATHS_RIVE = GearSet(
        name="Crimson Oath's Rive",
        id=602,
        debuffs=[Debuffs.CRIMSON_OATHS_RIVE.value],
        link='https://eso-hub.com/en/sets/crimson-oaths-rive',
        icon='https://eso-hub.com/storage/icons/gear_blackironhvy_head_a.webp',
    )
    THUNDEROUS_VOLLEY = GearSet(
        name='Thunderous Volley',
        id=372,
        buffs=[BuffsWithStacks.THUNDEROUS_VOLLEY.value],
        link='https://eso-hub.com/en/sets/thunderous-volley',
        icon='https://eso-hub.com/storage/icons/gear_dwarvenscavenged_bow_a.webp',
    )
    PERFECTED_THUNDEROUS_VOLLEY = GearSet(
        name='Perfected Thunderous Volley',
        id=525,
        buffs=[BuffsWithStacks.THUNDEROUS_VOLLEY.value],
        link='https://eso-hub.com/en/sets/perfected-thunderous-volley',
        icon='https://eso-hub.com/storage/icons/gear_dwarvenscavenged_bow_a.webp',
    )
    BAHSEIS_MANIA = GearSet(
        name="Bahsei's Mania",
        id=587,
        buffs=[BuffsWithStacks.BAHSEIS_MANIA.value],
        link='https://eso-hub.com/en/sets/bahseis-mania',
        icon='https://eso-hub.com/storage/icons/gear_rockgrove_lgt_head_a.webp',
    )
    PERFECTED_BAHSEIS_MANIA = GearSet(
        name="Perfected Bahsei's Mania",
        id=591,
        buffs=[BuffsWithStacks.BAHSEIS_MANIA.value],
        link='https://eso-hub.com/en/sets/perfected-bahseis-mania',
        icon='https://eso-hub.com/storage/icons/gear_rockgrove_lgt_head_a.webp',
    )
    DRAKES_RUSH = GearSet(
        name="Drake's Rush",
        id=571,
        buffs=[Buffs.MAJOR_HEROISM_DRAKES_RUSH.value],
        link='https://eso-hub.com/en/sets/drakes-rush',
        icon='https://eso-hub.com/storage/icons/gear_blackdv_hvy_head_a.webp',
    )
    TZOGVINS_WARBAND = GearSet(
        name="Tzogvin's Warband",
        id=430,  # Has stacks (116742) but its not really needed
        buffs=[Buffs.MINOR_FORCE_TZOGVINS_WARBAND.value],
        link='https://eso-hub.com/en/sets/tzogvins-warband',
        icon='https://eso-hub.com/storage/icons/gear_coldsnap_medium_head_a.webp',
    )
    PERFECTED_SUL_XANS_TORMENT = GearSet(
        name="Perfected Sul-Xan's Torment",
        id=590,
        buffs=[Buffs.SUL_XAN_SOULBOUND.value],
        link='https://eso-hub.com/en/sets/perfected-sul-xans-torment',
        icon='https://eso-hub.com/storage/icons/gear_rockgrove_med_head_a.webp',
    )
    TRUE_SWORN_FURY = GearSet(
        name='True-Sworn Fury',
        id=569,
        buffs=[BuffsWithStacks.TRUE_SWORN_FURY.value],
        link='https://eso-hub.com/en/sets/true-sworn-fury',
        icon='https://eso-hub.com/storage/icons/gear_blackdrakevilla_lgt_head_a.webp',
    )
    BURNING_SPELLWEAVE = GearSet(
        name='Burning Spellweave',
        id=160,
        buffs=[Buffs.BURNING_SPELLWEAVE.value],
        link='https://eso-hub.com/en/sets/burning-spellweave',
        icon='https://eso-hub.com/storage/icons/gear_daedric_light_head_a.webp',
    )
