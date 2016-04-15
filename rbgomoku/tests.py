import unittest
from view import Board, Piece

def print_test(s):
    print("{0:#^50}".format(s))

class BoardTests(unittest.TestCase):
    def setUp(self):
        self.board = Board(size=15, sequence_victory=5)

    def test_board_of_table(self):
        print_test(" starting test_board_of_table ")
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
        print_test(" starting test_get_piece ")
        piece = self.board.get_piece(1,1)
        print()
        self.assertEqual(Piece.NONE, piece)

    def test_play_piece(self):
        print_test(" starting test_play_piece ")
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

    def test_search_line(self):
        print_test(" starting test_search_line ")
        result = self.board.search_line(Piece.BLACK, row=1, col=6)
        self.assertFalse(result)
        self.board._table[1, 5:10] = 'x'
        result = self.board.search_line(Piece.BLACK, row=1, col=5)
        print(self.board)
        print()
        self.assertTrue(result)

    def test_search_column(self):
        print_test(' starting test_search_column ')
        result = self.board.search_column(Piece.BLACK, row=5, col=1)
        self.assertFalse(result)
        self.board._table[5:10, 1] = 'x'
        result = self.board.search_column(Piece.BLACK, row=9, col=1)
        print(self.board)
        print()
        self.assertTrue(result)
