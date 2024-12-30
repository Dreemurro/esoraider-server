from esoraider_server.data.classes.general import Buffs, Debuffs
from esoraider_server.data.classes.warden.buffs import WardenBuffs
from esoraider_server.data.classes.warden.debuffs import WardenDebuffs
from esoraider_server.data.core import EsoEnum, Skill


class WardenSkills(EsoEnum):
    BLUE_BETTY = Skill(
        name='Blue Betty',
        id=86054,
        buffs=[
            WardenBuffs.BLUE_BETTY.value,
            Buffs.MAJOR_BRUTALITY_BLUE_BETTY.value,
            Buffs.MAJOR_SORCERY_BLUE_BETTY.value,
        ],
        link='https://eso-hub.com/en/skills/warden/animal-companions/blue-betty',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_017.png',
    )
    BULL_NETCH = Skill(
        name='Bull Netch',
        id=86058,
        buffs=[
            WardenBuffs.BULL_NETCH.value,
            Buffs.MAJOR_BRUTALITY_BULL_NETCH.value,
            Buffs.MAJOR_SORCERY_BULL_NETCH.value,
        ],
        link='https://eso-hub.com/en/skills/warden/animal-companions/bull-netch',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_017_b.png',
    )
    FETCHER_INFECTION = Skill(
        name='Fetcher Infection',
        id=86027,
        debuffs=[
            Debuffs.MINOR_VULNERABILITY_FETCHER_INFECTION.value,
            WardenDebuffs.FETCHER_INFECTION.value,
        ],
        link='https://eso-hub.com/en/skills/warden/animal-companions/fetcher-infection',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_014_a.png',
    )
    GROWING_SWARM = Skill(
        name='Growing Swarm',
        id=86031,
        debuffs=[
            Debuffs.MINOR_VULNERABILITY_GROWING_SWARM.value,
            WardenDebuffs.GROWING_SWARM.value,
        ],
        link='https://eso-hub.com/en/skills/warden/animal-companions/growing-swarm',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_014_b.png',
    )
    EXPANSIVE_FROST_CLOAK = Skill(
        name='Expansive Frost Cloak',
        id=86126,
        buffs=[Buffs.MAJOR_RESOLVE_FROST_CLOAK.value],
        link='https://eso-hub.com/en/skills/warden/winters-embrace/expansive-frost-cloak',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_001_a.png',
    )
    ICE_FORTRESS = Skill(
        name='Ice Fortress',
        id=86130,
        buffs=[
            Buffs.MAJOR_RESOLVE_ICE_FORTRESS.value,
            Buffs.MINOR_PROTECTION_ICE_FORTRESS.value,
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
            WardenBuffs.LOTUS_BLOSSOM.value,
            Buffs.MAJOR_PROPHECY_LOTUS_BLOSSOM.value,
        ],
        link='https://eso-hub.com/en/skills/warden/green-balance/lotus-blossom',
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_warden_009_b.png',
    )
