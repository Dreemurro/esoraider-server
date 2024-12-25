from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING, Generic, TypeVar

from esoraider_server.analysis.report_builder import ReportBuilder

if TYPE_CHECKING:
    from esoraider_server.esologs.api import ApiWrapper
    from esoraider_server.esologs.responses.report_data.log import Log
    from esoraider_server.esologs.responses.report_data.report import TableData
    from esoraider_server.esologs.responses.world_data.encounter import (
        Encounter,
    )

ResultT = TypeVar('ResultT')


class UseCase(Generic[ResultT], metaclass=ABCMeta):
    _result: ResultT

    @abstractmethod
    async def run(self) -> None:
        ...

    @property
    def result(self) -> ResultT:
        return self._result


class LogMixin:
    _log: str | None

    @property
    def log(self) -> str | None:
        return self._log

    @log.setter
    def log(self, value: str) -> None:
        self._log = value


class EncounterMixin:
    _encounter: int | None

    @property
    def encounter(self) -> int | None:
        return self._encounter

    @encounter.setter
    def encounter(self, value: int) -> None:
        self._encounter = value


class FightMixin:
    _fight: int | None
    _start_time: int | None
    _end_time: int | None

    @property
    def fight(self) -> int | None:
        return self._fight

    @fight.setter
    def fight(self, value: int) -> None:
        self._fight = value

    @property
    def start_time(self) -> int | None:
        return self._start_time

    @start_time.setter
    def start_time(self, value: int) -> None:
        self._start_time = value

    @property
    def end_time(self) -> int | None:
        return self._end_time

    @end_time.setter
    def end_time(self, value: int) -> None:
        self._end_time = value


class CharMixin:
    _char: int | None
    _targets: tuple[int] | None

    @property
    def char(self) -> int | None:
        return self._char

    @char.setter
    def char(self, value: int) -> None:
        self._char = value

    @property
    def targets(self) -> tuple[int] | None:
        return self._targets

    @targets.setter
    def targets(self, value: tuple[int]) -> None:
        self._targets = value


class AnalysisMixin(LogMixin, FightMixin, CharMixin):
    pass


class GetLogUseCase(UseCase['Log'], LogMixin):
    def __init__(self, api: 'ApiWrapper') -> None:
        self._api = api

    async def run(self) -> None:
        if not self._log:
            raise ValueError('Log is required')
        self._result = await self._api.query_log(self._log)


class GetFightUseCase(UseCase['TableData'], LogMixin, FightMixin):
    def __init__(self, api: 'ApiWrapper') -> None:
        self._api = api

    async def run(self) -> None:
        if not self._log:
            raise ValueError('Log is required')
        if not self._fight:
            raise ValueError('Fight is required')
        self._result = await self._api.query_table(
            log=self._log,
            fight_id=self._fight,
            start_time=self._start_time,
            end_time=self._end_time,
        )


class GetCharUseCase(UseCase[dict], AnalysisMixin):
    def __init__(self, api: 'ApiWrapper') -> None:
        self._api = api

    async def run(self) -> None:
        if not self._log:
            raise ValueError('Log is required')
        if not self._fight:
            raise ValueError('Fight is required')
        if not self._char:
            raise ValueError('Fight is required')

        response = await self._api.query_char_table(
            log=self._log,
            fight_id=self._fight,
            char_id=self._char,
            start_time=self._start_time,
            end_time=self._end_time,
        )

        report = ReportBuilder(
            api=self._api,
            log=self._log,
            fight_id=self._fight,
            char_id=self._char,
            summary_table=response.table,
            start_time=self._start_time,
            end_time=self._end_time,
            encounter_info=response.fights[0],
            target=self._targets,
        )
        self._result = await report.build()


class GetEncounterUseCase(UseCase['Encounter'], EncounterMixin):
    def __init__(self, api: 'ApiWrapper'):
        self._api = api

    async def run(self) -> None:
        if not self._encounter:
            raise ValueError('Encounter is required')
        result = await self._api.query_encounter_info(self._encounter)
        self._result = result if result else ''  # FIXME: types


class GetFightEffectsUseCase(UseCase[dict], LogMixin, FightMixin):
    def __init__(self, api: 'ApiWrapper'):
        self._api = api

    async def run(self) -> None:
        if not self._log:
            raise ValueError('Log is required')
        if not self._fight:
            raise ValueError('Fight is required')
        report = ReportBuilder(
            api=self._api,
            log=self._log,
            fight_id=self._fight,
            start_time=self._start_time,
            end_time=self._end_time,
        )
        self._result = await report.build()
