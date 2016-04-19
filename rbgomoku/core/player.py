from core import OverwritePositionException
from core.board import Piece

class AIPlayer:
    """ Abstract AI players.
        To construct an AI player:
        Construct an instance (of its subclass) with the game Board
    """
    def __init__(self, board, piece):
        self._board = board
        self.my_piece = piece
        self.opponent = Piece.WHITE if piece == Piece.BLACK else Piece.BLACK

    def play(self, row, col):
        raise NotImplemented

class HumanPlayer(AIPlayer):
    """ Human Player
    """
    def __init__(self, board, piece, first=True):
        super(HumanPlayer, self).__init__(board, piece)
        self.first = not first

    def play(self, row, col):
        if self._board.get_piece(row, col) != Piece.NONE:
            raise OverwritePositionException
        return self._board.play_piece(self.my_piece, row, col)

    def __repr__(self):
        player_number = int(self.first) + 1
        return 'Player {}'.format(player_number)