from view import Piece

class AIPlayer:
    """ Abstract AI players.
        To construct an AI player:
        Construct an instance (of its subclass) with the game Board
    """
    def __init__(self, board):
        self._board = board
        self.my_piece = Piece.BLACK
        self.opponent = Piece.WHITE

    # Abstract method to get next move. Return int[2] of {row, col} */
    def play(self, row, col):
        raise NotImplemented

class HumanPlayer:
    """ Human Player
    """
    def __init__(self, board):
        super(HumanPlayer, self).__init__(board)

    def play(self, row, col):
        self._board.play(row, col)
        self._board.has_winner()
        return self._board.winner
