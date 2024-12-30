"""Known data extraction."""

from typing import TYPE_CHECKING

from structlog.stdlib import get_logger

from esoraider_server.analysis.exceptions import (
    NothingToTrackError,
    SkillsNotFoundError,
)
from esoraider_server.data.buffs import Buffs
from esoraider_server.data.classes.arcanist.skills import ArcanistSkills
from esoraider_server.data.classes.dragonknight.skills import DragonknightSkills
from esoraider_server.data.classes.general import GeneralSkills
from esoraider_server.data.classes.necromancer.skills import NecromancerSkills
from esoraider_server.data.classes.nightblade.skills import NightbladeSkills
from esoraider_server.data.classes.sorcerer.skills import SorcererSkills
from esoraider_server.data.classes.templar.skills import TemplarSkills
from esoraider_server.data.classes.warden.skills import WardenSkills
from esoraider_server.data.debuffs import Debuffs
from esoraider_server.data.repository import EnumESODataRepository

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
    Buffs.MAJOR_COURAGE.value,  # Spell Power Cure, Olorime
    Buffs.MAJOR_FORCE.value,  # Saxhleel, Aggressive Horn
    # BUFFS.MAJOR_PROPHECY.value,  # Potions
    Buffs.MAJOR_RESOLVE.value,  # Frost Cloak
    # BUFFS.MAJOR_SAVAGERY.value,  # Potions
    Buffs.MAJOR_SLAYER.value,  # Master Architect, War Machine, Roaring
    Buffs.MAJOR_SORCERY.value,  # Potions, Igneous Weapons
    Buffs.MINOR_BERSERK.value,  # Combat Prayer
    Buffs.MINOR_PROPHECY.value,  # Sorc passive
    Buffs.MINOR_SAVAGERY.value,  # NB passive
    Buffs.MINOR_SORCERY.value,  # Templar passive
    Buffs.AGGRESSIVE_HORN.value,
)
FIGHT_DEBUFFS = (
    Debuffs.MAJOR_BREACH.value,
    Debuffs.MAJOR_VULNERABILITY.value,
    Debuffs.MINOR_BREACH.value,
    Debuffs.MINOR_BRITTLE.value,
    Debuffs.MINOR_LIFESTEAL.value,
    Debuffs.MINOR_MAGICKASTEAL.value,
    Debuffs.MINOR_MAIM.value,
    Debuffs.MINOR_VULNERABILITY.value,
    Debuffs.CRUSHER.value,
)


# Move to general skills?
def _get_class_skills(char_class: str) -> type['EsoEnum']:
    classes = {
        'Nightblade': NightbladeSkills,
        'DragonKnight': DragonknightSkills,
        'Warden': WardenSkills,
        'Templar': TemplarSkills,
        'Necromancer': NecromancerSkills,
        'Sorcerer': SorcererSkills,
        'Arcanist': ArcanistSkills,
    }

    try:
        return classes[char_class]
    except KeyError as ex:
        raise ValueError(
            f'Class {char_class} is not known. Are you from the future?'
        ) from ex


class TrackedInfo:
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
        self._repository = EnumESODataRepository()

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
            )
        )
        if not any(empty_attrs):
            raise NothingToTrackError

    def _get_encounter_targets(self):
        logger.info('Get main targets of a fight')
        id_ = self._encounter_info.encounter_id

        encounter = self._repository.get_encounter(id_)
        if not encounter:
            logger.warning(
                f'Targets for encounter = {id_} were not found',
            )
            return
        if encounter.targets:
            self.targets = encounter.targets
            for _ in self.targets:
                logger.debug(f'{_.name} - {_.id}')

    def _get_char_skills(self):
        logger.info('Get char skills from summary table')

        if not self._summary_table.combatant_info.talents:
            raise SkillsNotFoundError

        for talent in self._summary_table.combatant_info.talents:
            self._char_skills.append(talent)
            logger.debug(f'{talent.name} - {talent.guid}')

    def _get_known_skills(self):
        logger.info('Checking extracted skills in enum of skills to track')

        general_skills = GeneralSkills
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
            known_set = self._repository.get_gear_set(gear_set)
            if not known_set:
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
            known_glyph = self._repository.get_glyph(enchant)
            if not known_glyph:
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
            child for skill in skills_with_children for child in skill.children
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

        self.buffs.extend(
            [buff for tracked in with_buffs for buff in tracked.buffs]
        )
        self.debuffs.extend(
            [debuff for tracked in with_debuffs for debuff in tracked.debuffs]
        )

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

        self._track_stack_effects()

        logger.info(f'{len(self.stacks)} stacks to track')
        for _ in self.stacks:
            logger.debug(_.name)

    def _track_stack_effects(self):
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
