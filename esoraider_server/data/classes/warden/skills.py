from esoraider_server.data.classes.general import BUFFS, DEBUFFS
from esoraider_server.data.classes.warden.buffs import WARDEN_BUFFS
from esoraider_server.data.classes.warden.debuffs import WARDEN_DEBUFFS
from esoraider_server.data.core import EsoEnum, Skill


class WARDEN_SKILLS(EsoEnum):
    BLUE_BETTY = Skill(
        name='Blue Betty',
        id=86054,
        buffs=[
            WARDEN_BUFFS.BLUE_BETTY.value,
            BUFFS.MAJOR_BRUTALITY_BLUE_BETTY.value,
            BUFFS.MAJOR_SORCERY_BLUE_BETTY.value,
        ],
        link='https://eso-hub.com/en/skills/warden/animal-companions/blue-betty',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_017.png',
    )
    BULL_NETCH = Skill(
        name='Bull Netch',
        id=86058,
        buffs=[
            WARDEN_BUFFS.BULL_NETCH.value,
            BUFFS.MAJOR_BRUTALITY_BULL_NETCH.value,
            BUFFS.MAJOR_SORCERY_BULL_NETCH.value,
        ],
        link='https://eso-hub.com/en/skills/warden/animal-companions/bull-netch',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_017_b.png',
    )
    FETCHER_INFECTION = Skill(
        name='Fetcher Infection',
        id=86027,
        debuffs=[
            DEBUFFS.MINOR_VULNERABILITY_FETCHER_INFECTION.value,
            WARDEN_DEBUFFS.FETCHER_INFECTION.value,
        ],
        link='https://eso-hub.com/en/skills/warden/animal-companions/fetcher-infection',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_014_a.png',
    )
    GROWING_SWARM = Skill(
        name='Growing Swarm',
        id=86031,
        debuffs=[
            DEBUFFS.MINOR_VULNERABILITY_GROWING_SWARM.value,
            WARDEN_DEBUFFS.GROWING_SWARM.value,
        ],
        link='https://eso-hub.com/en/skills/warden/animal-companions/growing-swarm',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_014_b.png',
    )
    EXPANSIVE_FROST_CLOAK = Skill(
        name='Expansive Frost Cloak',
        id=86126,
        buffs=[BUFFS.MAJOR_RESOLVE_FROST_CLOAK.value],
        link='https://eso-hub.com/en/skills/warden/winters-embrace/expansive-frost-cloak',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_001_a.png',
    )
    ICE_FORTRESS = Skill(
        name='Ice Fortress',
        id=86130,
        buffs=[
            BUFFS.MAJOR_RESOLVE_ICE_FORTRESS.value,
            BUFFS.MINOR_PROTECTION_ICE_FORTRESS.value,
        ],
        link='https://eso-hub.com/en/skills/warden/winters-embrace/ice-fortress',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_001_b.png',
    )
    WINTERS_REVENGE_DAMAGE = Skill(
        name="Winter's Revenge",
        id=88802,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_004_b.png',
    )
    WINTERS_REVENGE = Skill(
        name="Winter's Revenge",
        id=86169,
        children=[WINTERS_REVENGE_DAMAGE],
        link='https://eso-hub.com/en/skills/warden/winters-embrace/winters-revenge',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_004_b.png',
    )
    LOTUS_BLOSSOM = Skill(
        name='Lotus Blossom',
        id=85855,
        buffs=[
            WARDEN_BUFFS.LOTUS_BLOSSOM.value,
            BUFFS.MAJOR_PROPHECY_LOTUS_BLOSSOM.value,
        ],
        link='https://eso-hub.com/en/skills/warden/green-balance/lotus-blossom',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_009_b.png',
    )
