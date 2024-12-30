from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Sequence

    from esoraider_server.esologs.consts import DataType


# TODO: Merge Buff and Debuff into Effect?
@dataclass(frozen=True)
class Buff:
    name: str
    id: int

    icon: str | None = None
    advice: str | None = None
    optimal_uptime: float | None = None
    uptime: float | None = None
    stack: 'Stack | None' = None
    link: str | None = None

    def calculate_uptime(
        self,
        total_uptime: int,
        total_time: int,
        stack: 'Stack | None' = None,
    ):
        if stack and stack.uptimes:
            return stack.uptimes[stack.max_stacks]
        uptime = total_uptime / total_time * 100
        return round(uptime, 2)


@dataclass(frozen=True)
class Debuff:
    name: str
    id: int

    icon: str | None = None
    advice: str | None = None
    optimal_uptime: float | None = None
    uptime: float | None = None
    stack: 'Stack | None' = None
    link: str | None = None

    def calculate_uptime(
        self,
        total_uptime: int,
        total_time: int,
        stack: 'Stack | None' = None,
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

    link: str | None = None
    buffs: list[Buff] | None = None
    debuffs: list[Debuff] | None = None
    parent: 'Skill | None' = None
    children: list['Skill'] | None = None

    tick: int = 1
    advice: str | None = None
    optimal_uptime: float | None = None
    uptime: float | None = None

    def calculate_uptime(
        self,
        hit_count: int,
        tick_count: int,
        total_time: int,
    ) -> float:
        uptime = (hit_count + tick_count) * self.tick * 1000.0
        uptime /= float(total_time)
        uptime *= 100.0
        return round(uptime, 2)

    def bumped_uptime(
        self,
        buffs: list[Buff] | None = None,
        debuffs: list[Debuff] | None = None,
        children: list['Skill'] | None = None,
    ) -> float | None:
        if children and len(children) == 1:
            uptime = children[0].uptime
        elif self.uptime:
            uptime = self.uptime
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

    uptime: float | None = None
    optimal_uptime: float | None = None
    icon: str | None = None
    buffs: list[Buff] | None = None
    debuffs: list[Debuff] | None = None

    def bumped_uptime(
        self,
        buffs: list[Buff] | None = None,
        debuffs: list[Debuff] | None = None,
    ) -> float | None:
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

    buffs: list[Buff] | None = None
    debuffs: list[Debuff] | None = None
    uptime: float | None = None
    advice: str | None = None

    def bumped_uptime(
        self,
        buffs: list[Buff] | None = None,
        debuffs: list[Debuff] | None = None,
    ) -> float | None:
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
    type_: 'DataType'

    buffs: list[Buff] | None = None
    debuffs: list[Debuff] | None = None
    modifier: 'Callable[[int], int] | None' = None
    uptimes: dict[int, float] | None = None


@dataclass(frozen=True)
class Target:
    name: str
    id: 'Sequence[int]'


@dataclass(frozen=True)
class Difficulty:
    name: str
    id: int


@dataclass(frozen=True)
class Encounter:
    name: str
    id: int

    targets: list[Target] | None = None
    difficulties: list[Difficulty] | None = None
    phases: int | None = None


@dataclass(frozen=True)
class Rule:
    name: str
    icon: str

    required: list[Skill] | None = None

    buffs: list[Buff] | None = None

    @property
    def required_ids(self):
        return [skill.id for skill in self.required]


# FIXME: Search takes O(n) time, use a dict instead?
class EsoEnum(Enum):
    @classmethod
    def _missing_(cls, value):
        # This will allow access by id of a skill / set / buff / etc
        # i.e. BUFFS(40224) will return Skill(name='Aggressive Horn')
        return next(
            filter(lambda x: x.value.id == value, cls.__members__.values())
        )
