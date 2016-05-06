import unittest

import numpy as np
from core.board import Board, BoardSpace, Piece

class BoardTests(unittest.TestCase):
    def setUp(self):
        self.board = Board(size=15, sequence_victory=5)

    def print_test(self, s):
        print("{0:#^50}".format(s))

    def test_board_of_table(self):
        self.print_test(" starting test_board_of_table ")
        expected_table = '   0  1  2  3  4  5  6  7  8  9  10 11 12 13 14\n' \
                         '0  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . \n' \
                         '1  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . \n' \
                         '2  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . \n' \
                         '3  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . \n' \
                         '4  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . \n' \
                         '5  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . \n' \
                         '6  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . \n' \
                         '7  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . \n' \
                         '8  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . \n' \
                         '9  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . \n' \
                         '10 .  .  .  .  .  .  .  .  .  .  .  .  .  .  . \n' \
                         '11 .  .  .  .  .  .  .  .  .  .  .  .  .  .  . \n' \
                         '12 .  .  .  .  .  .  .  .  .  .  .  .  .  .  . \n' \
                         '13 .  .  .  .  .  .  .  .  .  .  .  .  .  .  . \n' \
                         '14 .  .  .  .  .  .  .  .  .  .  .  .  .  .  . '
        print(self.board)
        print()
        self.assertEqual(expected_table, str(self.board))

    def test_get_piece(self):
        self.print_test(" starting test_get_piece ")
        piece = self.board.get_piece(BoardSpace(1, 1))
        print()
        self.assertEqual(Piece.NONE, piece)

    def test_play_piece(self):
        self.print_test(" starting test_play_piece ")
        board_space = BoardSpace(1, 1)
        piece = self.board.get_piece(board_space)
        self.assertEqual(Piece.NONE, piece)
        self.board.take_up_space(Piece.BLACK, board_space)
        piece = self.board.get_piece(board_space)
        self.assertEqual(Piece.BLACK, piece)
        board_space = BoardSpace(0, 2)
        self.board.take_up_space(Piece.WHITE, board_space)
        piece = self.board.get_piece(board_space)
        self.assertEqual(Piece.WHITE, piece)
        print(self.board)
        print()

    def test_search_winner_by_line(self):
        self.print_test(" starting test_search_winner_by_line ")
        board_space = BoardSpace(1, 6)
        result = self.board.has_winner(Piece.BLACK, board_space)
        self.assertNotEqual(Piece.BLACK, result)
        self.board._table[1, 5:10] = Piece.BLACK
        board_space = BoardSpace(1, 5)
        result = self.board.has_winner(Piece.BLACK, board_space)
        print(self.board)
        print()
        self.assertEqual(Piece.BLACK, result)

    def test_search_winner_by_column(self):
        self.print_test(' starting test_search_winner_by_column ')
        board_space = BoardSpace(5, 1)
        result = self.board.has_winner(Piece.WHITE, board_space)
        self.assertNotEqual(Piece.WHITE, result)
        self.board._table[5:10, 1] = Piece.WHITE
        board_space = BoardSpace(9, 1)
        result = self.board.has_winner(Piece.WHITE, board_space)
        print(self.board)
        print()
        self.assertEqual(Piece.WHITE, result)

    def test_search_winner_by_diagonal(self):
        self.print_test(' starting test_search_winner_by_diagonal ')
        board_space = BoardSpace(9, 3)
        result = self.board.has_winner(Piece.BLACK, board_space)
        self.assertNotEqual(Piece.BLACK, result)
        subboard = self.board._table[8:13, 2:7]
        subboard[np.diag_indices_from(subboard)] = Piece.BLACK
        result = self.board.has_winner(Piece.BLACK, board_space)
        print(self.board)
        self.assertEqual(Piece.BLACK, result)

    def test_search_winner_by_opposite_diagonal(self):
        self.print_test(' starting test_search_winner_by_opposite_diagonal ')
        board_space = BoardSpace(9, 2)
        result = self.board.has_winner(Piece.BLACK, board_space)
        self.assertNotEqual(Piece.BLACK, result)
        subboard = self.board._table[5:10, 2:7]
        subboard = subboard[:, ::-1]
        subboard[np.diag_indices_from(subboard)] = Piece.BLACK
        print(self.board)
        result = self.board.has_winner(Piece.BLACK, board_space)
        print(self.board)
        self.assertEqual(Piece.BLACK, result)
