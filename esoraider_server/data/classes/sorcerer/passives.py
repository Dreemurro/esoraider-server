from esoraider_server.data.core import Buff, EsoEnum


class SORCERER_PASSIVES(EsoEnum):
    # Daedric Summoning
    REBATE = Buff(
        name='Rebate',
        id=45198,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_056.png',
        link='https://eso-hub.com/en/skills/sorcerer/daedric-summoning/rebate',
    )
    EXPERT_SUMMONER = Buff(
        name='Expert Summoner',
        id=45199,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_019.png',
        link='https://eso-hub.com/en/skills/sorcerer/daedric-summoning/expert-summoner',
    )

    # Dark Magic
    BLOOD_MAGIC = Buff(
        name='Blood Magic',
        id=45172,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_026.png',
        link='https://eso-hub.com/en/skills/sorcerer/dark-magic/blood-magic',
    )
    PERSISTENCE = Buff(  # Activates on block, can be not detected
        name='Persistence',
        id=108862,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_054.png',
        link='https://eso-hub.com/en/skills/sorcerer/dark-magic/persistence',
    )
    EXPLOITATION = Buff(
        name='Exploitation',
        id=45181,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_039.png',
        link='https://eso-hub.com/en/skills/sorcerer/dark-magic/exploitation',
    )

    # Storm Calling
    ENERGIZED = Buff(
        name='Energized',
        id=45190,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_sorcerer_015.png',
        link='https://eso-hub.com/en/skills/sorcerer/storm-calling/energized',
    )
