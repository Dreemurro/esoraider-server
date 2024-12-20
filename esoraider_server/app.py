from typing import Annotated, cast

from gql.transport.exceptions import TransportQueryError  # type: ignore
from litestar import Litestar, MediaType, Response, Router, get
from litestar.datastructures import State
from litestar.di import Provide
from litestar.params import Parameter
from litestar.status_codes import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from esoraider_server.analysis.exceptions import (
    NothingToTrackException,
    OutsideOfCombatException,
    SkillsNotFoundException,
    WrongCharException,
)
from esoraider_server.analysis.report_builder import ReportBuilder
from esoraider_server.esologs.api import ApiWrapper
from esoraider_server.esologs.exceptions import ZeroLengthFightException
from esoraider_server.esologs.responses.report_data.log import Log
from esoraider_server.esologs.responses.world_data.encounter import Encounter
from esoraider_server.settings import DEBUG, HEALTHCHECK_TOKEN

log_code = Parameter(title='Log code', pattern=r'(a:)?[a-zA-Z0-9]{16}')


@get('/{log:str}')
async def get_log(
    log: Annotated[str, log_code],
    api: ApiWrapper,
) -> Log:
    try:
        return await api.query_log(log)
    except TransportQueryError:
        return Response(
            "This log is either private or doesn't exist",
            media_type=MediaType.TEXT,
            status_code=HTTP_404_NOT_FOUND,
        )


@get('/{log:str}/{fight:int}')
async def get_fight(
    log: str,
    fight: int,
    api: ApiWrapper,
    start_time: int | None = None,
    end_time: int | None = None,
) -> dict:
    try:
        return await api.query_table(
            log=log,
            fight_id=fight,
            start_time=start_time,
            end_time=end_time,
        )
    except ZeroLengthFightException as ex:
        # FIXME: this is done only for the initial compatibility
        return Response(
            str(ex),
            media_type=MediaType.TEXT,
            status_code=HTTP_400_BAD_REQUEST,
        )


@get('/{log:str}/{fight:int}/{char:int}')
async def get_char(
    log: str,
    fight: int,
    char: int,
    api: ApiWrapper,
    start_time: int | None = None,
    end_time: int | None = None,
    target: list[int] | None = None,
) -> dict:
    try:
        response = await api.query_char_table(
            log=log,
            fight_id=fight,
            char_id=char,
            start_time=start_time,
            end_time=end_time,
        )
    except ZeroLengthFightException as ex:
        # FIXME: this is done only for the initial compatibility
        return Response(
            str(ex),
            media_type=MediaType.TEXT,
            status_code=HTTP_400_BAD_REQUEST,
        )

    report = ReportBuilder(
        api=api,
        log=log,
        fight_id=fight,
        char_id=char,
        summary_table=response.table,
        start_time=start_time,
        end_time=end_time,
        encounter_info=response.fights[0],
        target=target,
    )

    try:
        return await report.build()
    except (
        SkillsNotFoundException,
        NothingToTrackException,
        WrongCharException,
        OutsideOfCombatException,
    ) as ex:
        # FIXME: this is done only for the initial compatibility
        return Response(
            str(ex),
            media_type=MediaType.TEXT,
            status_code=HTTP_400_BAD_REQUEST,
        )


@get('/encounter/{encounter:int}')
async def get_encounter(encounter: int, api: ApiWrapper) -> Encounter:
    response = await api.query_encounter_info(encounter)

    if response:
        return response
    return ''


@get('/fight/{log:str}/{fight:int}')
async def get_fight_effects(
    log: str,
    fight: int,
    api: ApiWrapper,
    start_time: int | None = None,
    end_time: int | None = None,
) -> dict:
    report = ReportBuilder(
        api=api,
        log=log,
        fight_id=fight,
        start_time=start_time,
        end_time=end_time,
    )
    try:
        return await report.build()
    except ZeroLengthFightException as ex:
        # FIXME: this is done only for the initial compatibility
        return Response(
            str(ex),
            media_type=MediaType.TEXT,
            status_code=HTTP_400_BAD_REQUEST,
        )


@get('/{0}/health'.format(HEALTHCHECK_TOKEN), media_type=MediaType.HTML)
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


async def api(state: State) -> ApiWrapper:
    return state.api

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
    dependencies={'api': Provide(api)},
)

app = Litestar(
    route_handlers=[base_router],
    on_startup=[connect_api],
    on_shutdown=[close_api],
    debug=DEBUG,
    logging_config=None,
)
