

class Piece:
    """Piece representation
    """
    """Indicate the position in board does not played yet"""
    NONE = '.'

    """Indicate a BLACK piece for game"""
    BLACK = 'x'

    """Indicate a WHITE piece for game"""
    WHITE = 'o'


class Format:
    END     = '\033[0m'
    BOLD    = '\033[1m'

    class Color:
        RED     = '\033[91m'
        GREEN   = '\033[92m'
        YELLOW  = '\033[93m'
        BLUE    = '\033[94m'