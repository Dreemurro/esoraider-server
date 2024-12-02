"""Uptimes calculation of stackable buffs & debuffs."""

from dataclasses import replace
from itertools import tee
from typing import Callable, Dict, List, Optional

from portion.interval import Interval, closed  # type: ignore
from structlog.stdlib import get_logger

from esoraider_server.data.core import Stack
from esoraider_server.esologs.responses.report_data.effects import Aura, Band
from esoraider_server.esologs.responses.report_data.graph import Series

logger = get_logger()


def _pairwise(iterable):
    # s -> (s0,s1), (s1,s2), (s2, s3), ...
    cur, nxt = tee(iterable)
    next(nxt, None)
    return zip(cur, nxt)


def _convert_to_interval(bands: Optional[List[Band]] = None) -> Interval:
    if not bands:
        return closed()
    return Interval(*[
        closed(band.start_time, band.end_time)
        for band in bands
    ])


def _uptime_from_interval(interval: Interval, total_time: int) -> float:
    if interval.empty:
        return float(0)
    total_uptime = sum([atomic.upper - atomic.lower for atomic in interval])
    return round(total_uptime / total_time * 100, 2)


class Stacks(object):
    """Uptimes calculation of stackable buffs & debuffs."""

    def __init__(
        self,
        known_stacks: List[Stack],
        char_graphs: Dict[int, List[Series]],
        char_buffs: List[Aura],
        char_debuffs: List[Aura],
        total_time: int,
    ) -> None:
        self._known_stacks = known_stacks
        self._char_graphs = char_graphs
        self._char_buffs = char_buffs
        self._char_debuffs = char_debuffs
        self._total_time = total_time
        self.calculated: List[Stack] = []

    def calculate(self):
        """Calculate stacks uptimes."""
        logger.info('Calculating stacks uptimes')
        for stack in self._known_stacks:
            if not stack.buffs and not stack.debuffs:
                uptimes = self._calculate_uptime_from_graph(stack)
            elif stack.buffs or stack.debuffs:
                uptimes = self._calculate_uptime_from_effects(stack)
            else:
                uptimes = None

            self.calculated.append(replace(stack, uptimes=uptimes))

    def _calculate_uptime_from_graph(self, stack: Stack) -> Dict[int, float]:
        series_list = self._char_graphs[stack.id]

        intervals = self._calculate_intervals(
            stack.max_stacks, series_list, stack.modifier,
        )
        return self._calculate_stacks_uptimes(intervals)

    def _calculate_uptime_from_effects(self, stack: Stack) -> Dict[int, float]:
        char_effects = []
        effects_ids = []

        if stack.buffs:
            char_effects = self._char_buffs
            effects_ids = [buff.id for buff in stack.buffs]
        elif stack.debuffs:
            char_effects = self._char_debuffs
            effects_ids = [debuff.id for debuff in stack.debuffs]

        try:
            main_effect = next(
                eff
                for eff in char_effects
                if eff.guid == stack.id
            )
        except StopIteration:
            logger.error(
                "Effect of '{0}' was not found. ".format(stack.name)
                + "It's probably because of an incomplete set",
            )
            return {0: float(0)}

        effects = [eff for eff in char_effects if eff.guid in effects_ids]

        ordered = sorted(
            effects,
            key=lambda ef: ef.total_uptime or 0,
            reverse=True,
        )

        return self._calculate_complex_stacks_uptimes(
            _convert_to_interval(main_effect.bands),
            [_convert_to_interval(buff.bands) for buff in ordered],
            stack.max_stacks,
        )

    def _calculate_intervals(
        self,
        max_stacks: int,
        series_list: List[Series],
        modifier: Optional[Callable[[int], int]] = None,
    ) -> Dict[int, Interval]:
        intervals = {key: Interval() for key in range(1, max_stacks + 1)}
        stacks_list = [series.data for series in series_list]
        for stack_data in stacks_list:
            for cur, nxt in _pairwise(stack_data):
                interval = closed(cur[0], nxt[0])  # [0] - time, [1] - stack

                # Combine this interval with current stack and stacks below
                stack_n = modifier(cur[1]) if modifier else cur[1]
                for stack in range(1, stack_n + 1):
                    intervals[stack] = intervals[stack].union(interval)
        return intervals

    def _calculate_stacks_uptimes(
        self, intervals: Dict[int, Interval],
    ) -> Dict[int, float]:
        uptimes = {key: float(0) for key in intervals.keys()}
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
        calculated_stacks: Dict[int, float] = {}
        for n_stacks in range(1, max_stacks + 1):
            # Not enough debuffs for stack calculation
            if n_stacks > len(effects):
                calculated_stacks[n_stacks] = float(0)
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
        combined = Interval()
        for to_join in effects[-to_union:]:
            combined = combined.union(to_join)

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
