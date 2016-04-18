import unittest

from core.board import Board, Piece
from core.player import HumanPlayer

class PlayerTests(unittest.TestCase):
    def setUp(self):
        self.board = Board(size=15, sequence_victory=5)
        self.player = HumanPlayer(self.board, Piece.WHITE)

    def test_playing(self):
        self.player.play(row=7, col=7)
        piece = self.board.get_piece(row=7, col=7)
        self.assertEqual(Piece.WHITE, piece)

