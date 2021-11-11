"""Checklist building."""

from dataclasses import asdict
from typing import List, Set

from esoraider_server.data.rules import Rules
from esoraider_server.esologs.consts import (
    CharClass,
    GearSlot,
    GearType,
    WeaponType,
    WieldType,
)
from esoraider_server.esologs.responses.common import Gear
from esoraider_server.esologs.responses.report_data.effects import Aura


class ChecklistBuilder(object):
    def __init__(
        self,
        spec: str,
        class_: CharClass,
        gear: List[Gear],
        passives: List[Aura],
    ) -> None:
        self._spec = spec
        self._class = class_
        self._gear = gear
        self._passives = passives

        self._armor: List[Gear] = []
        self._front_bar: List[Gear] = []
        self._back_bar: List[Gear] = []

        self.rule_set: Set[Rules] = set()
        self.checklist = None

    def build(self):
        self._split_gear()

        self._add_universal_rules()
        self._add_race_rules()
        self._add_armor_rules()
        self._add_weapon_rules()
        self._add_class_rules()

        self._finalize()

    def _split_gear(self):
        for gear in self._gear:
            if GearSlot.is_frontbar_weapon(gear.slot):
                self._front_bar.append(gear)
            elif GearSlot.is_backbar_weapon(gear.slot):
                self._back_bar.append(gear)
            elif GearSlot.is_armor(gear.slot):
                self._armor.append(gear)

    def _add_universal_rules(self):
        rules = (
            Rules.UNDAUNTED,
        )
        for rule in rules:
            self.rule_set.add(rule)

    def _add_race_rules(self):
        race_rules = (
            # Rules.ARGONIAN,
            Rules.BRETON,
            Rules.DARK_ELF,
            Rules.HIGH_ELF,
            Rules.IMPERIAL,
            Rules.KHAJIIT,
            Rules.NORD,
            Rules.ORC,
            Rules.REDGUARD,
            # Rules.WOOD_ELF,
        )

        ids = {pas.ability for pas in self._passives}
        for rule in race_rules:
            for passive in rule.value.buffs:
                if passive.id in ids:
                    self.rule_set.add(rule)
                    return

    def _add_armor_rules(self):
        armor_rules = {
            GearType.LIGHT_ARMOR: Rules.LIGHT_ARMOR,
            GearType.MEDIUM_ARMOR: Rules.MEDIUM_ARMOR,
            # GearType.HEAVY_ARMOR: Rules.HEAVY_ARMOR,
        }
        for armor in self._armor:
            rule = armor_rules.get(armor.type, None)
            if rule:
                self.rule_set.add(rule)

    def _add_weapon_rules(self):
        weapon_rules = {
            # WieldType.BOW: None,
            WieldType.DESTRUCTION_STAFF: Rules.DESTRUCTION_STAFF,
            # WieldType.DUAL_WIELD: None,
            # WieldType.ONE_HAND_AND_SHIELD: None,
            # WieldType.RESTORATION_STAFF: None,
            # WieldType.TWO_HANDED: None,
        }

        bars = (
            tuple(_.type for _ in self._front_bar),
            tuple(_.type for _ in self._back_bar),
        )
        for weapons in bars:
            wield_type = WeaponType.wield_type(*weapons)
            rule = weapon_rules.get(wield_type, None)
            if rule:
                self.rule_set.add(rule)

    def _add_class_rules(self):
        class_rules = {
            CharClass.DRAGONKNIGHT: Rules.DRAGONKNIGHT,
            CharClass.NECROMANCER: Rules.NECROMANCER,
            CharClass.NIGHTBLADE: Rules.NIGHTBLADE,
            CharClass.SORCERER: Rules.SORCERER,
            CharClass.TEMPLAR: Rules.TEMPLAR,
            CharClass.WARDEN: Rules.WARDEN,
        }
        rule = class_rules.get(self._class, None)
        if rule:
            self.rule_set.add(rule)

    def _finalize(self):
        ids = {pas.ability or pas.guid for pas in self._passives}
        checklist = []

        for rules in self.rule_set:
            buffs = [
                {
                    'passive': asdict(buff),
                    'present': buff.id in ids,
                }
                for buff in rules.value.buffs
            ]

            checklist.append({
                'name': rules.value.name,
                'icon': rules.value.icon,
                'passives': buffs,
                'status': all(buff['present'] for buff in buffs),
            })

        self.checklist = checklist
