"""Casts / damage done table (dataType: Casts / DamageDone) response."""

from dataclasses import dataclass
from typing import Any, List, Optional

from esologs.responses.common import Gear, Talent
from esologs.responses.core import EsoLogsDataClass


@dataclass
class CastActor(EsoLogsDataClass):
    name: str
    total: int
    type: str

    total_reduced: Optional[int] = None
    id: Optional[int] = None
    guid: Optional[int] = None
    icon: Optional[str] = None
    item_level: Optional[int] = None
    active_time: Optional[int] = None
    active_time_reduced: Optional[int] = None
    overheal: Optional[int] = None
    abilities: Optional[List['CastActor']] = None
    damage_abilities: Optional[List['CastActor']] = None
    targets: Optional[List['CastActor']] = None
    talents: Optional[List[Talent]] = None
    gear: Optional[List[Gear]] = None


@dataclass
class HitDetails(EsoLogsDataClass):
    type: str
    total: int
    count: int
    absorb_or_overheal: int
    min: int
    max: int

    total_reduced: Optional[int] = None
    count_reduced: Optional[int] = None


@dataclass
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
    sources: List[CastActor]
    targets: List[CastActor]

    blockable: Optional[bool] = None
    composite: Optional[bool] = None
    subentries: Optional[List['Cast']] = None
    actor: Optional[int] = None
    actor_name: Optional[str] = None
    actor_icon: Optional[str] = None
    actor_type: Optional[str] = None
    flags: Optional[int] = None
    uptime: Optional[int] = None

    # From Damage Done
    total_reduced: Optional[int] = None
    uses: Optional[int] = None
    hitdetails: Optional[List[HitDetails]] = None
    multistrikedetails: Optional[List[Any]] = None
    missdetails: Optional[List[Any]] = None
    multistrikemissdetails: Optional[List[Any]] = None


@dataclass
class CastsTableData(EsoLogsDataClass):
    entries: List[Cast]
    total_time: int
    log_version: int
    game_version: int
