import copy as cp
import numpy as np

from core import NotBlankSpaceException

class GomokuState:
    level_tree = 0

    def __init__(self, board, parent_state):
        self.level_tree += 1
        # self.score = parent_state.value + 0
        self.board = cp.copy(board)
        self.parent = parent_state
        self._children = set()

    @property
    def children(self):
        return self._children

    def add_child(self, child_state):
        self._children.add(child_state)

    def add_children_states(self, children_state):
        self._children.update(children_state)

    def is_leaf(self):
        return len(self.children) == 0


class Score:
    ONE = 1
    TWO = 10
    THREE = 100
    FOUR = 1000
    FIVE = 10000

class Piece:
    """Piece representation
    """
    """Indicate the position in board does not played yet"""
    NONE = '.'

    """Indicate a BLACK piece for game"""
    BLACK = 'x'

    """Indicate a WHITE piece for game"""
    WHITE = 'o'


class Board:
    """ Board representation of the console game
    """
    def __init__(self, size, sequence_victory):
        """ Start the Board with empty positions
        :param size: size of board sizeXsize format
        :param sequence_victory: number of piece in sequence to see victory
        """
        self._table = np.chararray((size, size))
        self._table[:] = Piece.NONE
        self._table = self._table.astype(np.str)
        self._sequence_victory = sequence_victory


    def __repr__(self):
        """ Format the boarder
        :return: the board in str format
        """
        table_copy = self._table.tolist()
        formatter = ' '.join(['{' + str(i) + ':^2}' for i in range(len(table_copy) + 1)])
        range_table = range(len(table_copy))
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

    def get_piece(self, row, col):
        return self._table[row, col]

    def play_piece(self, piece, row, col):
        """ Current movement in border

        :param piece: the piece played
        :param row: the row position
        :param col: the column position
        :return: the winner or Piece.NONE if no there winner
        """
        self._table[row, col] = piece
        winner = self.has_winner(piece, row, col)
        if (self._table == '.').sum() == 0 and winner == Piece.NONE:
            raise NotBlankSpaceException
        return winner

    @property
    def table(self):
        return self._table

    def has_winner(self, piece, row, col):
        """ Search for winner play in border

        :param piece: represent current piece played
        :param row: the row position
        :param col: the column position
        :return: the current winner if there or Piece.NONE if no there winner
        """
        if self._search_line(piece, row, col):
            """ Faz verificação por linha
                se ocorrer uma vitória na linha atual
                escreve a peça ganhadora e retorna verdadeiro
            """
            return piece

        if self._search_column(piece, row, col):
            """ Faz verificação por linha
                se ocorrer uma vitória na linha atual
                escreve a peça ganhadora e retorna verdadeiro
            """
            return piece

        if self._search_diagonal(piece, row, col):
            """ Faz verificação da diagonal no sentido da diagonal principal
                se ocorrer uma vitória na diagonal atual
                escreve a peça ganhadora e retorna verdadeiro
            """
            return piece

        if self._search_opposite_diagonal(piece, row, col):
            """ Faz verificação da diagonal no sentido da diagonal secundária
                se ocorrer uma vitória na diagonal atual
                escreve a peça ganhadora e retorna verdadeiro
            """
            return piece

        return Piece.NONE

    def _victory_match(self, piece):
        """ A generator to match victory

        :param piece: for check the victory sequence
        :return: the sequence for victory
        """
        return piece * self._sequence_victory

    def _search_line(self, piece, row, col):
        """ Search has victory in line

                Check in matrix row if has match value to victory
                it get the previous five column position from current position played and
                the next five column position from current and check if has victory

        :param piece: current piece played
        :param row: position in matrix
        :param col: position in matrix
        :return: if has a victory in current line, True
                    otherwise is False
        """
        match_str = self._victory_match(piece)
        start_col = 0 if (col - self._sequence_victory) < 0 else (col - self._sequence_victory)
        size = len(self._table)
        end_col = size if (col + self._sequence_victory + 1) > size else (col + self._sequence_victory + 1)
        return match_str in ''.join(self._table[row, start_col:end_col])

    def _search_column(self, piece, row, col):
        """ Search has victory in line

                Check in matrix column if has match value to victory
                it get the previous five row position from current position played and
                the next five row position from current and check if has victory

        :param piece: current piece played
        :param row: position in matrix
        :param col: position in matrix
        :return: if has a victory in current row, True
                    otherwise is False
        """
        match_str = self._victory_match(piece)
        start_row = 0 if (row - self._sequence_victory) < 0 else (row - self._sequence_victory)
        size = len(self._table)
        end_row = size if (row + self._sequence_victory + 1) > size else (row + self._sequence_victory + 1)
        return match_str in ''.join(self._table[start_row:end_row, col])

    def _search_diagonal(self, piece, row, col):
        """ Search has victory by diagonal

                Check in matrix the diagonal if has match value to victory
                it get the previous five diagonal (row x col) position from current position played and
                the next five diagonal (row x col) position from current and check if has victory

        :param piece: current piece played
        :param row: position in matrix
        :param col: position in matrix
        :return: if has a victory in current diagonal, True
                    otherwise is False
        """
        match_str = self._victory_match(piece)
        offset = col - row
        diagonal = np.diag(self._table, k=offset).tolist()
        diagonal_formatted = ''.join(diagonal)

        return match_str in diagonal_formatted

    def _search_opposite_diagonal(self, piece, row, col):
        """ Search has victory by diagonal

                Check in matrix the diagonal if has match value to victory
                it get the previous five diagonal (row x col) position from current position played and
                the next five diagonal (row x col) position from current and check if has victory

        :param piece: current piece played
        :param row: position in matrix
        :param col: position in matrix
        :return: if has a victory in current diagonal, True
                    otherwise is False
        """
        new_col = row
        size = len(self._table)
        new_row = (size - 1) - col
        match_str = self._victory_match(piece)
        offset = new_col - new_row
        column_inverted = self._table[:, ::-1]
        transposed = column_inverted.transpose()
        diagonal = np.diag(transposed, k=offset).tolist()
        diagonal_formatted = ''.join(diagonal)

        return match_str in diagonal_formatted
