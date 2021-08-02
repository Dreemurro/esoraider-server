from typing import List, Set

from loguru import logger

from data.classes.dragonknight import DRAGONKNIGHT_SKILLS
from data.classes.general import GENERAL_SKILLS
from data.classes.necromancer import NECROMANCER_SKILLS
from data.classes.nightblade import NIGHTBLADE_SKILLS
from data.classes.sorcerer import SORCERER_SKILLS
from data.classes.templar import TEMPLAR_SKILLS
from data.classes.warden import WARDEN_SKILLS
from data.core import Buff, Debuff, EsoEnum, GearSet, Glyph, Skill
from data.sets import GEAR_SETS
from data.glyphs import GLYPHS
from api.response import SummaryTableData, Talent


class TrackedInfo:
    def __init__(
        self,
        summary_table: SummaryTableData,
        char_class: str,
    ) -> None:
        self._summary_table: SummaryTableData = summary_table
        self._char_class: str = char_class
        self._char_skills: List[Talent] = []

        self.skills: Set[Skill] = set()
        self.sets: List[GearSet] = []
        self.glyphs: List[Glyph] = []
        self.buffs: List[Buff] = []
        self.debuffs: List[Debuff] = []

    def extract(self):
        self._get_char_skills()
        self._get_known_skills()
        self._get_known_sets()
        self._get_known_glyphs()
        self._get_known_effects()

    def _get_char_skills(self):
        logger.info('Get char skills from summary table')

        if not self._summary_table.combatant_info.talents:
            logger.error('Log is broken - character skills were not found')

        for talent in self._summary_table.combatant_info.talents:
            self._char_skills.append(talent)
            logger.debug(talent)

    def _get_known_skills(self):
        logger.info('Checking extracted skills in enum of skills to track')

        general_skills = GENERAL_SKILLS
        class_skills = self._get_class_skills()

        for skill in self._char_skills:
            for skills_enum in [general_skills, class_skills]:
                try:
                    known_skill: Skill = skills_enum(skill.guid).value
                except StopIteration:
                    continue

                logger.debug(known_skill)
                self.skills.add(known_skill)
                break

    def _get_class_skills(self) -> EsoEnum:
        classes = {
            'Nightblade': NIGHTBLADE_SKILLS,
            'DragonKnight': DRAGONKNIGHT_SKILLS,
            'Warden': WARDEN_SKILLS,
            'Templar': TEMPLAR_SKILLS,
            'Necromancer': NECROMANCER_SKILLS,
            'Sorcerer': SORCERER_SKILLS,
        }

        try:
            return classes[self._char_class]
        except KeyError:
            raise Exception('Class is not known. Are you from the future?')

    def _get_known_sets(self):
        logger.info('Checking known sets in char data')
        char_sets = {
            gear.set_id for gear in self._summary_table.combatant_info.gear
        }
        for gear_set in char_sets:
            try:
                known_set = GEAR_SETS(gear_set).value
            except StopIteration:
                continue

            logger.debug(known_set)
            self.sets.append(known_set)

    def _get_known_glyphs(self):
        logger.info('Checking known enchants in char data')
        char_enchants = {
            gear.enchant_type
            for gear in self._summary_table.combatant_info.gear
        }
        for enchant in char_enchants:
            try:
                known_glyph = GLYPHS(enchant).value
            except StopIteration:
                continue

            logger.debug(known_glyph)
            self.glyphs.append(known_glyph)

    def _get_known_effects(self):
        logger.info('Getting buffs & debuffs to track based on skills & sets')

        for tracked_info in [*self.skills, *self.sets, *self.glyphs]:
            if tracked_info.buffs:
                self.buffs.extend(tracked_info.buffs)
                for buff in tracked_info.buffs:
                    logger.debug(buff)
            if tracked_info.debuffs:
                self.debuffs.extend(tracked_info.debuffs)
                for debuff in tracked_info.debuffs:
                    logger.debug(debuff)
