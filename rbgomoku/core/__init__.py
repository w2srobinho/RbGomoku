FACTOR = 100


class ScoreEnum:
    NONE = 0,
    ONE = 1,
    TWO = 2,
    THREE = 3,
    FOUR = 4,
    FIVE = 5


SCORE_POINT = [
    0,
    1,
    100,
    10000,
    1000000,
    50000000000
]


class Piece:
    """Piece representation
    """
    """Indicate the position in board does not played yet"""
    NONE = '.'

    """Indicate a BLACK piece for game"""
    BLACK = 'x'

    """Indicate a WHITE piece for game"""
    WHITE = 'o'
