import unittest

from core.board import Board, Square, Piece


class BoardTests(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_board_of_table(self):
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
        piece = self.board.get_piece(Square(1, 1))
        print()
        self.assertEqual(Piece.NONE, piece)

    def test_play_piece(self):
        square = Square(1, 1)
        piece = self.board.get_piece(square)
        self.assertEqual(Piece.NONE, piece)
        self.board.take_up_space(Piece.BLACK, square)
        piece = self.board.get_piece(square)
        self.assertEqual(Piece.BLACK, piece)
        square = Square(0, 2)
        self.board.take_up_space(Piece.WHITE, square)
        piece = self.board.get_piece(square)
        self.assertEqual(Piece.WHITE, piece)
        print(self.board)
        print()
