from dataclasses import dataclass
from http import HTTPStatus
from typing import Optional, Sequence, Tuple

import pytest
from blacksheep.testing import TestClient


@dataclass
class Log:
    desc: str
    log: str
    fight: Optional[int] = None
    char: Optional[int] = None
    targets: Optional[Sequence[int]] = None
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
    def query(self) -> Optional[Sequence[Tuple[str, str]]]:
        if self.targets:
            return [('target', str(_)) for _ in self.targets]
        return None


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

ENCOUNTERS = (
    44,  # Yolnahkriin
    132737,  # Related to Rockgrove, returns nothing
)


def id_of_test(log: Log) -> str:
    return log.desc


@pytest.mark.asyncio(loop_scope='session')
@pytest.mark.parametrize('log', LOGS, ids=id_of_test)
async def test_get_log(test_client: TestClient, log: Log):
    response = await test_client.get(log.link)

    assert response.status == log.expected


@pytest.mark.asyncio(loop_scope='session')
@pytest.mark.parametrize('fight', FIGHTS, ids=id_of_test)
async def test_get_fight(test_client: TestClient, fight: Log):
    response = await test_client.get(fight.link)

    assert response.status == fight.expected


@pytest.mark.asyncio(loop_scope='session')
@pytest.mark.parametrize('char', CHARS, ids=id_of_test)
async def test_get_char(test_client: TestClient, char: Log):
    response = await test_client.get(char.link, query=char.query)

    assert response.status == char.expected


@pytest.mark.asyncio(loop_scope='session')
@pytest.mark.parametrize('fight', FIGHT_EFFECTS, ids=id_of_test)
async def test_get_fight_effects(test_client: TestClient, fight: Log):
    response = await test_client.get('/fight' + fight.link)

    assert response.status == fight.expected


@pytest.mark.asyncio(loop_scope='session')
@pytest.mark.parametrize('encounter', ENCOUNTERS)
async def test_get_encounter_info(test_client: TestClient, encounter: int):
    response = await test_client.get('/encounter/{0}'.format(encounter))

    assert response.status == HTTPStatus.OK
