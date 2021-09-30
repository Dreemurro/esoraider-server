from data.core import Encounter, EsoEnum, Difficulty, Target


class Encounters(EsoEnum):
    #
    # Asylum Sanctorium
    #
    SAINT_LLOTHIS_THE_PIOUS = Encounter(
        name='Saint Llothis the Pious',
        id=21,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran +1', 123),
            Difficulty('Veteran +2', 124),
        ],
    )
    SAINT_FELMS_THE_BOLD = Encounter(
        name='Saint Felms the Bold',
        id=22,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran +1', 123),
            Difficulty('Veteran +2', 124),
        ],
    )
    SAINT_OLMS_THE_JUST = Encounter(
        name='Saint Olms the Just',
        id=23,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran +1', 123),
            Difficulty('Veteran +2', 124),
        ],
        targets=[
            Target('Saint Olms the Just', (78773,)),
            Target('Minis', (
                79508,  # Saint Felms the Bold
                79507,  # Saint Llothis the Pious
            )),
            Target('Ordinated Protector', (78861,)),
        ]
    )

    #
    # Cloudrest
    #
    SHADE_OF_GALENWE = Encounter(
        name='Shade of Galenwe',
        id=24,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran +1', 123),
            Difficulty('Veteran +2', 124),
            Difficulty('Veteran +3', 125),
        ],
    )
    SHADE_OF_RELEQUEN = Encounter(
        name='Shade of Relequen',
        id=25,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran +1', 123),
            Difficulty('Veteran +2', 124),
            Difficulty('Veteran +3', 125),
        ],
    )
    SHADE_OF_SIRORIA = Encounter(
        name='Shade of Siroria',
        id=26,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran +1', 123),
            Difficulty('Veteran +2', 124),
            Difficulty('Veteran +3', 125),
        ],
    )
    ZMAJA = Encounter(
        name="Z'Maja",
        id=27,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran +1', 123),
            Difficulty('Veteran +2', 124),
            Difficulty('Veteran +3', 125),
        ],
        targets=[
            Target("Z'Maja", (
                83117,  # Z'Maja
                83835,  # Shade of Z'Maja
            )),
            Target('Minis', (
                83607,  # Shade of Galenwe
                83594,  # Shade of Relequen
                83591,  # Shade of Siroria
            )),
        ],
    )

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
            Target('Lokkestiiz', (88342,)),
            Target('Storm Atronach', (90348,)),
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
            Target('Yolnahkriin', (88341,)),
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
            Target('Nahviintaas', (88345,)),
            Target('Adds', (
                88878,  # Alkosh's Fate
                88874,  # Alkosh's Will
                90100,  # Flame Atronach
                88875,  # Fury of Alkosh
                88871,  # Ruin of Alkosh
            )),
        ],
    )
