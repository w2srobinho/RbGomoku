import math
import numpy as np
from core import Piece, ScoreEnum, SCORE_POINT
from core.exceptions import NotBlankSpaceException

class Square:
    """ This is the abstraction of position in border
    """
    def __init__(self, row, col):
        """ The position
        :param row: is the row number in border
        :param col: is the column number in border
        """
        self.row = row
        self.col = col

    def __eq__(self, other):
        """ Compare the positions
        :param other: The position to compare
        :return: True if equals, False otherwise
        """
        return self.row == other.row and self.col == other.col


class Board:
    """ Board representation of the console game
    """

    def __init__(self, size, sequence_victory):
        """ Start the Board with empty positions
        :param size: size of board sizeXsize format
        :param sequence_victory: number of piece in sequence to see victory
        """
        self.size = size
        self.score = 0
        self._table = np.chararray((size, size))
        self._table[:] = Piece.NONE
        self._table = self._table.astype(np.str)
        self._sequence_victory = sequence_victory

    def __len__(self):
        """
        :return: length of border
        """
        return self.size

    def __eq__(self, other):
        """ Compare borders
        :param other:
        :return:
        """
        size_equals = self.size == len(other)
        sequence_victory_equals = self._sequence_victory == other._sequence_victory
        score_equals = self.score == other.current_score
        table_equals = np.array_equal(self._table, other.table)
        return size_equals and sequence_victory_equals and score_equals and table_equals

    def __repr__(self):
        """ Format the boarder
        :return: the board in str format
        """
        table_copy = self._table.tolist()
        formatter = ' '.join(['{' + str(i) + ':^2}' for i in range(self.size + 1)])
        range_table = range(self.size)
        idx_table = list(range_table)

        ## top index table ##
        idx_table_str = [str(n) for n in idx_table]
        top_idx_table_str = [' '] + idx_table_str
        top_idx_f = formatter.format(*top_idx_table_str)

        ## left index table ##
        left_idx_table = [[str(i)] + table_copy[i] for i in range_table]
        left_idx_table_f = [formatter.format(*line) for line in left_idx_table]

        str_table = '\n'.join([top_idx_f] + left_idx_table_f)
        return str_table

    def get_piece(self, board_space):
        return self._table[board_space.row, board_space.col]

    def take_up_space(self, piece, board_space):
        """ Current movement in border

        :param piece: the piece played
        :param board_space: is a position played in matrix ex. BoardSpace(row, col)
        :return: the winner or Piece.NONE if no there winner
        """
        self._table[board_space.row, board_space.col] = piece
        winner = self.has_winner(piece, board_space)
        if self._table.count(Piece.NONE).sum() == 0 and winner == Piece.NONE:
            raise NotBlankSpaceException
        return winner

    def restore_move(self, board_space, score):
        self._table[board_space.row, board_space.col] = Piece.NONE
        self.score = score

    @property
    def table(self):
        return self._table

    @property
    def current_score(self):
        return self.score

    def has_winner(self, piece, board_space):
        """ Search for winner play in border

        :param piece: represent current piece played
        :param board_space: is a position played in matrix ex. BoardSpace(row, col)
        :return: the current winner if there or Piece.NONE if no there winner
        """
        if self._search_diagonal(piece, board_space):
            """ Faz verificação da diagonal no sentido da diagonal principal
                se ocorrer uma vitória na diagonal atual
                escreve a peça ganhadora e retorna verdadeiro
            """
            return piece

        if self._search_opposite_diagonal(piece, board_space):
            """ Faz verificação da diagonal no sentido da diagonal secundária
                se ocorrer uma vitória na diagonal atual
                escreve a peça ganhadora e retorna verdadeiro
            """
            return piece

        if self._search_line(piece, board_space):
            """ Faz verificação por linha
                se ocorrer uma vitória na linha atual
                escreve a peça ganhadora e retorna verdadeiro
            """
            return piece

        if self._search_column(piece, board_space):
            """ Faz verificação por linha
                se ocorrer uma vitória na linha atual
                escreve a peça ganhadora e retorna verdadeiro
            """
            return piece

        return Piece.NONE

    def heuristic_move_score(self, piece, line):
        score_factor = 1 if piece == Piece.BLACK else -1
        opponent = Piece.WHITE if piece == Piece.BLACK else Piece.BLACK
        line = ''.join(line)
        for i in range(self._sequence_victory, 0, -1):
            """ A generator to match sequence to search score
            """
            match = piece * i
            if match in line:
                bad_move = opponent + match + opponent
                if bad_move not in line:
                    self.score += (score_factor * SCORE_POINT[i])
                return

    def _search_line(self, piece, board_space):
        """ Search has victory in line

                Check in matrix row if has match value to victory
                it get the previous five column position from current position played and
                the next five column position from current and check if has victory

        :param piece: current piece played
        :param board_space: is a position played in matrix ex. BoardSpace(row, col)
        :return: if has a victory in current line, True
                    otherwise is False
        """

        start_col = 0 if (board_space.col - self._sequence_victory) < 0 else (board_space.col - self._sequence_victory)
        end_col = self.size if (board_space.col + self._sequence_victory + 1) > self.size \
                            else (board_space.col + self._sequence_victory)
        sequence = self._table[board_space.row, start_col:end_col]
        self.heuristic_move_score(piece, sequence)
        return math.fabs(self.score) >= SCORE_POINT[ScoreEnum.FIVE]

    def _search_column(self, piece, board_space):
        """ Search has victory in line

                Check in matrix column if has match value to victory
                it get the previous five row position from current position played and
                the next five row position from current and check if has victory

        :param piece: current piece played
        :param board_space: is a position played in matrix ex. BoardSpace(row, col)
        :return: if has a victory in current row, True
                    otherwise is False
        """
        start_row = 0 if (board_space.row - self._sequence_victory) < 0 else (board_space.row - self._sequence_victory)
        end_row = self.size if (board_space.row + self._sequence_victory + 1) > self.size \
                            else (board_space.row + self._sequence_victory)
        sequence = self._table[start_row:end_row, board_space.col]
        self.heuristic_move_score(piece, sequence)
        return math.fabs(self.score) >= SCORE_POINT[ScoreEnum.FIVE]

    def _search_diagonal(self, piece, board_space):
        """ Search has victory by diagonal

                Check in matrix the diagonal if has match value to victory
                it get the previous five diagonal (row x col) position from current position played and
                the next five diagonal (row x col) position from current and check if has victory

        :param piece: current piece played
        :param board_space: is a position played in matrix ex. BoardSpace(row, col)
        :return: if has a victory in current diagonal, True
                    otherwise is False
        """
        offset = board_space.col - board_space.row
        diagonal = np.diag(self._table, k=offset).tolist()

        if len(diagonal) < self._sequence_victory:
            return False

        self.heuristic_move_score(piece, diagonal)
        return math.fabs(self.score) >= SCORE_POINT[ScoreEnum.FIVE]

    def _search_opposite_diagonal(self, piece, board_space):
        """ Search has victory by diagonal

                Check in matrix the diagonal if has match value to victory
                it get the previous five diagonal (row x col) position from current position played and
                the next five diagonal (row x col) position from current and check if has victory

        :param piece: current piece played
        :param board_space: is a position played in matrix ex. BoardSpace(row, col)
        :return: if has a victory in current diagonal, True
                    otherwise is False
        """
        new_col = board_space.row
        new_row = (self.size - 1) - board_space.col
        offset = new_col - new_row
        column_inverted = self._table[:, ::-1]
        transposed = column_inverted.transpose()
        diagonal = np.diag(transposed, k=offset).tolist()

        if len(diagonal) < self._sequence_victory:
            return False

        self.heuristic_move_score(piece, diagonal)
        return math.fabs(self.score) >= SCORE_POINT[ScoreEnum.FIVE]
