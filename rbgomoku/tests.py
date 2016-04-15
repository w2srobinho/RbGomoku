import unittest
from view import Board

class BoardTests(unittest.TestCase):
    def setUp(self):
        self.board = Board(3, 3)

    def test_board_of_table(self):
        expected_table = '   0  1  2 \n' \
                         '0  .  .  . \n' \
                         '1  .  .  . \n' \
                         '2  .  .  . '
        self.assertEqual(expected_table, str(self.board))

    def test_get_piece(self):
        piece = self.board.get_piece(1,1)
        self.assertEqual(Board.NONE, piece)

    def test_play_piece(self):
        piece = self.board.get_piece(1, 1)
        self.assertEqual(Board.NONE, piece)
        self.board.play_piece(Board.BLACK, 1, 1)
        piece = self.board.get_piece(1, 1)
        self.assertEqual(Board.BLACK, piece)
        self.board.play_piece(Board.WHITE, 0, 2)
        piece = self.board.get_piece(0, 2)
        self.assertEqual(Board.WHITE, piece)
        print(self.board)

