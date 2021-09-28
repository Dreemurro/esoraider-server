from data.core import Encounter, EsoEnum, Difficulty, Target


class Encounters(EsoEnum):
    #
    # Sunspire
    #
    LOKKESTIIZ = Encounter(
        name='Lokkestiiz',
        id=43,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran Hard Mode', 122),
        ],
        targets=[
            Target('Lokkestiiz', 88342),
            Target('Storm Atronach', 90348),
        ],
    )
    YOLNAHKRIIN = Encounter(
        name='Yolnahkriin',
        id=44,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran Hard Mode', 122),
        ],
        targets=[
            Target('Yolnahkriin', 88341),
        ],
    )
    NAHVIINTAAS = Encounter(
        name='Nahviintaas',
        id=45,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran Hard Mode', 122),
        ],
        targets=[
            Target('Nahviintaas', 88345),
        ],
    )
