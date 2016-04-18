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

    # Abstract method to get next move. Return int[2] of {row, col} */
    def play(self, row, col):
        raise NotImplemented

class HumanPlayer(AIPlayer):
    """ Human Player
    """
    def __init__(self, board, piece):
        super(HumanPlayer, self).__init__(board, piece)

    def play(self, row, col):
        self._board.play_piece(self.my_piece, row, col)
        self._board.has_winner(self.my_piece, row, col)
        return self._board.winner
