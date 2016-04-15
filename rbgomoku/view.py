
class Score:
    ONE = 1
    TWO = 20
    THREE = 50
    FOUR = 100
    FIVE = 10000


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


class Board:
    NONE = '.'
    BLACK = 'x'
    WHITE = 'o'

    def __init__(self, size, sequency_victory):
        self._table = []
        self._winner = self.NONE
        self._sequency_victory = sequency_victory

        for i in range(size):
            self._table.append(list(self.NONE * (size)))

    def __repr__(self):
        formatter = ' '.join(['{' + str(i) + ':^2}' for i in range(len(self._table) + 1)])
        range_table = range(len(self._table))
        idx_table = list(range_table)

        ## top index table ##
        idx_table_str = [str(n) for n in idx_table]
        top_idx_table_str = [' '] + idx_table_str
        top_idx_f = formatter.format(*top_idx_table_str)

        ## left index table ##
        left_idx_table = [[str(i)] + self._table[i] for i in range_table]
        left_idx_table_f = [formatter.format(*line) for line in left_idx_table]

        str_table = '\n'.join([top_idx_f] + left_idx_table_f)
        return str_table

    def get_piece(self, row, col):
        return self._table[row][col]

    def play_piece(self, piece, row, col):
        self._table[row][col] = piece

    def victory_match(self, piece):
        return piece * self._sequency_victory

    def search_line(self, piece, line):
        match_str = self.victory_match(piece)
        return match_str in ''.join(line)


    # def search_winner(self, piece):
    #     size = len(self._table)
    #     for i in range(size):
    #         for j in


# class Human:
#     human_piece = Board.BLACK
#
#     def __init__(self, node):





class GomokuState:
    def __init__(self, value, board):
        self.board = board
        self.value = value

