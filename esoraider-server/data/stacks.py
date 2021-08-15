from data.core import Buff, Debuff, EsoEnum, Stack
from data.debuffs import DEBUFFS
from data.classes.dragonknight.debuffs import DRAGONKNIGHT_DEBUFFS
from data.classes.warden.debuffs import WARDEN_DEBUFFS
from data.classes.templar.debuffs import TEMPLAR_DEBUFFS


class STACKS(EsoEnum):
    """
    Sets
    """
    HUNTERS_FOCUS = Stack(
        name='Hunter\'s Focus',
        id=155150,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_rogue_066.png',
        max_stacks=10,
        type_='Buff',
    )


class BUFFS_WITH_STACKS(EsoEnum):
    """
    Sets
    """
    HUNTERS_FOCUS = Buff(
        name='Hunter\'s Focus',
        id=155150,
        icon='https://assets.rpglogs.com/img/eso/abilities/ability_rogue_066.png',
        stack=STACKS.HUNTERS_FOCUS.value,
    )
