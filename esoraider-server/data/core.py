from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


@dataclass(frozen=True)
class Buff:
    name: str
    id: int

    icon: Optional[str] = None
    advice: Optional[str] = None
    optimal_uptime: Optional[float] = None
    uptime: Optional[float] = None

    def calculate_uptime(
        self,
        total_uptime: int,
        total_time: int,
    ):
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

    def calculate_uptime(
        self,
        total_uptime: int,
        total_time: int,
    ):
        uptime = total_uptime / total_time * 100
        return round(uptime, 2)


@dataclass(frozen=True)
class Skill:
    def __eq__(self, o: object) -> bool:
        return self.id == o.id

    def __hash__(self) -> int:
        return hash(('name', self.name, 'id', self.id))

    name: str
    id: int

    icon: Optional[str] = None
    buffs: List[Buff] = None
    debuffs: List[Debuff] = None
    link: str = None
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
        uptime = (hit_count + tick_count) * 1000
        uptime /= total_time
        uptime *= 100
        return round(uptime, 2)

    def bumped_uptime(
        self,
        buffs: List[Buff],
        debuffs: List[Debuff],
        children: List['Skill'],
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
    buffs: List[Buff] = None
    debuffs: List[Debuff] = None

    def bumped_uptime(
        self,
        buffs: List[Buff],
        debuffs: List[Debuff],
    ) -> Optional[float]:
        if buffs and len(buffs) == 1 and not debuffs:
            uptime = buffs[0].uptime
        elif debuffs and len(debuffs) == 1 and not buffs:
            uptime = debuffs[0].uptime
        else:
            uptime = None
        return uptime


class EsoEnum(Enum):
    @classmethod
    def _missing_(cls, value):
        # This will allow access by id of a skill / set / buff / etc
        # i.e. BUFFS(40224) will return Skill(name='Aggressive Horn')
        return next(filter(
            lambda x: x.value.id == value, cls.__members__.values(),
        ))
