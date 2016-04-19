import unittest

import numpy as np
from core.board import Board, Piece

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
        piece = self.board.get_piece(1,1)
        print()
        self.assertEqual(Piece.NONE, piece)

    def test_play_piece(self):
        self.print_test(" starting test_play_piece ")
        piece = self.board.get_piece(1, 1)
        self.assertEqual(Piece.NONE, piece)
        self.board.play_piece(Piece.BLACK, 1, 1)
        piece = self.board.get_piece(1, 1)
        self.assertEqual(Piece.BLACK, piece)
        self.board.play_piece(Piece.WHITE, 0, 2)
        piece = self.board.get_piece(0, 2)
        self.assertEqual(Piece.WHITE, piece)
        print(self.board)
        print()

    def test_search_winner_by_line(self):
        self.print_test(" starting test_search_winner_by_line ")
        result = self.board.has_winner(Piece.BLACK, row=1, col=6)
        self.assertNotEqual(Piece.BLACK, result)
        self.board._table[1, 5:10] = 'x'
        result = self.board.has_winner(Piece.BLACK, row=1, col=5)
        print(self.board)
        print()
        self.assertEqual(Piece.BLACK, result)

    def test_search_winner_by_column(self):
        self.print_test(' starting test_search_winner_by_column ')
        result = self.board.has_winner(Piece.BLACK, row=5, col=1)
        self.assertNotEqual(Piece.BLACK, result)
        self.board._table[5:10, 1] = 'x'
        result = self.board.has_winner(Piece.BLACK, row=9, col=1)
        print(self.board)
        print()
        self.assertEqual(Piece.BLACK, result)

    def test_search_winner_by_diagonal(self):
        self.print_test(' starting test_search_winner_by_diagonal ')
        result = self.board.has_winner(Piece.BLACK, row=9, col=3)
        self.assertNotEqual(Piece.BLACK, result)
        subboard = self.board._table[8:13, 2:7]
        subboard[np.diag_indices_from(subboard)] = Piece.BLACK
        result = self.board.has_winner(Piece.BLACK, row=9, col=3)
        print(self.board)
        self.assertEqual(Piece.BLACK, result)

    def test_search_winner_by_opposite_diagonal(self):
        self.print_test(' starting test_search_winner_by_opposite_diagonal ')
        result = self.board.has_winner(Piece.BLACK, row=9, col=2)
        self.assertNotEqual(Piece.BLACK, result)
        subboard = self.board._table[5:10, 2:7]
        subboard = subboard[:, ::-1]
        subboard[np.diag_indices_from(subboard)] = Piece.BLACK
        print(self.board)
        result = self.board.has_winner(Piece.BLACK, row=9, col=2)
        print(self.board)
        self.assertEqual(Piece.BLACK, result)
