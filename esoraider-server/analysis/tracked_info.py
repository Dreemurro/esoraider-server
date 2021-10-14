"""Known data extraction."""

from typing import Dict, List, Optional, Set, Type

from data.buffs import BUFFS
from data.classes.dragonknight.skills import DRAGONKNIGHT_SKILLS
from data.classes.general import GENERAL_SKILLS
from data.classes.necromancer.skills import NECROMANCER_SKILLS
from data.classes.nightblade.skills import NIGHTBLADE_SKILLS
from data.classes.sorcerer.skills import SORCERER_SKILLS
from data.classes.templar.skills import TEMPLAR_SKILLS
from data.classes.warden.skills import WARDEN_SKILLS
from data.core import (
    Buff, Debuff, EsoEnum, GearSet, Glyph, Skill, Stack, Target,
)
from data.debuffs import DEBUFFS
from data.encounters import Encounters
from data.glyphs import GLYPHS
from data.sets import GEAR_SETS
from esologs.responses.common import Talent
from esologs.responses.report_data.summary import SummaryTableData
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
FIGHT_DEBUFFS = (
    DEBUFFS.MAJOR_BREACH.value,
    DEBUFFS.MAJOR_VULNERABILITY.value,

    DEBUFFS.MINOR_BREACH.value,
    DEBUFFS.MINOR_BRITTLE.value,
    DEBUFFS.MINOR_LIFESTEAL.value,
    DEBUFFS.MINOR_MAGICKASTEAL.value,
    DEBUFFS.MINOR_MAIM.value,
    DEBUFFS.MINOR_VULNERABILITY.value,

    DEBUFFS.CRUSHER.value,
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


class SkillsNotFoundException(Exception):
    def __init__(self):
        message = 'Log is broken - character skills were not found'
        super().__init__(message)


class NothingToTrackException(Exception):
    def __init__(self):
        message = 'There is nothing to track'
        super().__init__(message)


class TrackedInfo(object):
    """
    Extracts known info for further usage during analysis.

    Extracts all the known data, such as:
    - important targets of a fight
    - skills
    - gear sets
    - glyphs
    - buffs/debuffs and related stacks
    """

    def __init__(
        self,
        summary_table: Optional[SummaryTableData] = None,
        char_class: Optional[str] = None,
        encounter_info: Optional[Dict[str, int]] = None,
    ) -> None:
        self._summary_table = summary_table
        self._encounter_info = encounter_info
        self._char_class = char_class
        self._char_skills: List[Talent] = []

        self.targets: List[Target] = []
        self.skills: Set[Skill] = set()
        self.sets: List[GearSet] = []
        self.glyphs: List[Glyph] = []
        self.buffs: List[Buff] = []
        self.debuffs: List[Debuff] = []
        self.stacks: List[Stack] = []

    def extract(self):
        """Extract known skills, sets, glyphs, buffs & debuffs with stacks."""
        if not self._summary_table and not self._char_class:
            self.buffs = list(FIGHT_BUFFS)
            self.debuffs = list(FIGHT_DEBUFFS)
            return

        self._get_encounter_targets()
        self._get_char_skills()
        self._get_known_skills()
        self._get_known_sets()
        self._get_known_glyphs()
        self._get_known_effects()
        self._get_known_stacks()

        empty_attrs = (
            bool(attr)
            for attr in (
                self.skills,
                self.sets,
                self.glyphs,
                self.buffs,
                self.debuffs,
                self.stacks,
            ))
        if not any(empty_attrs):
            raise NothingToTrackException

    def _get_encounter_targets(self):
        logger.info('Get main targets of a fight')
        id_ = self._encounter_info.get('encounterID')

        try:
            encounter = Encounters(id_)
        except StopIteration:
            logger.info(
                'Targets for encounter = {0} were not found'.format(id_),
            )
            return
        self.targets = encounter.value.targets
        for _ in self.targets:
            logger.debug('{0} - {1}'.format(_.name, _.id))

    def _get_char_skills(self):
        logger.info('Get char skills from summary table')

        if not self._summary_table.combatant_info.talents:
            raise SkillsNotFoundException

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
                self.skills.add(known_skill)
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
