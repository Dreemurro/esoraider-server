from esoraider_server.data.buffs import Buffs
from esoraider_server.data.core import EsoEnum, Glyph
from esoraider_server.data.debuffs import Debuffs


class Glyphs(EsoEnum):
    CRUSHING = Glyph(
        name='Glyph of Crushing',
        id=28,
        link='https://en.uesp.net/wiki/Online:Glyph_of_Crushing',
        icon='https://images.uesp.net/2/2c/ON-icon-glyph-weapon-Glyph_of_Crushing.png',
        debuffs=[Debuffs.CRUSHER.value],
    )
    WEAKENING = Glyph(
        name='Glyph of Weakening',
        id=32,
        link='https://en.uesp.net/wiki/Online:Glyph_of_Weakening',
        icon='https://images.uesp.net/9/90/ON-icon-glyph-weapon-Glyph_of_Weakening.png',
        debuffs=[Debuffs.WEAKENING.value],
    )
    FLAME = Glyph(
        name='Glyph of Flame',
        id=12,
        link='https://en.uesp.net/wiki/Online:Glyph_of_Flame',
        icon='https://images.uesp.net/4/41/ON-icon-glyph-weapon-Glyph_of_Flame.png',
        debuffs=[Debuffs.BURNING.value],
    )
    POISON = Glyph(
        name='Glyph of Poison',
        id=24,
        link='https://en.uesp.net/wiki/Online:Glyph_of_Poison',
        icon='https://images.uesp.net/9/90/ON-icon-glyph-weapon-Glyph_of_Poison.png',
        debuffs=[Debuffs.POISONED.value],
    )
    BERSERKER = Glyph(
        name='Glyph of Weapon Damage',
        id=5,
        link='https://en.uesp.net/wiki/Online:Glyph_of_Weapon_Damage',
        icon='https://images.uesp.net/d/d4/ON-icon-glyph-weapon-Glyph_of_Weapon_Damage.png',
        buffs=[Buffs.BERSERKER.value],
    )
