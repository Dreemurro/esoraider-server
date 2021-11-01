from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Tuple


# TODO: Merge Buff and Debuff into Effect?
@dataclass(frozen=True)
class Buff:
    name: str
    id: int

    icon: Optional[str] = None
    advice: Optional[str] = None
    optimal_uptime: Optional[float] = None
    uptime: Optional[float] = None
    stack: Optional['Stack'] = None
    link: Optional[str] = None

    def calculate_uptime(
        self,
        total_uptime: int,
        total_time: int,
        stack: 'Stack' = None,
    ):
        if stack and stack.uptimes:
            return stack.uptimes[stack.max_stacks]
        uptime = total_uptime / total_time * 100
        return round(uptime, 2)


@dataclass(frozen=True)
class Debuff:
    name: str
    id: int

    icon: Optional[str] = None
    advice: Optional[str] = None
    optimal_uptime: Optional[float] = None
    uptime: Optional[float] = None
    stack: Optional['Stack'] = None
    link: Optional[str] = None

    def calculate_uptime(
        self,
        total_uptime: int,
        total_time: int,
        stack: 'Stack' = None,
    ):
        if stack and stack.uptimes:
            return stack.uptimes[stack.max_stacks]
        uptime = total_uptime / total_time * 100
        return round(uptime, 2)


@dataclass(frozen=True)
class Skill:
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Skill):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(('name', self.name, 'id', self.id))

    name: str
    id: int
    icon: str

    link: Optional[str] = None
    buffs: Optional[List[Buff]] = None
    debuffs: Optional[List[Debuff]] = None
    parent: Optional['Skill'] = None
    children: Optional[List['Skill']] = None

    advice: Optional[str] = None
    optimal_uptime: Optional[float] = None
    uptime: Optional[float] = None

    def calculate_uptime(
        self,
        hit_count: int,
        tick_count: int,
        total_time: int,
    ) -> float:
        uptime = (hit_count + tick_count) * 1000.0
        uptime /= float(total_time)
        uptime *= 100.0
        return round(uptime, 2)

    def bumped_uptime(
        self,
        buffs: Optional[List[Buff]] = None,
        debuffs: Optional[List[Debuff]] = None,
        children: Optional[List['Skill']] = None,
    ) -> Optional[float]:
        if children and len(children) == 1:
            uptime = children[0].uptime
        elif buffs and len(buffs) == 1 and not debuffs:
            uptime = buffs[0].uptime
        elif debuffs and len(debuffs) == 1 and not buffs:
            uptime = debuffs[0].uptime
        else:
            uptime = None
        return uptime


@dataclass(frozen=True)
class GearSet:
    name: str
    id: int
    link: str

    uptime: Optional[float] = None
    optimal_uptime: Optional[float] = None
    icon: Optional[str] = None
    buffs: Optional[List[Buff]] = None
    debuffs: Optional[List[Debuff]] = None

    def bumped_uptime(
        self,
        buffs: Optional[List[Buff]] = None,
        debuffs: Optional[List[Debuff]] = None,
    ) -> Optional[float]:
        if buffs and len(buffs) == 1 and not debuffs:
            uptime = buffs[0].uptime
        elif debuffs and len(debuffs) == 1 and not buffs:
            uptime = debuffs[0].uptime
        else:
            uptime = None
        return uptime


@dataclass(frozen=True)
class Glyph:
    name: str
    id: int
    link: str
    icon: str

    buffs: Optional[List[Buff]] = None
    debuffs: Optional[List[Debuff]] = None
    uptime: Optional[float] = None
    advice: Optional[str] = None

    def bumped_uptime(
        self,
        buffs: Optional[List[Buff]] = None,
        debuffs: Optional[List[Debuff]] = None,
    ) -> Optional[float]:
        if buffs and len(buffs) == 1 and not debuffs:
            uptime = buffs[0].uptime
        elif debuffs and len(debuffs) == 1 and not buffs:
            uptime = debuffs[0].uptime
        else:
            uptime = None
        return uptime


@dataclass(frozen=True)
class Stack:
    name: str
    id: int
    icon: str
    max_stacks: int
    type_: str

    buffs: Optional[List[Buff]] = None
    debuffs: Optional[List[Debuff]] = None
    uptimes: Optional[Dict[int, float]] = None


@dataclass(frozen=True)
class Target:
    name: str
    id: Tuple[int]


@dataclass(frozen=True)
class Difficulty:
    name: str
    id: int


@dataclass(frozen=True)
class Encounter:
    name: str
    id: int

    targets: Optional[List[Target]] = None
    difficulties: Optional[List[Difficulty]] = None
    phases: Optional[int] = None


@dataclass(frozen=True)
class Rule:
    name: str
    icon: str

    buffs: Optional[List[Buff]] = None


class EsoEnum(Enum):
    @classmethod
    def _missing_(cls, value):
        # This will allow access by id of a skill / set / buff / etc
        # i.e. BUFFS(40224) will return Skill(name='Aggressive Horn')
        return next(filter(
            lambda x: x.value.id == value, cls.__members__.values(),
        ))
