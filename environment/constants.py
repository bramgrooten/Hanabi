import random
from enum import Enum
from colorama import Fore, Style

COLOR_STRING = list('RGBWYM')


class Colors(Enum):
    RED = 'R'
    GREEN = 'G'
    LIGHTBLUE_EX = 'B'
    BLACK = 'W'  # This is more white, than actual White (which is more gray)
    LIGHTYELLOW_EX = 'Y'
    MAGENTA = 'M'

    @staticmethod
    def get(color: 'Colors') -> str:
        """ Returns the color value in the right color.  """
        return getattr(Fore, color.name) + Style.BRIGHT + color.value + Style.RESET_ALL

    @staticmethod
    def index(color: 'Colors') -> int:
        """ Return the index of a color object.  """
        return COLOR_STRING.index(color.value)

    @staticmethod
    def color(index: int) -> 'Colors':
        """ Return a Colors object, based on an index.  """
        return [color for color in Colors if color.value == COLOR_STRING[index]].pop(0)


class Rank(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    @staticmethod
    def get(rank: 'Rank') -> str:
        """ Return the rank in uniform formatting. """
        return getattr(Fore, Colors.BLACK.name) + Style.BRIGHT + rank.value + Style.RESET_ALL


class Actions:
    id: int = None
    index: int = None
    player: int = None

    def __init__(self, action_id, index, player=None):
        self.id = action_id
        self.index = index
        self.player = player

    def __str__(self):
        return f"Actions: (id={self.id}, index={self.index}, player={self.player})"

    def __repr__(self):
        return f"<class {self.__str__()}>"

    @classmethod
    def PLAY(cls, index, *args, **kwargs) -> 'Actions':
        return cls(action_id=0, index=index)

    @classmethod
    def INFORM_COLOR(cls, index, player) -> 'Actions':
        return cls(action_id=1, index=index, player=player)

    @classmethod
    def INFORM_RANK(cls, index, player) -> 'Actions':
        return cls(action_id=2, index=index, player=player)

    @classmethod
    def DISCARD(cls, index, *args, **kwargs) -> 'Actions':
        return cls(action_id=3, index=index)

    @staticmethod
    def sample(hand_size: int, players: int, hints: int) -> 'Actions':
        action = random.choice([Actions.PLAY, Actions.DISCARD])
        if hints:
            action = random.choice([Actions.PLAY, Actions.INFORM_COLOR, Actions.INFORM_RANK, Actions.DISCARD])
        return action(index=random.randint(1, hand_size - 1), player=random.randint(0, players - 1))
