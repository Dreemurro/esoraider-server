from dataclasses import replace
from typing import List, Set, Union

from loguru import logger

from api.response import Aura, Cast, CastsTableData
from data.core import Buff, Debuff, GearSet, Glyph, Skill


# TODO: Refactor
class Uptimes:
    def __init__(
        self,
        damage_done_table,
        known_skills,
        known_sets,
        known_glyphs,
        char_buffs,
        char_debuffs,
    ) -> None:
        self.skills: List[Skill] = None
        self.sets: List[GearSet] = None
        self.glyphs: List[Glyph] = None
        self._damage_done_table: CastsTableData = damage_done_table
        self._known_skills: Set[Skill] = known_skills
        self._known_sets: List[GearSet] = known_sets
        self._known_glyphs: List[Glyph] = known_glyphs
        self._char_buffs: List[Aura] = char_buffs
        self._char_debuffs: List[Aura] = char_debuffs

    def calculate(self):
        self.skills = self._skills_uptimes()
        self.sets = self._sets_uptimes()
        self.glyphs = self._glyphs_uptimes()

    def _sets_uptimes(self):
        new_sets = []
        for gear_set in self._known_sets:
            new_set = self._calculate_item_uptimes(gear_set)
            new_sets.append(new_set)
        return new_sets

    def _skills_uptimes(self):
        new_skills = []
        for skill in self._known_skills:
            new_skill = self._calculate_item_uptimes(skill)
            new_skills.append(new_skill)
        return new_skills

    def _glyphs_uptimes(self):
        new_glyphs = []
        for glyph in self._known_glyphs:
            new_glyph = self._calculate_item_uptimes(glyph)
            new_glyphs.append(new_glyph)
        return new_glyphs

    def _calculate_item_uptimes(
        self,
        item: Union[Skill, GearSet, Glyph],
    ) -> Union[Skill, GearSet, Glyph]:
        new_buffs = self._calculate_effects_uptimes(
            item.buffs, self._char_buffs,
        )
        new_debuffs = self._calculate_effects_uptimes(
            item.debuffs, self._char_debuffs,
        )

        new_children: List[Skill] = []
        if isinstance(item, Skill) and item.children:
            # Not the best solution for child's children calculation
            child_children = [
                self._calculate_item_uptimes(child)
                for child in item.children
            ]
            for child in child_children:
                child_uptime = None
                if child.uptime:
                    child_uptime = child.uptime
                else:
                    child_uptime = self._calculate_skill_or_effect_uptime(
                        child,
                        self._damage_done_table.entries,
                    )
                if child_uptime:
                    new_children.append(replace(child, uptime=child_uptime))

        new_uptime = self._set_parent_uptime(
            item,
            new_buffs,
            new_debuffs,
            new_children,
        )

        if isinstance(item, Skill):
            new_item = replace(
                item,
                buffs=new_buffs,
                debuffs=new_debuffs,
                children=new_children,
                uptime=new_uptime,
            )
        elif isinstance(item, (GearSet, Glyph)):
            new_item = replace(
                item,
                buffs=new_buffs,
                debuffs=new_debuffs,
                uptime=new_uptime,
            )

        logger.debug(new_item)
        return new_item

    def _set_parent_uptime(
        self,
        parent_item: Union[Skill, GearSet, Glyph],
        buffs: List[Buff],
        debuffs: List[Debuff],
        children: List[Skill] = None,
    ) -> Union[float, None]:
        # If there is exactly one child/buff/debuff of a skill/set being
        # tracked - move calculated uptime to parent skill/set
        if isinstance(parent_item, Skill):
            uptime = parent_item.bumped_uptime(
                buffs, debuffs, children,
            ) or self._calculate_skill_or_effect_uptime(
                parent_item,
                self._damage_done_table.entries,
            )
        elif isinstance(parent_item, (GearSet, Glyph)):
            uptime = parent_item.bumped_uptime(buffs, debuffs)

        return uptime

    def _calculate_effects_uptimes(
        self,
        effects: Union[List[Buff], List[Debuff]],
        effects_info: List[Aura],
    ) -> Union[List[Buff], List[Debuff]]:
        new_items = []

        if not effects:
            return new_items

        for effect in effects:
            uptime = self._calculate_skill_or_effect_uptime(
                effect,
                effects_info,
            )
            new_items.append(replace(effect, uptime=uptime))
        return new_items

    def _calculate_skill_or_effect_uptime(
        self,
        skill_or_effect: Union[Skill, Buff, Debuff],
        casts_or_auras: Union[List[Cast], List[Aura]],
    ) -> Union[float, None]:
        try:
            extracted = next(filter(
                lambda cast_or_aura: cast_or_aura.guid == skill_or_effect.id,
                casts_or_auras,
            ))
        except StopIteration:
            return None

        if isinstance(skill_or_effect, Skill):
            uptime = skill_or_effect.calculate_uptime(
                extracted.hit_count,
                extracted.tick_count,
                self._damage_done_table.total_time,
            )
        elif isinstance(skill_or_effect, (Buff, Debuff)):
            uptime = skill_or_effect.calculate_uptime(
                extracted.total_uptime,
                self._damage_done_table.total_time,
            )

        return uptime
