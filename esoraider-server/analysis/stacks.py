from dataclasses import replace
from itertools import tee
from typing import Dict, List

from api.response import Aura, Band, Series
from data.core import Stack
from portion.interval import Interval, closed


def _pairwise(iterable):
    # s -> (s0,s1), (s1,s2), (s2, s3), ...
    cur, nxt = tee(iterable)
    next(nxt, None)
    return zip(cur, nxt)


def _convert_to_interval(bands: List[Band]) -> Interval:
    return Interval(*[
        closed(band.start_time, band.end_time)
        for band in bands
    ])


def _uptime_from_interval(interval: Interval, total_time: int) -> float:
    total_uptime = sum([atomic.upper - atomic.lower for atomic in interval])
    return round(total_uptime / total_time * 100, 2)


class Stacks(object):
    def __init__(
        self,
        known_stacks: List[Stack],
        char_graphs: List[Series],
        char_buffs: List[Aura],
        char_debuffs: List[Aura],
        total_time: int,
    ) -> None:
        self._known_stacks = known_stacks
        self._char_graphs = char_graphs
        self._char_buffs = char_buffs
        self._char_debuffs = char_debuffs
        self._total_time = total_time
        self.data: List[Stack] = []

    def calculate(self):
        for stack in self._known_stacks:
            uptimes = None
            if not stack.buffs and not stack.debuffs:
                uptimes = self._calculate_uptime_from_graph(stack)
            else:
                uptimes = self._calculate_uptime_from_effects(stack)

            self.data.append(replace(stack, uptimes=uptimes))

    def _calculate_uptime_from_graph(self, stack: Stack) -> Dict[int, float]:
        series = next(
            # Graph response doesn't show which ability ID was requested
            # so will have to get it by other means...
            srs
            for srs in self._char_graphs
            if srs.events[0].ability.guid == stack.id
        )
        intervals = self._calculate_intervals(stack.max_stacks, series.data)
        return self._calculate_stacks_uptimes(intervals)

    def _calculate_uptime_from_effects(self, stack: Stack) -> Dict[int, float]:
        if stack.buffs:
            char_effects = self._char_buffs
            effects_ids = [buff.id for buff in stack.buffs]
        else:
            char_effects = self._char_debuffs
            effects_ids = [debuff.id for debuff in stack.debuffs]

        main_effect = next(eff for eff in char_effects if eff.guid == stack.id)
        effects = [eff for eff in char_effects if eff.guid in effects_ids]

        ordered = sorted(effects, key=lambda ef: ef.total_uptime, reverse=True)

        return self._calculate_complex_stacks_uptimes(
            _convert_to_interval(main_effect.bands),
            [_convert_to_interval(buff.bands) for buff in ordered],
            stack.max_stacks,
        )

    def _calculate_intervals(
        self,
        max_stacks: int,
        stacks_data: List[List[int]],
    ) -> Dict[int, Interval]:
        intervals_dict = {key: Interval() for key in range(1, max_stacks + 1)}
        for cur, nxt in _pairwise(stacks_data):
            interval = closed(cur[0], nxt[0])  # [0] - time, [1] - stack

            # Combine this interval with current stack and stacks below
            for stack in range(1, cur[1] + 1):
                intervals_dict[stack] = intervals_dict[stack].union(interval)
        return intervals_dict

    def _calculate_stacks_uptimes(
        self, intervals: Dict[int, Interval],
    ) -> Dict[int, float]:
        uptimes = {key: 0 for key in intervals.keys()}
        for stack, interval in intervals.items():
            uptimes[stack] = _uptime_from_interval(interval, self._total_time)
        return uptimes

    # Imagine doing all of this just for Z'en...
    def _calculate_complex_stacks_uptimes(
        self,
        effect_with_stacks: Interval,
        effects: List[Interval],
        max_stacks: int,
    ) -> Dict[int, float]:
        # Whole thing is based on debuff uptime intervals
        # Debuffs come in desc order, from highest uptime to lowest
        # Assuming there are 6 debuffs and 5 max stacks:
        # 1x - Just union all debuff intervals
        # 2x - Union 5 debuffs from bottom, then intersect with 1 on top
        # ...
        # 5x - Union 1 debuff from bottom, intersect 5 on top, then intersect
        #      with combined
        # Last step for each stack is to intersect with the main debuff
        # to get final uptime
        calculated_stacks = {}
        for n_stacks in range(1, max_stacks + 1):
            # Not enough debuffs for stack calculation
            if n_stacks > len(effects):
                calculated_stacks[n_stacks] = 0
                continue

            to_union = len(effects) - n_stacks + 1
            effects_intervals = self._combine_and_intersect(
                effects, n_stacks, to_union,
            )

            calculated_stacks[n_stacks] = _uptime_from_interval(
                effects_intervals.intersection(effect_with_stacks),
                self._total_time,
            )
        return calculated_stacks

    def _combine_and_intersect(
        self,
        effects: List[Interval],
        n_stacks: int,
        to_union: int,
    ) -> Interval:
        combined = None
        for to_join in effects[-to_union:]:
            combined = combined.union(to_join) if combined else to_join

        intersected = None
        if n_stacks > 1:
            intersected = effects[0]
            for to_intersect in effects[1:n_stacks - 1]:
                intersected = intersected.intersection(to_intersect)

        if intersected:
            intersected = intersected.intersection(combined)
        else:
            intersected = combined

        return intersected
