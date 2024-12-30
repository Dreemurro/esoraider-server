from esoraider_server.data.core import Buff, EsoEnum


class WardenPassives(EsoEnum):
    # Animal Companions
    BOND_WITH_NATURE = Buff(
        name='Bond With Nature',
        id=86065,
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_warden_010.png',
        link='https://eso-hub.com/en/skills/warden/animal-companions/bond-with-nature',
    )
    SAVAGE_BEAST = Buff(
        name='Savage Beast',
        id=86063,
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_warden_009.png',
        link='https://eso-hub.com/en/skills/warden/animal-companions/savage-beast',
    )
    FLOURISH = Buff(
        name='Flourish',
        id=86067,
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_warden_012.png',
        link='https://eso-hub.com/en/skills/warden/animal-companions/flourish',
    )
    ADVANCED_SPECIES = Buff(
        name='Advanced Species',
        id=86069,
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_warden_011.png',
        link='https://eso-hub.com/en/skills/warden/animal-companions/advanced-species',
    )

    # Green Balance
    ACCELERATED_GROWTH = Buff(
        name='Accelerated Growth',
        id=85883,
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_warden_008.png',
        link='https://eso-hub.com/en/skills/warden/green-balance/accelerated-growth',
    )
    NATURES_GIFT = Buff(
        name="Nature's Gift",
        id=85879,
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_warden_006.png',
        link='https://eso-hub.com/en/skills/warden/green-balance/natures-gift',
    )
    EMERALD_MOSS = Buff(
        name='Emerald Moss',
        id=85877,
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_warden_005.png',
        link='https://eso-hub.com/en/skills/warden/green-balance/emerald-moss',
    )
    MATURATION = Buff(
        name='Maturation',
        id=85881,
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_warden_007.png',
        link='https://eso-hub.com/en/skills/warden/green-balance/maturation',
    )

    # Winter's Embrace
    ICY_AURA = Buff(
        name='Icy Aura',
        id=86194,
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_warden_003.png',
        link='https://eso-hub.com/en/skills/warden/winters-embrace/icy-aura',
    )
    PIERCING_COLD = Buff(
        name='Piercing Cold',
        id=86196,
        icon='https://assets.rpglogs.com/img/eso/abilities/passive_warden_004.png',
        link='https://eso-hub.com/en/skills/warden/winters-embrace/piercing-cold',
    )
