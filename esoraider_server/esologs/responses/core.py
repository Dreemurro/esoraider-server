"""Parent JSON dataclass."""

from msgspec import Struct


class EsoLogsDataClass(Struct, rename='camel'):
    pass
