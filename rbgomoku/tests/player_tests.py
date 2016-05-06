import copy as cp
import unittest

from core.board import Board, Square, Piece
from core.player import HumanPlayer, MachinePlayer

class PlayerTests(unittest.TestCase):
    def setUp(self):
        self.board = Board(size=15, sequence_victory=5)

    def test_playing(self):
        player = HumanPlayer(self.board, Piece.WHITE)
        square = Square(row=7, col=7)
        player.play(square)
        piece = self.board.get_piece(square)
        self.assertEqual(Piece.WHITE, piece)

    def test_minimax(self):
        player = MachinePlayer(self.board, Piece.BLACK)
        self.board._table[1, 5:8] = Piece.BLACK

        expected_board = cp.deepcopy(self.board)
        expected_score = 999999
        expected_movement = Square(1, 4)

        current_score, current_movement = player.minimax(2)

        self.assertEqual(expected_score, current_score)
        self.assertEqual(expected_movement, current_movement)
        self.assertEqual(expected_board, self.board)

    def test_minimax_pruning(self):
        player = MachinePlayer(self.board, Piece.BLACK)
        self.board._table[1, 5:8] = Piece.BLACK

        expected_board = cp.deepcopy(self.board)
        expected_score = 999999
        expected_movement = Square(1, 4)

        current_score, current_movement = player.minimax_pruning(2)

        self.assertEqual(expected_score, current_score)
        self.assertEqual(expected_movement, current_movement)
        self.assertEqual(expected_board, self.board)


