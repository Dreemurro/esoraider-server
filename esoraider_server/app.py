from typing import Annotated, cast

from litestar import Litestar, MediaType, Router, get
from litestar.config.cors import CORSConfig
from litestar.di import Provide
from litestar.exceptions import NotFoundException, ValidationException
from litestar.params import Parameter

from esoraider_server import dependencies as deps
from esoraider_server.analysis.exceptions import (
    NothingToTrackError,
    OutsideOfCombatError,
    SkillsNotFoundError,
    WrongCharError,
)
from esoraider_server.esologs.api import ApiWrapper
from esoraider_server.esologs.exceptions import (
    NonexistentFightError,
    NonexistentLogError,
    ZeroLengthFightError,
)
from esoraider_server.esologs.responses.report_data.log import Log
from esoraider_server.esologs.responses.world_data.encounter import Encounter
from esoraider_server.settings import (
    CORS_ALLOW_ORIGINS,
    DEBUG,
    HEALTHCHECK_TOKEN,
)

LogCode = Annotated[
    str,
    Parameter(title='Log code', pattern=r'(a:)?[a-zA-Z0-9]{16}'),
]
FightID = Annotated[
    int,
    Parameter(title='Fight ID', ge=0),
]
Target = Annotated[
    int | None,
    Parameter(title='Target ID', ge=0),
]
Targets = Annotated[
    list[Target] | None,
    Parameter(title='Target IDs', min_items=1, required=False),
]
StartTime = Annotated[
    int | None,
    Parameter(title='Start time', ge=0, required=False),
]
EndTime = Annotated[
    int | None,
    Parameter(title='Start time', ge=0, required=False),
]


@get(
    '/{log:str}',
    name='get_log',
    dependencies={'usecase': Provide(deps.get_log_use_case)},
)
async def get_log(
    log: LogCode,
    usecase: deps.UseCaseGetLog,
) -> Log:
    usecase.log = log
    try:
        await usecase.run()
    except NonexistentLogError as ex:
        raise NotFoundException(detail=str(ex)) from ex
    return usecase.result


@get(
    '/{log:str}/{fight:int}',
    name='get_fight',
    dependencies={'usecase': Provide(deps.get_fight_use_case)},
)
async def get_fight(
    log: LogCode,
    fight: FightID,
    usecase: deps.UseCaseGetFight,
    start_time: StartTime = None,
    end_time: EndTime = None,
) -> dict:
    usecase.log = log
    usecase.fight = fight
    usecase.start_time = start_time
    usecase.end_time = end_time
    try:
        await usecase.run()
    except ZeroLengthFightError as ex:
        raise ValidationException(detail=str(ex)) from ex
    except (NonexistentFightError, NonexistentLogError) as ex:
        raise NotFoundException(detail=str(ex)) from ex
    return usecase.result


@get(
    '/{log:str}/{fight:int}/{char:int}',
    name='get_char',
    dependencies={'usecase': Provide(deps.get_char_use_case)},
)
async def get_char(
    log: LogCode,
    fight: FightID,
    char: int,
    usecase: deps.UseCaseGetChar,
    start_time: StartTime = None,
    end_time: EndTime = None,
    target: Targets = None,
) -> dict:
    usecase.log = log
    usecase.fight = fight
    usecase.char = char
    usecase.start_time = start_time
    usecase.end_time = end_time
    usecase.targets = target
    try:
        await usecase.run()
    except (
        ZeroLengthFightError,
        SkillsNotFoundError,
        NothingToTrackError,
        OutsideOfCombatError,
    ) as ex:
        raise ValidationException(detail=str(ex)) from ex
    except (
        NonexistentFightError,
        WrongCharError,
        NonexistentLogError,
    ) as ex:
        raise NotFoundException(detail=str(ex)) from ex
    return usecase.result


@get(
    '/encounter/{encounter:int}',
    name='get_encounter',
    dependencies={'usecase': Provide(deps.get_encounter_use_case)},
)
async def get_encounter(
    encounter: int,
    usecase: deps.UseCaseGetEncounter,
) -> Encounter:
    usecase.encounter = encounter
    await usecase.run()
    return usecase.result


@get(
    '/fight/{log:str}/{fight:int}',
    name='get_fight_effects',
    dependencies={'usecase': Provide(deps.get_fight_effects_use_case)},
)
async def get_fight_effects(
    log: LogCode,
    fight: FightID,
    usecase: deps.UseCaseGetFightEffects,
    start_time: StartTime = None,
    end_time: EndTime = None,
) -> dict:
    usecase.log = log
    usecase.fight = fight
    usecase.start_time = start_time
    usecase.end_time = end_time
    try:
        await usecase.run()
    except ZeroLengthFightError as ex:
        raise ValidationException(detail=str(ex)) from ex
    except (NonexistentFightError, NonexistentLogError) as ex:
        raise NotFoundException(detail=str(ex)) from ex
    return usecase.result


@get(
    f'/{HEALTHCHECK_TOKEN}/health',
    media_type=MediaType.HTML,
    name='health',
)
async def healthcheck() -> str:
    return 'gucci'


async def connect_api(app: Litestar) -> ApiWrapper:
    if not getattr(app.state, 'api', None):
        api = ApiWrapper()
        await api.connect()
        app.state.api = api
    return app.state.api


async def close_api(app: Litestar) -> None:
    if getattr(app.state, 'api', None):
        await cast('ApiWrapper', app.state.api).close()


base_router = Router(
    path='/',
    route_handlers=[
        get_log,
        get_fight,
        get_char,
        get_encounter,
        get_fight_effects,
        healthcheck,
    ],
    dependencies={'api': Provide(deps.api)},
)

cors_config = CORSConfig(
    allow_origins=CORS_ALLOW_ORIGINS,
)

app = Litestar(
    route_handlers=[base_router],
    on_startup=[connect_api],
    on_shutdown=[close_api],
    debug=DEBUG,
    cors_config=cors_config,
    logging_config=None,
)
