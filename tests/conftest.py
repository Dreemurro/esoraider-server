import asyncio

import pytest
from blacksheep.testing import TestClient

from esoraider_server.app import app as app_server


@pytest.fixture(scope='session')
def event_loop(request):
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
async def api():
    await app_server.start()
    await asyncio.sleep(3)  # Wait for API connection
    yield app_server
    await app_server.stop()


@pytest.fixture(scope='session')
async def test_client(api):
    return TestClient(api)
