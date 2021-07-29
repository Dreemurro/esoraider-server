from data.classes.general import BUFFS, DEBUFFS
from data.core import EsoEnum, Skill


class WARDEN_BUFFS(EsoEnum):
    pass


class WARDEN_DEBUFFS(EsoEnum):
    pass


class WARDEN_SKILLS(EsoEnum):
    BLUE_BETTY = Skill(
        name='Blue Betty',
        id=86054,
        buffs=[BUFFS.MAJOR_BRUTALITY.value, BUFFS.MAJOR_SORCERY.value],
        link='https://eso-hub.com/en/skills/warden/animal-companions/blue-betty',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_017.png',
    )
    FETCHER_INFECTION = Skill(
        name='Fetcher Infection',
        id=86027,
        debuffs=[DEBUFFS.MINOR_VULNERABILITY.value],
        link='https://eso-hub.com/en/skills/warden/animal-companions/fetcher-infection',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_014_a.png',
    )
    EXPANSIVE_FROST_CLOAK = Skill(
        name='Expansive Frost Cloak',
        id=86126,
        buffs=[BUFFS.MAJOR_RESOLVE_FROST_CLOAK.value],
        link='https://eso-hub.com/en/skills/warden/winters-embrace/expansive-frost-cloak',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_001_a.png',
    )
