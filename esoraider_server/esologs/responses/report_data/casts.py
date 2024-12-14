"""Casts / damage done table (dataType: Casts / DamageDone) response."""

from esoraider_server.esologs.responses.common import Gear, Talent
from esoraider_server.esologs.responses.core import EsoLogsDataClass


class CastActor(EsoLogsDataClass):
    name: str
    total: int
    type: str

    total_reduced: int | None = None
    id: int | None = None
    guid: int | None = None
    icon: str | None = None
    item_level: int | None = None
    active_time: int | None = None
    active_time_reduced: int | None = None
    overheal: int | None = None
    abilities: list['CastActor'] | None = None
    damage_abilities: list['CastActor'] | None = None
    targets: list['CastActor'] | None = None
    talents: list[Talent] | None = None
    gear: list[Gear] | None = None


class HitDetails(EsoLogsDataClass):
    type: str
    total: int
    count: int
    absorb_or_overheal: int
    min: int
    max: int

    total_reduced: int | None = None
    count_reduced: int | None = None


class Cast(EsoLogsDataClass):
    name: str
    guid: int
    type: int
    total: int
    ability_icon: str
    hit_count: int
    tick_count: int
    tick_miss_count: int
    miss_count: int
    multistrike_hit_count: int
    multistrike_tick_count: int
    multistrike_miss_count: int
    multistrike_tick_miss_count: int
    crit_hit_count: int
    crit_tick_count: int
    sources: list[CastActor]
    targets: list[CastActor]

    blockable: bool | None = None
    composite: bool | None = None
    subentries: list['Cast'] | None = None
    actor: int | None = None
    actor_name: str | None = None
    actor_icon: str | None = None
    actor_type: str | None = None
    flags: int | None = None
    uptime: int | None = None

    # From Damage Done
    total_reduced: int | None = None
    uses: int | None = None
    hitdetails: list[HitDetails] | None = None
    multistrikedetails: list | None = None
    missdetails: list | None = None
    multistrikemissdetails: list | None = None


class CastsTableData(EsoLogsDataClass):
    entries: list[Cast]
    total_time: int
    log_version: int
    game_version: int
