from collections.abc import AsyncIterator
from typing import TypeAlias

import pytest_asyncio
from litestar import Litestar
from litestar.testing import AsyncTestClient

from esoraider_server.app import app

Client: TypeAlias = AsyncTestClient[Litestar]


@pytest_asyncio.fixture(scope='session')
async def test_client() -> AsyncIterator[Client]:
    async with AsyncTestClient(app) as client:
        yield client
