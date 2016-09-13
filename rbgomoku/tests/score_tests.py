import unittest

import numpy as np

from core import Piece, utils
from core.board import Board, Square
from core.score import Score, ScoreEnum, SCORE_POINT


def print_test_name(s):
    print("{0:#^50}".format(s))


class ScoreTests(unittest.TestCase):
    def setUp(self):
        self.board = Board(size=15, sequence_victory=5)
        self.score = Score(self.board.table)

    def test_search_winner_by_line(self):
        print_test_name(" starting test_search_winner_by_line ")
        square = Square(1, 6)
        result = self.score.has_winner(Piece.BLACK, square)
        self.assertNotEqual(Piece.BLACK, result)
        self.board.table[1, 5:10] = Piece.BLACK
        square = Square(1, 5)
        print(self.board)
        print()
        result = self.score.has_winner(Piece.BLACK, square)
        self.assertEqual(Piece.BLACK, result)

    def test_search_winner_by_column(self):
        print_test_name(' starting test_search_winner_by_column ')
        square = Square(5, 1)
        result = self.score.has_winner(Piece.WHITE, square)
        self.assertNotEqual(Piece.WHITE, result)
        self.board.table[5:10, 1] = Piece.WHITE
        square = Square(9, 1)
        print(self.board)
        print()
        result = self.score.has_winner(Piece.WHITE, square)
        self.assertEqual(Piece.WHITE, result)

    def test_search_winner_by_diagonal(self):
        print_test_name(' starting test_search_winner_by_diagonal ')
        square = Square(9, 3)
        result = self.score.has_winner(Piece.BLACK, square)
        self.assertNotEqual(Piece.BLACK, result)
        range = self.board.table[8:13, 2:7]
        range[np.diag_indices_from(range)] = Piece.BLACK
        print(self.board)
        print()
        result = self.score.has_winner(Piece.BLACK, square)
        self.assertEqual(Piece.BLACK, result)

    def test_search_winner_by_opposite_diagonal(self):
        print_test_name(' starting test_search_winner_by_opposite_diagonal ')
        square = Square(9, 2)
        result = self.score.has_winner(Piece.BLACK, square)
        self.assertNotEqual(Piece.BLACK, result)
        range = self.board.table[5:10, 2:7]
        range = range[:, ::-1]
        range[np.diag_indices_from(range)] = Piece.BLACK
        print(self.board)
        print()
        result = self.score.has_winner(Piece.BLACK, square)
        self.assertEqual(Piece.BLACK, result)

    def test_heuristic_4_sequence_pieces(self):
        print_test_name(' heuristic_4_sequence_pieces ')
        range = self.board.table[8:12, 2:6]
        range[np.diag_indices_from(range)] = Piece.BLACK
        diag = utils.get_diagonal(self.board.table, -6)

        self.score.heuristic_move_score(Piece.BLACK, diag)
        self.assertEqual(SCORE_POINT[ScoreEnum.FOUR], self.score.score)
        print(self.board)
        print()



