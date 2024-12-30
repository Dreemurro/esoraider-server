from esoraider_server.data.core import Difficulty, Encounter, EsoEnum, Target


class Encounters(EsoEnum):
    #
    # Maw of Lorkhaj
    #
    ZHAJHASSA_THE_FORGOTTEN = Encounter(
        name="Zhaj'hassa The Forgotten",
        id=13,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran Hard Mode', 122),
        ],
        targets=[
            Target("Zhaj'hassa The Forgotten", (60005,)),
        ],
    )
    THE_TWINS = Encounter(
        name='The Twins',
        id=14,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran Hard Mode', 122),
        ],
        targets=[
            Target('Vashai', (60374,)),
            Target("S'kinrai", (60375,)),
        ],
    )
    RAKKHAT = Encounter(
        name='Rakkhat',
        id=15,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran Hard Mode', 122),
        ],
        targets=[
            Target('Rakkhat', (60437,)),
        ],
    )

    #
    # Halls of Fabrication
    #
    THE_HUNTER_KILLERS = Encounter(
        name='The Hunter Killers',
        id=16,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran Hard Mode', 122),
        ],
        targets=[
            Target('Hunter-Killer Negatrix', (76597,)),
            Target('Hunter-Killer Positrox', (76664,)),
        ],
    )
    PINNACLE_FACTOTUM = Encounter(
        name='Pinnacle Factotum',
        id=17,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran Hard Mode', 122),
        ],
        targets=[
            Target('Pinnacle Factotum', (76660,)),
        ],
    )
    ARCHCUSTODIAN = Encounter(
        name='Archcustodian',
        id=18,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran Hard Mode', 122),
        ],
        targets=[
            Target('Archcustodian', (76729,)),
        ],
    )
    THE_REFABRICATION_COMMITTEE = Encounter(
        name='The Refabrication Committee',
        id=19,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran Hard Mode', 122),
        ],
        targets=[
            Target('Reactor', (76766,)),
            Target('Reclaimer', (77312,)),
            Target('Reducer', (76768,)),
        ],
    )
    ASSEMBLY_GENERAL = Encounter(
        name='Assembly General',
        id=20,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran Hard Mode', 122),
        ],
        targets=[
            Target('Assembly General', (76600,)),
            Target(
                'Adds',
                (
                    78538,  # Calefactor
                    78537,  # Capacitor
                    77464,  # Tactical Facsimile
                ),
            ),
        ],
    )

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
            Target(
                'Minis',
                (
                    79508,  # Saint Felms the Bold
                    79507,  # Saint Llothis the Pious
                ),
            ),
            Target('Ordinated Protector', (78861,)),
        ],
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
            Target(
                "Z'Maja",
                (
                    83117,  # Z'Maja
                    83835,  # Shade of Z'Maja
                ),
            ),
            Target(
                'Minis',
                (
                    83607,  # Shade of Galenwe
                    83594,  # Shade of Relequen
                    83591,  # Shade of Siroria
                ),
            ),
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
            Target(
                'Adds',
                (
                    88878,  # Alkosh's Fate
                    88874,  # Alkosh's Will
                    90100,  # Flame Atronach
                    88875,  # Fury of Alkosh
                    88871,  # Ruin of Alkosh
                ),
            ),
        ],
    )

    #
    # Kyne's Aegis
    #
    YANDIR_THE_BUTCHER = Encounter(
        name='Yandir the Butcher',
        id=46,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran Hard Mode', 122),
        ],
        targets=[
            Target('Yandir the Butcher', (94771,)),
        ],
    )
    CAPTAIN_VROL = Encounter(
        name='Captain Vrol',
        id=47,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran Hard Mode', 122),
        ],
        targets=[
            Target('Captain Vrol', (94772,)),
        ],
    )
    LORD_FALGRAVN = Encounter(
        name='Lord Falgravn',
        id=48,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran Hard Mode', 122),
        ],
        targets=[
            Target('Lord Falgravn', (94773,)),
        ],
    )

    #
    # Rockgrove
    #
    OAXILTSO = Encounter(
        name='Oaxiltso',
        id=49,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran Hard Mode', 122),
        ],
        targets=[
            Target('Oaxiltso', (101793,)),
        ],
    )
    FLAME_HERALD_BAHSEI = Encounter(
        name='Flame-Herald Bahsei',
        id=50,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran Hard Mode', 122),
        ],
        targets=[
            Target('Flame-Herald Bahsei', (101794,)),
        ],
    )
    XALVAKKA = Encounter(
        name='Xalvakka',
        id=51,
        difficulties=[
            Difficulty('Normal', 120),
            Difficulty('Veteran', 121),
            Difficulty('Veteran Hard Mode', 122),
        ],
        targets=[
            Target('Xalvakka', (101797,)),
        ],
    )
