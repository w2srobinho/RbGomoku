import numpy as np

# class Gomoku:
#     def __init__(self):
#         self.current_state =
#
#
# class Tree:
#     def __init__(self, head):
#         self._parent = None
#         self._head = head
#         self._subtree = {}
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
        self._winner = Piece.NONE
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
        return self._table[row][col]

    def play_piece(self, piece, row, col):
        self._table[row][col] = piece
        # return self.has_winner(piece, row, col)

    @property
    def winner(self):
        return self._winner

    @property
    def table(self):
        return self._table

    def has_winner(self, piece, row, col):
        if self.search_line(piece, row, col):
            """ Faz verificação por linha
                se ocorrer uma vitória na linha atual
                escreve a peça ganhadora e retorna verdadeiro
            """
            self._winner = piece
            return True

        if self.search_column(piece, row, col):
            """ Faz verificação por linha
                se ocorrer uma vitória na linha atual
                escreve a peça ganhadora e retorna verdadeiro
            """
            self._winner = piece
            return True

        if self.search_diagonal(piece, row, col):
            """ Faz verificação da diagonal no sentido da diagonal principal
                se ocorrer uma vitória na diagonal atual
                escreve a peça ganhadora e retorna verdadeiro
            """
            self._winner = piece
            return True

        if self.search_opposite_diagonal(piece, row, col):
            """ Faz verificação da diagonal no sentido da diagonal secundária
                se ocorrer uma vitória na diagonal atual
                escreve a peça ganhadora e retorna verdadeiro
            """
            self._winner = piece
            return True

    def victory_match(self, piece):
        """ A generator to match victory

        :param piece: for check the victory sequence
        :return: the sequence for victory
        """
        return piece * self._sequence_victory

    def search_line(self, piece, row, col):
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
        match_str = self.victory_match(piece)
        start_col = 0 if (col - self._sequence_victory) < 0 else (col - self._sequence_victory)
        size = len(self._table)
        end_col = size if (col + self._sequence_victory + 1) > size else (col + self._sequence_victory + 1)
        return match_str in ''.join(self._table[row][start_col:end_col])

    def search_column(self, piece, row, col):
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
        match_str = self.victory_match(piece)
        start_row = 0 if (row - self._sequence_victory) < 0 else (row - self._sequence_victory)
        size = len(self._table)
        end_row = size if (row + self._sequence_victory + 1) > size else (row + self._sequence_victory + 1)
        return match_str in ''.join(self._table[start_row:end_row, col])

    def search_diagonal(self, piece, row, col):
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
        match_str = self.victory_match(piece)
        offset = col - row
        diagonal = np.diagonal(self._table, offset=offset, axis1=0).tolist()
        diagonal_formatted = ''.join(diagonal)

        return match_str in diagonal_formatted

    def search_opposite_diagonal(self, piece, row, col):
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
        match_str = self.victory_match(piece)
        offset = new_col - new_row
        column_inverted = self._table[:, ::-1]
        transposed = column_inverted.transpose()
        diagonal = np.diag(transposed, k=offset).tolist()
        diagonal_formatted = ''.join(diagonal)

        return match_str in diagonal_formatted





class GomokuState:
    def __init__(self, value, board):
        self.board = board
        self.value = value

