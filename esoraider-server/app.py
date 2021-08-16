import asyncio

from blacksheep.server import Application
from blacksheep.server.responses import json, not_found
from gql.transport.exceptions import TransportQueryError

from analysis.report_builder import ReportBuilder
from api.api import ApiWrapper
from api.response import SummaryTableData
from settings import DEBUG, SHOW_ERROR_DETAILS

app = Application(show_error_details=SHOW_ERROR_DETAILS, debug=DEBUG)

app.use_cors(
    allow_methods="*",
    allow_origins="*",
    # allow_headers="* Authorization",
    # max_age=300,
)


@app.route('/<str:log>')
async def get_log(log: str, api: ApiWrapper):
    response = await api.query_log(log)

    if type(response) is TransportQueryError:
        return not_found('This log is either private or doesn\'t exist')

    return response.get('reportData').get('report')


@app.route('/<str:log>/<int:fight>')
async def get_fight(
    log: str,
    fight: int,
    api: ApiWrapper,
    start_time: str = None,
    end_time: str = None,
):
    response = await api.query_table(
        log=log,
        fight_id=fight,
        start_time=start_time,
        end_time=end_time,
    )
    response = response.get('reportData')
    response = response.get('report')
    response = response.get('table')
    response = response.get('data')

    return response


@app.route('/<str:log>/<int:fight>/<int:char>')
async def get_char(
    log: str,
    fight: int,
    char: int,
    api: ApiWrapper,
    start_time: str = None,
    end_time: str = None,
):
    response = await api.query_char_table(
        log=log,
        fight_id=fight,
        char_id=char,
        start_time=start_time,
        end_time=end_time,
    )
    response = response.get('reportData')
    response = response.get('report')
    response = response.get('table')
    response = response.get('data')

    decoded = SummaryTableData.from_dict(response)
    report = ReportBuilder(
        api=api,
        log=log,
        fight_id=fight,
        char_id=char,
        summary_table=decoded,
        start_time=start_time,
        end_time=end_time,
    )
    r = await report.build()

    return json(r)


# TODO: Rewrite & probably move to enums
@app.route('/encounter/<int:encounter>')
async def get_encounter(encounter, api: ApiWrapper):
    response = await api.query_name(encounter)
    response = response.get('worldData')
    response = response.get('encounter')

    if response:
        return response
    return json('')


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
