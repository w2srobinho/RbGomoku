import sys

from core import OverwritePositionException
from core.board import BoardSpace, Piece

class AIPlayer:
    """ Abstract AI players.
        To construct an AI player:
        Construct an instance (of its subclass) with the game Board
    """
    def __init__(self, board, piece):
        self._board = board
        self.my_piece = piece
        self.opponent = Piece.WHITE if piece == Piece.BLACK else Piece.BLACK

    def play(self, board_space):
        raise NotImplemented


class HumanPlayer(AIPlayer):
    """ Human Player
    """
    def __init__(self, board, piece, first=True):
        super(HumanPlayer, self).__init__(board, piece)
        self.first = not first

    def play(self, board_space):
        if self._board.get_piece(board_space) != Piece.NONE:
            raise OverwritePositionException
        return self._board.take_up_space(self.my_piece, board_space)

    def __repr__(self):
        player_number = int(self.first) + 1
        return 'Player {}'.format(player_number)


class MachinePlayer(AIPlayer):
    """ Machine Player
    """
    def __init__(self, board, piece):
        super(MachinePlayer, self).__init__(board, piece)

    def play(self, board_space):
        if self._board.get_piece(board_space) != Piece.NONE:
            raise OverwritePositionException
        return self._board.take_up_space(self.my_piece, board_space)

    def minimax(self, level):
        return self._minimax(level, self.my_piece)

    def _minimax(self, level, player):
        current_score = 0
        best_movement = BoardSpace(-1, -1)
        best_score = -sys.maxsize if (player == self.my_piece) else sys.maxsize

        if level == 0:
            return (self._board.current_score, best_movement)

        for row in range(len(self._board)):
            for col in range(len(self._board)):
                current_movement = BoardSpace(row, col)
                if self._board.get_piece(current_movement) != Piece.NONE:
                    continue

                previous_score = self._board.current_score
                self._board.take_up_space(player, current_movement)

                if player == self.my_piece: # me
                    current_score, _ = self._minimax(level - 1, self.opponent)
                    if current_score > best_score:
                        best_score = current_score
                        best_movement = current_movement
                else: # opponent
                    current_score, _ = self._minimax(level - 1, self.my_piece)
                    if current_score < best_score:
                        best_score = current_score
                        best_movement = current_movement
                # undo move
                self._board.restore_move(current_movement, previous_score)

        return (best_score, best_movement)


    """
        minimax(level, player, alpha, beta)  // player may be "computer" or "opponent"
        if (gameover || level == 0)
           return score
        children = all valid moves for this "player"
        if (player is computer, i.e., max's turn)
           // Find max and store in alpha
           for each child
              score = minimax(level - 1, opponent, alpha, beta)
              if (score > alpha) alpha = score
              if (alpha >= beta) break;  // beta cut-off
           return alpha
        else (player is opponent, i.e., min's turn)
           // Find min and store in beta
           for each child
              score = minimax(level - 1, computer, alpha, beta)
              if (score < beta) beta = score
              if (alpha >= beta) break;  // alpha cut-off
           return beta

        // Initial call with alpha=-inf and beta=inf
        minimax(2, computer, -inf, +inf)
    """
    def minimax_pruning(self, level):
        infinite = sys.maxsize
        return self._minimax_pruning(level, self.my_piece, -infinite, infinite)

    def _minimax_pruning(self, level, player, alpha, beta):
        score = 0
        best_movement = BoardSpace(-1, -1)

        if level == 0:
            return (self._board.current_score, best_movement)

        for row in range(len(self._board)):
            for col in range(len(self._board)):
                current_movement = BoardSpace(row, col)
                if self._board.get_piece(current_movement) != Piece.NONE:
                    continue

                previous_score = self._board.current_score
                self._board.take_up_space(player, current_movement)

                if player == self.my_piece: # me
                    score, _ = self._minimax_pruning(level - 1, self.opponent, alpha, beta)
                    if score > alpha:
                        alpha = score
                        best_movement = current_movement
                else: # opponent
                    score, _ = self._minimax_pruning(level - 1, self.my_piece, alpha, beta)
                    if score < beta:
                        beta = score
                        best_movement = current_movement
                # undo move
                self._board.restore_move(current_movement, previous_score)

                if (alpha >= beta):
                    break

        score_return = alpha if player == self.my_piece else beta
        return (score_return, best_movement)


    def __repr__(self):
        return 'Machine'
