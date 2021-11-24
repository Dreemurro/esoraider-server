import asyncio
from typing import Optional, Tuple

from blacksheep.server import Application
from blacksheep.server.responses import bad_request, json, not_found
from gql.transport.exceptions import TransportQueryError  # type: ignore

from esoraider_server.analysis.report_builder import (
    OutsideOfCombatException,
    ReportBuilder,
    WrongCharException,
)
from esoraider_server.analysis.tracked_info import (
    NothingToTrackException,
    SkillsNotFoundException,
)
from esoraider_server.esologs.api import ApiWrapper, ZeroLengthFightException
from esoraider_server.settings import DEBUG, SHOW_ERROR_DETAILS

app = Application(show_error_details=SHOW_ERROR_DETAILS, debug=DEBUG)

app.use_cors(
    allow_methods='*',
    allow_origins='*',
)


@app.route('/<str:log>')
async def get_log(log: str, api: ApiWrapper):
    response = await api.query_log(log)

    if isinstance(response, TransportQueryError):
        return not_found("This log is either private or doesn't exist")

    return response.get('reportData').get('report')


@app.route('/<str:log>/<int:fight>')
async def get_fight(
    log: str,
    fight: int,
    api: ApiWrapper,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None,
):
    try:
        response = await api.query_table(
            log=log,
            fight_id=fight,
            start_time=start_time,
            end_time=end_time,
        )
    except ZeroLengthFightException as ex:
        return bad_request(str(ex))

    return response.to_json()


@app.route('/<str:log>/<int:fight>/<int:char>')
async def get_char(
    log: str,
    fight: int,
    char: int,
    api: ApiWrapper,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None,
    target: Optional[Tuple[int]] = None,
):
    try:
        response = await api.query_char_table(
            log=log,
            fight_id=fight,
            char_id=char,
            start_time=start_time,
            end_time=end_time,
        )
    except ZeroLengthFightException as ex:
        return bad_request(str(ex))

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
        return json(await report.build())
    except (
        SkillsNotFoundException,
        NothingToTrackException,
        WrongCharException,
        OutsideOfCombatException,
    ) as ex:
        return bad_request(str(ex))


# TODO: Rewrite & probably move to enums
# WIP, check `encounters.py`
@app.route('/encounter/<int:encounter>')
async def get_encounter(encounter, api: ApiWrapper):
    response = await api.query_encounter_info(encounter)

    if response:
        return response.to_json()
    return json('')


@app.route('/fight/<str:log>/<int:fight>')
async def get_fight_effects(
    log: str,
    fight: int,
    api: ApiWrapper,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None,
):
    report = ReportBuilder(
        api=api,
        log=log,
        fight_id=fight,
        start_time=start_time,
        end_time=end_time,
    )
    try:
        return json(await report.build())
    except ZeroLengthFightException as ex:
        return bad_request(str(ex))


async def connect_api(app: Application) -> None:
    api = app.service_provider.get(ApiWrapper)
    await api.connect()


async def configure_background_tasks(app):
    asyncio.get_event_loop().create_task(connect_api(app))


async def close_api(app: Application):
    service = app.service_provider[ApiWrapper]
    await service.close()


app.on_start += configure_background_tasks
app.on_stop += close_api

app.services.add_instance(ApiWrapper())
