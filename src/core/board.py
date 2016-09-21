import numpy as np
from core import Format, Piece
from core.exceptions import NotBlankSpaceException
from core.score import Score


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

    def is_valid(self):
        return not (self.row == -1 or self.col == -1)

    def __eq__(self, other):
        """ Compare the positions
        :param other: The position to compare
        :return: True if equals, False otherwise
        """
        return self.row == other.row and self.col == other.col

    def __repr__(self):
        return '[{},{}]'.format(self.row, self.col)


class Board:
    """ Board representation of the console game
    """
    SIZE = 15

    def __init__(self):
        """ Start the Board with empty positions
        :param size: size of board sizeXsize format
        """
        self._table = np.chararray((self.SIZE, self.SIZE))
        self._table[:] = Piece.NONE
        self._table = self._table.astype(np.str)
        self.score = Score(self._table)
        self.current_play = Square(-1, -1)

    def __len__(self):
        """
        :return: length of border
        """
        return self.SIZE

    def __eq__(self, other):
        """ Compare borders
        :param other:
        :return:
        """
        size_equals = self.SIZE == len(other)
        score_equals = self.score.value == other.current_score
        table_equals = np.array_equal(self._table, other.table)
        return size_equals and score_equals and table_equals

    def __repr__(self):
        """ Format the boarder
        :return: the board in str format
        """
        table_copy = self._table.tolist()
        if self.current_play.is_valid():
            table_copy[self.current_play.row][self.current_play.col] = Format.BOLD + \
                                                                       Format.Color.GREEN + \
                                                                       table_copy[self.current_play.row][
                                                                           self.current_play.col] + \
                                                                       ' ' + \
                                                                       Format.END
        formatter = ' '.join(['{' + str(i) + ':^2}' for i in range(self.SIZE + 1)])
        range_table = range(self.SIZE)
        idx_table = list(range_table)

        ## top index table ##
        idx_table_str = [str(n) for n in idx_table]
        top_idx_table_str = [' '] + idx_table_str
        top_idx_f = [formatter.format(*top_idx_table_str)]

        ## left index table ##
        left_idx_table = [[str(i)] + table_copy[i] for i in range_table]
        left_idx_table_f = [formatter.format(*line) for line in left_idx_table]

        str_table = '\n'.join(top_idx_f + left_idx_table_f)
        return str_table

    def get_piece(self, board_space):
        return self._table[board_space.row, board_space.col]

    def take_up_space(self, piece, board_space):
        """ Current movement in border

        :param piece: the piece played
        :param board_space: is a position played in matrix ex. BoardSpace(row, col)
        :return: the winner or Piece.NONE if no there winner
        """
        self.current_play = board_space
        self._table[board_space.row, board_space.col] = piece
        winner = self.score.has_winner(piece, board_space)
        if self._table.count(Piece.NONE).sum() == 0 and winner == Piece.NONE:
            raise NotBlankSpaceException
        return winner

    def restore_move(self, board_space, score):
        self._table[board_space.row, board_space.col] = Piece.NONE
        self.score.value = score

    @property
    def table(self):
        return self._table

    @property
    def current_score(self):
        return self.score.value
