from aioauth_client import OAuth2Client
from gql import Client  # type: ignore
from gql.dsl import DSLSchema  # type: ignore
from gql.transport.aiohttp import AIOHTTPTransport  # type: ignore
from gql.transport.exceptions import TransportQueryError  # type: ignore
from structlog.stdlib import get_logger

from esoraider_server.settings import CLIENT_ID, CLIENT_SECRET

logger = get_logger()


class ApiWrapperBase(object):
    def __init__(self) -> None:
        self._client: Client | None = None
        self._session = None
        self.ds: DSLSchema = None

    async def connect(self):
        await logger.ainfo('Opening connection')
        self._client = await self._create_client()
        self._session = await self._client.connect_async(reconnecting=True)
        self.ds = DSLSchema(self._client.schema)
        await logger.ainfo('Connected to API')

    async def close(self):
        await logger.ainfo('Disconnecting')
        self._session = None
        await self._client.close_async()
        await logger.ainfo('Disconnected')

    async def execute(self, *args, **kwargs):
        try:
            answer = await self._session.execute(*args, **kwargs)
        except TransportQueryError as ex:
            await logger.aexception("Couldn't get the log")
            return ex

        return answer

    async def _create_client(self) -> Client:
        token = await self._get_access_token()
        return Client(
            transport=AIOHTTPTransport(
                url='https://www.esologs.com/api/v2/client',
                headers={'Authorization': 'Bearer {0}'.format(token)},
            ),
            fetch_schema_from_transport=True,
        )

    async def _get_access_token(self) -> str:
        url = 'https://www.esologs.com/oauth/{0}'
        client = OAuth2Client(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            authorize_url=url.format('authorize'),
            access_token_url=url.format('token'),
        )
        token, _ = await client.get_access_token(
            '', grant_type='client_credentials',
        )
        return token
