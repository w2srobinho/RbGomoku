import unittest

import numpy as np

from core import Piece, utils
from core.board import Board, Square
from core.score import Score, ScoreEnum, SCORE_POINT

class ScoreTests(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.score = Score(self.board.table)

    def test_search_winner_by_line(self):
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

    def test_heuristic_4_sequence_with_outmost_opened(self):
        """ ..xxxx.. """
        self.board.table[8, 3:7] = Piece.BLACK
        line = self.board.table[8, 1:9]
        current_score_value = self.score.heuristic(Piece.BLACK, line)
        expected_score = SCORE_POINT[ScoreEnum.FOUR] * 2
        self.assertEqual(expected_score, current_score_value)

    def test_heuristic_4_sequence_with_1_outmost_opened(self):
        """ .oxxxx.. """
        self.board.table[8, 3:7] = Piece.BLACK
        self.board.table[8, 2] = Piece.WHITE
        line = self.board.table[8, 1:9]
        current_score_value = self.score.heuristic(Piece.BLACK, line)
        expected_score = SCORE_POINT[ScoreEnum.FOUR]
        self.assertEqual(expected_score, current_score_value)

    def test_heuristic_4_sequence_with_1_outmost_closed(self):
        """ .oxxxxo. """
        self.board.table[8, 3:7] = Piece.BLACK
        self.board.table[8, 2] = Piece.WHITE
        self.board.table[8, 7] = Piece.WHITE
        line = self.board.table[8, 1:9]
        current_score_value = self.score.heuristic(Piece.BLACK, line)
        expected_score = 0
        self.assertEqual(expected_score, current_score_value)

    def test_heuristic_3_blank_1(self):
        """ ..xxx.x.. """
        self.board.table[8, 3:6] = Piece.BLACK
        self.board.table[8, 7] = Piece.BLACK
        print(self.board)
        line = self.board.table[8, 1:9]
        current_value = self.score.heuristic(Piece.BLACK, line)
        expected_value = SCORE_POINT[ScoreEnum.FOUR]
        self.assertEqual(expected_value, current_value)



