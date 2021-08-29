"""Known data extraction."""

from typing import List, Optional, Type

from api.response import SummaryTableData, Talent
from data.buffs import BUFFS
from data.classes.dragonknight.skills import DRAGONKNIGHT_SKILLS
from data.classes.general import GENERAL_SKILLS
from data.classes.necromancer.skills import NECROMANCER_SKILLS
from data.classes.nightblade.skills import NIGHTBLADE_SKILLS
from data.classes.sorcerer.skills import SORCERER_SKILLS
from data.classes.templar.skills import TEMPLAR_SKILLS
from data.classes.warden.skills import WARDEN_SKILLS
from data.core import Buff, Debuff, EsoEnum, GearSet, Glyph, Skill, Stack
from data.glyphs import GLYPHS
from data.sets import GEAR_SETS
from loguru import logger

FIGHT_BUFFS = (
    BUFFS.MAJOR_COURAGE.value,  # Spell Power Cure, Olorime
    BUFFS.MAJOR_FORCE.value,  # Saxhleel, Aggressive Horn
    # BUFFS.MAJOR_PROPHECY.value,  # Potions
    BUFFS.MAJOR_RESOLVE.value,  # Frost Cloak
    # BUFFS.MAJOR_SAVAGERY.value,  # Potions
    BUFFS.MAJOR_SLAYER.value,  # Master Architect, War Machine, Roaring
    BUFFS.MAJOR_SORCERY.value,  # Potions, Igneous Weapons

    BUFFS.MINOR_BERSERK.value,  # Combat Prayer
    BUFFS.MINOR_PROPHECY.value,  # Sorc passive
    BUFFS.MINOR_SAVAGERY.value,  # NB passive
    BUFFS.MINOR_SORCERY.value,  # Templar passive

    BUFFS.AGGRESSIVE_HORN.value,
)


# Move to general skills?
def _get_class_skills(char_class: str) -> Type[EsoEnum]:
    classes = {
        'Nightblade': NIGHTBLADE_SKILLS,
        'DragonKnight': DRAGONKNIGHT_SKILLS,
        'Warden': WARDEN_SKILLS,
        'Templar': TEMPLAR_SKILLS,
        'Necromancer': NECROMANCER_SKILLS,
        'Sorcerer': SORCERER_SKILLS,
    }

    try:
        return classes[char_class]
    except KeyError:
        raise KeyError(
            'Class {0} is not known. Are you from the future?'.format(
                char_class,
            ))


class TrackedInfo(object):
    """
    Extracts known info for further usage during analysis.

    Extracts all the known data, such as:
    - skills
    - gear sets
    - glyphs
    - buffs/debuffs and related stacks
    """

    def __init__(
        self,
        summary_table: Optional[SummaryTableData] = None,
        char_class: Optional[str] = None,
    ) -> None:
        self._summary_table = summary_table
        self._char_class = char_class
        self._char_skills: List[Talent] = []

        self.skills: List[Skill] = []
        self.sets: List[GearSet] = []
        self.glyphs: List[Glyph] = []
        self.buffs: List[Buff] = []
        self.debuffs: List[Debuff] = []
        self.stacks: List[Stack] = []

    def extract(self):
        """Extract known skills, sets, glyphs, buffs & debuffs with stacks."""
        if not self._summary_table and not self._char_class:
            self.buffs = list(FIGHT_BUFFS)
            return

        self._get_char_skills()
        self._get_known_skills()
        self._get_known_sets()
        self._get_known_glyphs()
        self._get_known_effects()
        self._get_known_stacks()

    def _get_char_skills(self):
        logger.info('Get char skills from summary table')

        if not self._summary_table.combatant_info.talents:
            logger.error('Log is broken - character skills were not found')

        for talent in self._summary_table.combatant_info.talents:
            self._char_skills.append(talent)
            logger.debug('{0} - {1}'.format(talent.name, talent.guid))

    def _get_known_skills(self):
        logger.info('Checking extracted skills in enum of skills to track')

        general_skills = GENERAL_SKILLS
        class_skills = _get_class_skills(self._char_class)

        for skill in self._char_skills:
            for skills_enum in (general_skills, class_skills):
                try:
                    known_skill: Skill = skills_enum(skill.guid).value
                except StopIteration:
                    continue
                self.skills.append(known_skill)
                break

        logger.info('{0} skills to track'.format(len(self.skills)))
        for _ in self.skills:
            logger.debug(_.name)

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
            self.sets.append(known_set)

        logger.info('{0} sets to track'.format(len(self.sets)))
        for _ in self.sets:
            logger.debug(_.name)

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
            self.glyphs.append(known_glyph)

        logger.info('{0} glyphs to track'.format(len(self.glyphs)))
        for _ in self.glyphs:
            logger.debug(_.name)

    def _get_known_effects(self):
        logger.info(
            'Getting buffs & debuffs to track based on skills, sets & glyphs',
        )

        skills_with_children = [
            skill for skill in self.skills if skill.children
        ]
        children = [
            child
            for skill in skills_with_children
            for child in skill.children
        ]
        with_buffs = [
            tracked
            for tracked in (*self.skills, *self.sets, *self.glyphs, *children)
            if tracked.buffs
        ]
        with_debuffs = [
            tracked
            for tracked in (*self.skills, *self.sets, *self.glyphs, *children)
            if tracked.debuffs
        ]

        self.buffs.extend([
            buff
            for tracked in with_buffs
            for buff in tracked.buffs
        ])
        self.debuffs.extend([
            debuff
            for tracked in with_debuffs
            for debuff in tracked.debuffs
        ])

        logger.info('{0} buffs to track'.format(len(self.buffs)))
        for _ in self.buffs:
            logger.debug(_.name)
        logger.info('{0} debuffs to track'.format(len(self.debuffs)))
        for _ in self.debuffs:
            logger.debug(_.name)

    def _get_known_stacks(self):
        logger.info('Getting stacks to track based on buffs & debuffs')

        self.stacks = [
            effect.stack
            for effect in (*self.buffs, *self.debuffs)
            if effect.stack
        ]

        for _ in self.stacks:
            if _.buffs:
                logger.info('Found additional buffs required for stack')
                self.buffs.extend(_.buffs)
                for buff in _.buffs:
                    logger.debug(buff.name)
            if _.debuffs:
                logger.info('Found additional debuffs required for stack')
                self.debuffs.extend(_.debuffs)
                for debuff in _.debuffs:
                    logger.debug(debuff.name)

        logger.info('{0} stacks to track'.format(len(self.stacks)))
        for _ in self.stacks:
            logger.debug(_.name)
