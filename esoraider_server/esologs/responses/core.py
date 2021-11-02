"""Parent JSON dataclass."""

from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin, LetterCase, Undefined, config


@dataclass
class EsoLogsDataClass(DataClassJsonMixin):
    dataclass_json_config = config(
        letter_case=LetterCase.CAMEL,  # type: ignore
        undefined=Undefined.RAISE,
    )['dataclasses_json']
