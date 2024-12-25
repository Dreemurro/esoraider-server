from typing import Annotated

from litestar.datastructures import State
from litestar.params import Dependency

from esoraider_server import usecases
from esoraider_server.esologs.api import ApiWrapper


async def api(state: State) -> ApiWrapper:
    return state.api


async def get_log_use_case(
    api: ApiWrapper,
) -> usecases.GetLogUseCase:
    return usecases.GetLogUseCase(api)


async def get_fight_use_case(
    api: ApiWrapper,
) -> usecases.GetFightUseCase:
    return usecases.GetFightUseCase(api)


async def get_char_use_case(
    api: ApiWrapper,
) -> usecases.GetCharUseCase:
    return usecases.GetCharUseCase(api)


async def get_encounter_use_case(
    api: ApiWrapper,
) -> usecases.GetEncounterUseCase:
    return usecases.GetEncounterUseCase(api)


async def get_fight_effects_use_case(
    api: ApiWrapper,
) -> usecases.GetFightEffectsUseCase:
    return usecases.GetFightEffectsUseCase(api)

################################################################################

UseCaseGetLog = Annotated[
    usecases.GetLogUseCase, Dependency(),
]
UseCaseGetFight = Annotated[
    usecases.GetFightUseCase, Dependency(),
]
UseCaseGetChar = Annotated[
    usecases.GetCharUseCase, Dependency(),
]
UseCaseGetEncounter = Annotated[
    usecases.GetEncounterUseCase, Dependency(),
]
UseCaseGetFightEffects = Annotated[
    usecases.GetFightEffectsUseCase, Dependency(),
]
