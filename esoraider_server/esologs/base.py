import asyncio
from typing import Optional

import backoff  # type: ignore
from gql import Client  # type: ignore
from gql.dsl import DSLSchema  # type: ignore
from gql.transport.aiohttp import AIOHTTPTransport  # type: ignore
from gql.transport.exceptions import (  # type: ignore
    TransportClosed,
    TransportQueryError,
)
from loguru import logger
from oauthlib.oauth2 import BackendApplicationClient  # type: ignore
from requests_oauthlib import OAuth2Session  # type: ignore

from esoraider_server.settings import CLIENT_ID, CLIENT_SECRET

WAIT_FOR = 300
TIMEOUT = 10.0


class ApiWrapperBase(object):
    # https://github.com/graphql-python/gql/issues/179#issuecomment-749044193
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
        self._connect_task = None

        self._close_request_event: Optional[asyncio.Event] = None
        self._reconnect_request_event: Optional[asyncio.Event] = None

        self._connected_event: Optional[asyncio.Event] = None
        self._closed_event: Optional[asyncio.Event] = None

        self.ds: DSLSchema = None

    async def connect(self):
        self._close_request_event = asyncio.Event()
        self._reconnect_request_event = asyncio.Event()

        self._connected_event = asyncio.Event()
        self._closed_event = asyncio.Event()

        logger.info('Opening connection')
        if self._connect_task:
            logger.info('Already connected')
        else:
            self._connected_event.clear()
            self._connect_task = asyncio.create_task(self._connection_loop())
            await asyncio.wait_for(
                self._connected_event.wait(), timeout=TIMEOUT,
            )

    async def close(self):
        logger.info('Disconnecting')
        self._connect_task = None
        self._closed_event.clear()
        self._close_request_event.set()
        await asyncio.wait_for(self._closed_event.wait(), timeout=TIMEOUT)

    @backoff.on_exception(backoff.expo, Exception, max_tries=3)
    async def execute(self, *args, **kwargs):
        try:
            answer = await self._session.execute(*args, **kwargs)
        except TransportClosed:
            self._reconnect_request_event.set()
            raise
        except TransportQueryError as ex:
            logger.error(ex)
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

    @backoff.on_exception(backoff.expo, Exception, max_time=WAIT_FOR)
    async def _connection_loop(self):
        while True:
            logger.info('Connecting to API')
            try:
                async with self._client as session:
                    self._session = session
                    self.ds = DSLSchema(self._client.schema)
                    logger.info('Connected to API')
                    self._connected_event.set()

                    # Wait for the close or reconnect event
                    self._close_request_event.clear()
                    self._reconnect_request_event.clear()

                    close_event_task = asyncio.create_task(
                        self._close_request_event.wait(),
                    )
                    reconnect_event_task = asyncio.create_task(
                        self._reconnect_request_event.wait(),
                    )

                    events = [close_event_task, reconnect_event_task]

                    done, pending = await asyncio.wait(
                        events, return_when=asyncio.FIRST_COMPLETED,
                    )

                    for task in pending:
                        task.cancel()

                    if close_event_task in done:
                        # If we received a closed event,
                        # then we go out of the loop
                        break

                    # If we received a reconnect event,
                    # then we disconnect and connect again
            finally:
                self._session = None
                logger.info('Disconnected from API')
        logger.info('Connection closed')
        self._closed_event.set()
