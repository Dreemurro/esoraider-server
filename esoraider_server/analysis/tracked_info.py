"""Known data extraction."""

from typing import TYPE_CHECKING

from structlog.stdlib import get_logger

from esoraider_server.analysis.exceptions import (
    NothingToTrackException,
    SkillsNotFoundException,
)
from esoraider_server.data.buffs import BUFFS
from esoraider_server.data.classes.arcanist.skills import ARCANIST_SKILLS
from esoraider_server.data.classes.dragonknight.skills import (
    DRAGONKNIGHT_SKILLS,
)
from esoraider_server.data.classes.general import GENERAL_SKILLS
from esoraider_server.data.classes.necromancer.skills import NECROMANCER_SKILLS
from esoraider_server.data.classes.nightblade.skills import NIGHTBLADE_SKILLS
from esoraider_server.data.classes.sorcerer.skills import SORCERER_SKILLS
from esoraider_server.data.classes.templar.skills import TEMPLAR_SKILLS
from esoraider_server.data.classes.warden.skills import WARDEN_SKILLS
from esoraider_server.data.debuffs import DEBUFFS
from esoraider_server.data.encounters import Encounters
from esoraider_server.data.glyphs import GLYPHS
from esoraider_server.data.sets import GEAR_SETS

if TYPE_CHECKING:
    from esoraider_server.data.core import (
        Buff,
        Debuff,
        EsoEnum,
        GearSet,
        Glyph,
        Skill,
        Stack,
        Target,
    )
    from esoraider_server.esologs.consts import CharClass
    from esoraider_server.esologs.responses.common import Talent
    from esoraider_server.esologs.responses.report_data.fight import Fight
    from esoraider_server.esologs.responses.report_data.summary import (
        SummaryTableData,
    )

logger = get_logger()

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
def _get_class_skills(char_class: str) -> type['EsoEnum']:
    classes = {
        'Nightblade': NIGHTBLADE_SKILLS,
        'DragonKnight': DRAGONKNIGHT_SKILLS,
        'Warden': WARDEN_SKILLS,
        'Templar': TEMPLAR_SKILLS,
        'Necromancer': NECROMANCER_SKILLS,
        'Sorcerer': SORCERER_SKILLS,
        'Arcanist': ARCANIST_SKILLS,
    }

    try:
        return classes[char_class]
    except KeyError:
        raise KeyError(
            f'Class {char_class} is not known. Are you from the future?')


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
        summary_table: 'SummaryTableData | None' = None,
        char_class: 'CharClass | None' = None,
        encounter_info: 'Fight | None' = None,
    ) -> None:
        self._summary_table = summary_table
        self._encounter_info = encounter_info
        self._char_class = char_class
        self._char_skills: list[Talent] = []

        self.targets: list[Target] = []
        self.skills: set[Skill] = set()
        self.sets: list[GearSet] = []
        self.glyphs: list[Glyph] = []
        self.buffs: list[Buff] = []
        self.debuffs: list[Debuff] = []
        self.stacks: list[Stack] = []

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
        id_ = self._encounter_info.encounter_id

        try:
            encounter = Encounters(id_)
        except StopIteration:
            logger.info(
                f'Targets for encounter = {id_} were not found',
            )
            return
        if encounter.value.targets:
            self.targets = encounter.value.targets
            for _ in self.targets:
                logger.debug(f'{_.name} - {_.id}')

    def _get_char_skills(self):
        logger.info('Get char skills from summary table')

        if not self._summary_table.combatant_info.talents:
            raise SkillsNotFoundException

        for talent in self._summary_table.combatant_info.talents:
            self._char_skills.append(talent)
            logger.debug(f'{talent.name} - {talent.guid}')

    def _get_known_skills(self):
        logger.info('Checking extracted skills in enum of skills to track')

        general_skills = GENERAL_SKILLS
        class_skills = _get_class_skills(self._char_class.value)

        for skill in self._char_skills:
            for skills_enum in (general_skills, class_skills):
                try:
                    known_skill: Skill = skills_enum(skill.guid).value
                except StopIteration:
                    continue
                self.skills.add(known_skill)
                break

        logger.info(f'{len(self.skills)} skills to track')
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

        logger.info(f'{len(self.sets)} sets to track')
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

        logger.info(f'{len(self.glyphs)} glyphs to track')
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

        logger.info(f'{len(self.buffs)} buffs to track')
        for _ in self.buffs:
            logger.debug(_.name)
        logger.info(f'{len(self.debuffs)} debuffs to track')
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

        logger.info(f'{len(self.stacks)} stacks to track')
        for _ in self.stacks:
            logger.debug(_.name)
