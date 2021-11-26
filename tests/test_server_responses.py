from typing import Optional

import pytest
from attr import dataclass
from blacksheep.testing import TestClient


@dataclass
class TestLog:
    desc: str
    log: str
    fight: Optional[int] = None
    char: Optional[int] = None
    expected: int = 200

    @property
    def link(self) -> str:
        link = '/{0}'.format(self.log)
        if self.fight:
            link += '/{0}'.format(self.fight)
        if self.fight and self.char:
            link += '/{0}'.format(self.char)
        return link


LOGS = (
    TestLog(
        desc='Log w/o issues',
        log='b7jT1yp2fz8J9PWc',
    ),
    TestLog(
        desc='Log in anonymous mode',
        log='a:NWBcJ9DYMRLPFkjz',
    ),
    TestLog(
        desc='Nonexistent log',
        log='0123456789101112',
        expected=404,
    ),
)

FIGHTS = (
    TestLog(
        desc='Fight w/o issues',
        log='a:NWBcJ9DYMRLPFkjz',
        fight=4,
    ),
    TestLog(
        desc='No specs on anon char',
        log='a:PB2xAGyCRHbrXwca',
        fight=21,
    ),
    TestLog(
        desc='Zero-length trash fight',
        log='a:BqFVw84HZAr2hLy7',
        fight=1,
        expected=400,
    ),
)

FIGHT_EFFECTS = (
    TestLog(
        desc='Fight w/o issues',
        log='a:NWBcJ9DYMRLPFkjz',
        fight=4,
    ),
    TestLog(
        desc='Zero-length trash fight',
        log='a:BqFVw84HZAr2hLy7',
        fight=1,
        expected=400,
    ),
)

CHARS = (
    TestLog(
        desc='Char w/o issues',
        log='a:NWBcJ9DYMRLPFkjz',
        fight=4,
        char=231,
    ),
    TestLog(
        desc='Anon char outside of fight',
        log='a:PB2xAGyCRHbrXwca',
        fight=21,
        char=127,
        expected=400,
    ),
    TestLog(
        desc='Char from zero-length trash fight',
        log='a:BqFVw84HZAr2hLy7',
        fight=1,
        char=7,
        expected=400,
    ),
    TestLog(
        desc='Char w/o skills & gear',
        log='a:br83pxTLvt67fJnH',
        fight=40,
        char=143,
        expected=400,
    ),
)

ENCOUNTERS = (
    44,  # Yolnahkriin
    132737,  # Related to Rockgrove, returns nothing
)


def id_of_test(log: TestLog) -> str:
    return log.desc


@pytest.mark.asyncio
@pytest.mark.parametrize('log', LOGS, ids=id_of_test)
async def test_get_log(test_client: TestClient, log: TestLog):
    response = await test_client.get(log.link)

    assert response.status == log.expected


@pytest.mark.asyncio
@pytest.mark.parametrize('fight', FIGHTS, ids=id_of_test)
async def test_get_fight(test_client: TestClient, fight: TestLog):
    response = await test_client.get(fight.link)

    assert response.status == fight.expected


@pytest.mark.asyncio
@pytest.mark.parametrize('char', CHARS, ids=id_of_test)
async def test_get_char(test_client: TestClient, char: TestLog):
    response = await test_client.get(char.link)

    assert response.status == char.expected


@pytest.mark.asyncio
@pytest.mark.parametrize('fight', FIGHT_EFFECTS, ids=id_of_test)
async def test_get_fight_effects(test_client: TestClient, fight: TestLog):
    response = await test_client.get('/fight' + fight.link)

    assert response.status == fight.expected


@pytest.mark.asyncio
@pytest.mark.parametrize('encounter', ENCOUNTERS)
async def test_get_encounter_info(test_client: TestClient, encounter: int):
    response = await test_client.get('/encounter/{0}'.format(encounter))

    assert response.status == 200
