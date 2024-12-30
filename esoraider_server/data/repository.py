from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

from structlog.stdlib import get_logger

from esoraider_server.data.encounters import Encounters

if TYPE_CHECKING:
    from esoraider_server.data.core import Encounter

logger = get_logger()


class ESODataRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_encounter(self, id_: int) -> 'Encounter | None':
        raise NotImplementedError


class EnumESODataRepository(ESODataRepository):
    def get_encounter(self, id_: int) -> 'Encounter | None':
        try:
            return Encounters(id_).value
        except StopIteration:
            return None
