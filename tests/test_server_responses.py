from contextlib import suppress
from dataclasses import dataclass
from http import HTTPStatus
from json import JSONDecodeError
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from msgspec import json

if TYPE_CHECKING:
    from httpx import Response

    from tests.conftest import Client


@dataclass
class Log:
    desc: str
    log: str
    fight: int | None = None
    char: int | None = None
    targets: tuple[int, ...] | None = None
    expected: HTTPStatus = HTTPStatus.OK

    @property
    def link(self) -> str:
        link = '/{0}'.format(self.log)
        if self.fight:
            link += '/{0}'.format(self.fight)
        if self.fight and self.char:
            link += '/{0}'.format(self.char)
        return link

    @property
    def query(self) -> dict[str, list[int]] | None:
        return {'target': list(self.targets)} if self.targets else None

    @property
    def response(self) -> dict | None:
        if self.expected != HTTPStatus.OK:
            return None
        path = self.log.replace(':', '-')
        if self.fight:
            path = '{path}-{fight}'.format(path=path, fight=self.fight)
        if self.fight and self.char:
            path = '{path}-{char}'.format(path=path, char=self.char)
        if self.fight and self.char and self.targets:
            path = '{path}-targets'.format(path=path)
        return json.decode(
            Path('tests/files/log_{path}.json'.format(path=path)).read_bytes(),
        )


LOGS = (
    Log(
        desc='Log w/o issues',
        log='MRrz4bhfc8FGxmBT',
    ),
    Log(
        desc='Log in anonymous mode',
        log='a:xJa4CgrcfvLFdVKT',
    ),
    Log(
        desc='Nonexistent log',
        log='0123456789101112',
        expected=HTTPStatus.NOT_FOUND,
    ),
)

FIGHTS = (
    Log(
        desc='Fight w/o issues',
        log='a:xJa4CgrcfvLFdVKT',
        fight=5,
    ),
    Log(
        desc='No specs on anon char',
        log='a:xJa4CgrcfvLFdVKT',
        fight=3,  # Player (10) has no specs
    ),
    Log(
        desc='Zero-length trash fight',
        log='XmB7YQbrjD6p8x4n',
        fight=18,
        expected=HTTPStatus.BAD_REQUEST,
    ),
)

FIGHT_EFFECTS = (
    Log(
        desc='Fight w/o issues',
        log='XmB7YQbrjD6p8x4n',
        fight=97,
    ),
    Log(
        desc='Zero-length trash fight',
        log='XmB7YQbrjD6p8x4n',
        fight=18,
        expected=HTTPStatus.BAD_REQUEST,
    ),
)

CHARS = (
    Log(
        desc='Char w/o issues',
        log='XmB7YQbrjD6p8x4n',
        fight=35,
        char=2,
    ),
    Log(
        desc='Targets provided',
        log='XmB7YQbrjD6p8x4n',
        fight=35,
        char=2,
        targets=(88878, 88874, 90100, 88875, 88871),  # Adds on Nahvi
    ),
    Log(
        desc='Anon char outside of fight',
        log='MRrz4bhfc8FGxmBT',
        fight=3,
        char=8,
        expected=HTTPStatus.BAD_REQUEST,
    ),
    Log(
        desc='Char from zero-length trash fight',
        log='a:BqFVw84HZAr2hLy7',
        fight=1,
        char=7,
        expected=HTTPStatus.BAD_REQUEST,
    ),
    Log(
        desc='Char w/o skills & gear',
        log='XmB7YQbrjD6p8x4n',
        fight=106,
        char=4,
        expected=HTTPStatus.BAD_REQUEST,
    ),
)


@dataclass
class Encounter:
    desc: str
    id: int
    expected: HTTPStatus = HTTPStatus.OK
    is_empty: bool = False

    @property
    def link(self) -> str:
        return '/{id}'.format(id=self.id)

    @property
    def response(self) -> str | dict | None:
        if self.expected != HTTPStatus.OK:
            return None
        if self.is_empty:
            return ''
        return json.decode(
            Path(
                'tests/files/encounter_{id}.json'.format(id=self.id),
            ).read_bytes(),
        )


ENCOUNTERS = (
    Encounter(desc='Yolnahkriin', id=44),
    Encounter(desc='Related to Rockgrove', id=132737, is_empty=True),
)


def id_of_test(log: Log | Encounter) -> str:
    return log.desc


def get_json(response: 'Response') -> dict | None:
    with suppress(JSONDecodeError):
        return response.json()
    return None


@pytest.mark.asyncio(loop_scope='session')
@pytest.mark.parametrize('log', LOGS, ids=id_of_test)
async def test_get_log(test_client: 'Client', log: Log):
    response = await test_client.get(log.link)

    assert response.status_code == log.expected
    assert get_json(response) == log.response


@pytest.mark.asyncio(loop_scope='session')
@pytest.mark.parametrize('fight', FIGHTS, ids=id_of_test)
async def test_get_fight(test_client: 'Client', fight: Log):
    response = await test_client.get(fight.link)

    assert response.status_code == fight.expected
    assert len(get_json(response) or {}) == len(fight.response or {})


@pytest.mark.asyncio(loop_scope='session')
@pytest.mark.parametrize('char', CHARS, ids=id_of_test)
async def test_get_char(test_client: 'Client', char: Log):
    response = await test_client.get(char.link, params=char.query)

    assert response.status_code == char.expected
    assert len(get_json(response) or {}) == len(char.response or {})


@ pytest.mark.asyncio(loop_scope='session')
@ pytest.mark.parametrize('fight', FIGHT_EFFECTS, ids=id_of_test)
async def test_get_fight_effects(test_client: 'Client', fight: Log):
    response = await test_client.get('/fight{0}'.format(fight.link))

    assert response.status_code == fight.expected
    assert get_json(response) == fight.response


@ pytest.mark.asyncio(loop_scope='session')
@ pytest.mark.parametrize('encounter', ENCOUNTERS, ids=id_of_test)
async def test_get_encounter_info(test_client: 'Client', encounter: Encounter):
    response = await test_client.get('/encounter{0}'.format(encounter.link))

    assert response.status_code == HTTPStatus.OK
    assert get_json(response) or '' == encounter.response
