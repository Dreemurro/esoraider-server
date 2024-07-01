from gql import Client  # type: ignore
from gql.dsl import DSLSchema  # type: ignore
from gql.transport.aiohttp import AIOHTTPTransport  # type: ignore
from gql.transport.exceptions import TransportQueryError  # type: ignore
from loguru import logger
from oauthlib.oauth2 import BackendApplicationClient  # type: ignore
from requests_oauthlib import OAuth2Session  # type: ignore

from esoraider_server.settings import CLIENT_ID, CLIENT_SECRET

WAIT_FOR = 300
TIMEOUT = 10.0


class ApiWrapperBase(object):
    def __init__(self) -> None:
        self._token = self._auth()
        self._transport = AIOHTTPTransport(
            url='https://www.esologs.com/api/v2/client',
            headers={'Authorization': 'Bearer {0}'.format(self._token)},
        )
        self._client = Client(
            transport=self._transport,
            fetch_schema_from_transport=True,
        )
        self._session = None
        self.ds: DSLSchema = None

    async def connect(self):
        logger.info('Opening connection')
        self._session = await self._client.connect_async(reconnecting=True)
        self.ds = DSLSchema(self._client.schema)
        logger.info('Connected to API')

    async def close(self):
        logger.info('Disconnecting')
        self._session = None
        await self._client.close_async()
        logger.info('Disconnected')

    async def execute(self, *args, **kwargs):
        try:
            answer = await self._session.execute(*args, **kwargs)
        except TransportQueryError as ex:
            logger.exception("Couldn't get the log")
            return ex

        return answer

    def _auth(self):
        access_token_url = 'https://www.esologs.com/oauth/token'

        client = BackendApplicationClient(client_id=CLIENT_ID)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(
            token_url=access_token_url,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
        )
        return token['access_token']
