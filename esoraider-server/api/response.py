from dataclasses import dataclass, field
from typing import Any, List, Optional

from dataclasses_json import DataClassJsonMixin, LetterCase, Undefined, config


@dataclass
class Gear(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    id: int
    slot: int
    quality: int
    icon: str
    champion_points: int
    trait: int
    enchant_type: int
    enchant_quality: int
    set_id: int = field(metadata=config(field_name='setID'))

    name: Optional[str] = None
    type: Optional[int] = None
    set_name: Optional[str] = None


@dataclass
class Talent(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    name: str
    guid: int
    type: int
    ability_icon: str
    flags: int


@dataclass
class CombatantInfo(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    stats: List[Any]
    talents: List[Talent]
    gear: List[Gear]

    spec_ids: Optional[List[Any]] = field(
        default=None,
        metadata=config(field_name='specIDs'),
    )
    artifact: Optional[List[Any]] = None

    def skill_ids(self):
        return [t.guid for t in self.talents]


@dataclass
class PlayerDetails(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    name: str
    id: int
    guid: int
    type: str
    server: str
    display_name: str
    anonymous: bool
    icon: str
    specs: List[str]
    min_item_level: int
    max_item_level: int
    combatant_info: CombatantInfo


@dataclass
class PlayerDetailsBySpec(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    dps: Optional[List[PlayerDetails]] = None
    healers: Optional[List[PlayerDetails]] = None
    tanks: Optional[List[PlayerDetails]] = None


@dataclass
class DoneByAbility(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    name: str
    guid: int
    type: int
    ability_icon: str
    total: int

    composite: Optional[bool] = None
    flags: Optional[int] = None


@dataclass
class DeathFromAbility(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    name: str
    guid: int
    type: int
    ability_icon: str
    flags: int


@dataclass
class DeathEvent(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    name: str
    id: int
    guid: int
    type: str
    icon: str
    death_time: int
    ability: DeathFromAbility


@dataclass
class DoneByChar(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    name: str
    guid: int
    type: str
    total: int

    id: Optional[int] = None
    icon: Optional[str] = None
    ability_icon: Optional[str] = None
    composite: Optional[bool] = None
    flags: Optional[int] = None


@dataclass
class Spec(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    spec: str
    role: str


@dataclass
class Composition(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    name: str
    id: int
    guid: int
    type: str
    specs: List[Spec]


"""
    Summary Table
"""


@dataclass
class SummaryTableData(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    total_time: int
    item_level: float
    log_version: int
    game_version: int
    composition: List[Composition]
    damage_done: List[DoneByChar]
    healing_done: List[DoneByChar]
    damage_taken: List[DoneByAbility]
    death_events: List[DeathEvent]

    combatant_info: Optional[CombatantInfo] = None
    player_details: Optional[PlayerDetailsBySpec] = None


"""
    Buffs / Debuffs Table
"""


@dataclass
class Band(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    start_time: int
    end_time: int


@dataclass
class Aura(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    name: str
    guid: int
    type: int
    ability_icon: str
    flags: int
    total_uptime: int
    total_uses: int
    bands: List[Band]


@dataclass
class BuffsTableData(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    auras: List[Aura]
    use_targets: bool
    total_time: int
    start_time: int
    end_time: int

    category: Optional[int] = None


"""
    Casts Table
"""


@dataclass
class CastActor(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

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
class HitDetails(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    type: str
    total: int
    count: int
    absorb_or_overheal: int
    min: int
    max: int

    total_reduced: Optional[int] = None
    count_reduced: Optional[int] = None


@dataclass
class Cast(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

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
class CastsTableData(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    # entries: Union[List[Cast], List[CastActor]]
    entries: List[Cast]
    total_time: int
    log_version: int
    game_version: int


"""
    Graph
"""


@dataclass
class Event(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    timestamp: int
    type: str
    source_id: int = field(metadata=config(field_name='sourceID'))
    source_is_friendly: bool
    target_id: int = field(metadata=config(field_name='targetID'))
    target_is_friendly: bool
    ability: Talent
    fight: int

    stack: Optional[int] = None
    target_instance: Optional[int] = None


def skip_events(items: List) -> List[Event]:
    final = []
    for item in items:
        if isinstance(item, list):
            continue
        if item.get('type') == 'combatantinfo':
            continue
        final.append(item)
    return [Event.from_dict(item) for item in final]


@dataclass
class Series(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    name: str
    id: int
    guid: int
    type: str
    # 0 - time, 1 - stack
    data: List[List[int]]  # noqa: WPS110
    events: List[Event] = field(metadata=config(
        # First and last elements are empty lists for some reason
        # + there is an occasional combatantinfo in there
        # Skipping such stuff for now
        decoder=skip_events,
    ))


@dataclass
class GraphData(DataClassJsonMixin):
    dataclass_json_config = config(  # type: ignore
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']

    series: List[Series]
    start_time: int
    end_time: int
    use_targets: bool
