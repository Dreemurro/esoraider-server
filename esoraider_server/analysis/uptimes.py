"""Uptimes calculation."""

from dataclasses import replace
from typing import TYPE_CHECKING, overload

from structlog.stdlib import get_logger

from esoraider_server.analysis.stacks import Stacks
from esoraider_server.data.core import Buff, Debuff, GearSet, Glyph, Skill
from esoraider_server.esologs.responses.report_data.casts import Cast
from esoraider_server.esologs.responses.report_data.effects import Aura

if TYPE_CHECKING:
    from esoraider_server.analysis.data_request import DataRequest
    from esoraider_server.analysis.tracked_info import TrackedInfo
    from esoraider_server.data.core import Stack
    from esoraider_server.esologs.responses.report_data.graph import Series

logger = get_logger()


class Uptimes:
    """Uptimes calculation based on provided info.

    Uptimes are calculated for skills, sets, glyphs, buffs & debuffs and their
    stacks
    """

    def __init__(
        self,
        tracked_info: 'TrackedInfo',
        requested_info: 'DataRequest',
        char_buffs: list[Aura],
        char_debuffs: list[Aura],
        char_graphs: dict[int, list['Series']],
    ) -> None:
        self.skills: list[Skill] = []
        self.sets: list[GearSet] = []
        self.glyphs: list[Glyph] = []
        self.buffs: list[Buff] = []
        self.debuffs: list[Debuff] = []
        self._stacks: list[Stack] = []

        self._requested = requested_info
        self._tracked = tracked_info

        self._char_buffs = char_buffs
        self._char_debuffs = char_debuffs
        self._char_graphs = char_graphs

    def calculate(self):
        """Calculate uptimes based on provided data."""
        logger.info('Calculating uptimes')

        if not self._char_buffs and not self._char_debuffs:
            self.buffs = self._calculate_effects_uptimes(
                self._tracked.buffs, self._requested.buffs_table.auras
            )
            self.debuffs = self._calculate_effects_uptimes(
                self._tracked.debuffs, self._requested.debuffs_table.auras
            )
            return

        stacks = Stacks(
            known_stacks=self._tracked.stacks,
            char_graphs=self._char_graphs,
            char_buffs=self._char_buffs,
            char_debuffs=self._char_debuffs,
            total_time=self._requested.total_time,
        )
        stacks.calculate()
        self._stacks = stacks.calculated
        for _ in self._stacks:
            logger.debug(f'{_.name} - {_.uptimes}')

        self.skills = self._uptimes_of(self._tracked.skills)
        self.sets = self._uptimes_of(self._tracked.sets)
        self.glyphs = self._uptimes_of(self._tracked.glyphs)

    def _uptimes_of(self, eso_items):
        new_items = []
        for eso_item in eso_items:
            new_item = self._calculate_item_uptimes(eso_item)
            new_items.append(new_item)
            logger.debug(f'{new_item.name} - {new_item.uptime}')
        return new_items

    @overload
    def _calculate_item_uptimes(self, eso_item: Skill) -> Skill: ...

    @overload
    def _calculate_item_uptimes(self, eso_item: GearSet) -> GearSet: ...

    @overload
    def _calculate_item_uptimes(self, eso_item: Glyph) -> Glyph: ...

    def _calculate_item_uptimes(self, eso_item):
        new_buffs = (
            self._calculate_effects_uptimes(eso_item.buffs, self._char_buffs)
            if eso_item.buffs
            else None
        )
        new_debuffs = (
            self._calculate_effects_uptimes(
                eso_item.debuffs, self._char_debuffs
            )
            if eso_item.debuffs
            else None
        )

        new_children: list[Skill] = []
        if isinstance(eso_item, Skill):
            new_children = self._calculate_skill_children_uptimes(eso_item)

        new_uptime = self._set_parent_uptime(
            eso_item, new_buffs, new_debuffs, new_children
        )

        if isinstance(eso_item, Skill):
            return replace(
                eso_item,
                buffs=new_buffs,
                debuffs=new_debuffs,
                children=new_children,
                uptime=new_uptime,
            )
        if isinstance(eso_item, GearSet | Glyph):
            return replace(
                eso_item,
                buffs=new_buffs,
                debuffs=new_debuffs,
                uptime=new_uptime,
            )

        raise TypeError('Unsupported type')

    def _calculate_skill_children_uptimes(self, skill: Skill) -> list[Skill]:
        # Not the best solution for child's children calculation
        if not skill.children:
            return []

        skill_children = [
            self._calculate_item_uptimes(child) for child in skill.children
        ]

        new_children = []
        for child in skill_children:
            child_uptime = None
            if child.uptime:
                child_uptime = child.uptime
            else:
                child_uptime = self._calculate_skill_or_effect_uptime(
                    child, self._requested.damage_done_table.entries
                )
            if child_uptime:
                new_children.append(replace(child, uptime=child_uptime))
        return new_children

    def _set_parent_uptime(
        self,
        parent_item: Skill | GearSet | Glyph,
        buffs: list[Buff] | None = None,
        debuffs: list[Debuff] | None = None,
        children: list[Skill] | None = None,
    ) -> float | None:
        # If there is exactly one child/buff/debuff of a skill/set being
        # tracked - move calculated uptime to parent skill/set
        if isinstance(parent_item, Skill):
            uptime = parent_item.bumped_uptime(
                buffs, debuffs, children
            ) or self._calculate_skill_or_effect_uptime(
                parent_item, self._requested.damage_done_table.entries
            )
        elif isinstance(parent_item, GearSet | Glyph):
            uptime = parent_item.bumped_uptime(buffs, debuffs)

        return uptime

    @overload
    def _calculate_effects_uptimes(
        self,
        effects: list[Buff],
        effects_info: list[Aura],
    ) -> list[Buff]: ...

    @overload
    def _calculate_effects_uptimes(
        self,
        effects: list[Debuff],
        effects_info: list[Aura],
    ) -> list[Debuff]: ...

    def _calculate_effects_uptimes(self, effects, effects_info):
        new_items = []

        if not effects:
            return new_items

        for effect in effects:
            stack = None
            if effect.stack:
                stack = next(
                    stack
                    for stack in self._stacks
                    if stack.id == effect.stack.id
                )

            uptime = self._calculate_skill_or_effect_uptime(
                effect,
                effects_info,
                stack,
            )
            new_items.append(replace(effect, uptime=uptime, stack=stack))
        return new_items

    @overload
    def _calculate_skill_or_effect_uptime(
        self,
        skill_or_effect: Skill,
        casts_or_auras: list[Cast],
        stack: 'Stack | None' = None,
    ) -> float | None: ...

    @overload
    def _calculate_skill_or_effect_uptime(
        self,
        skill_or_effect: Buff | Debuff,
        casts_or_auras: list[Aura],
        stack: 'Stack | None' = None,
    ) -> float | None: ...

    def _calculate_skill_or_effect_uptime(
        self, skill_or_effect, casts_or_auras, stack=None
    ):
        try:
            extracted = next(
                filter(
                    lambda cast_or_aura: cast_or_aura.guid
                    == skill_or_effect.id,
                    casts_or_auras,
                )
            )
        except StopIteration:
            return None

        is_skill = isinstance(skill_or_effect, Skill)
        is_effect = isinstance(skill_or_effect, Buff | Debuff)
        is_cast = isinstance(extracted, Cast)
        is_aura = isinstance(extracted, Aura)
        if is_skill and is_cast:
            return skill_or_effect.calculate_uptime(
                extracted.hit_count,
                extracted.tick_count,
                self._requested.total_time,
            )
        if is_effect and is_aura:
            return skill_or_effect.calculate_uptime(
                extracted.total_uptime,
                self._requested.total_time,
                stack,
            )

        raise TypeError('Unsupported types')
