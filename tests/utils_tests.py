import unittest
import numpy as np

from core import utils


class UtilsTests(unittest.TestCase):
    def _create_table(self, matrix):
        table = np.chararray(np.shape(matrix))
        table[:] = matrix[:]
        return table.astype(np.str)

    def test_take_third_diagonal_above_main(self):
        """
               0  1  2  3  4  5  6  7  8  9  10 11 12 13 14
            0  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
            1  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
            2  .  .  .  .  .  x  .  .  .  .  .  .  .  .  .
            3  .  .  .  .  .  .  o  .  .  .  .  .  .  .  .
            4  .  .  .  .  .  .  .  o  .  .  .  .  .  .  .
            5  .  .  .  .  .  .  .  .  x  .  .  .  .  .  .
            6  .  .  .  .  .  .  .  .  .  x  .  .  .  .  .
            7  .  .  .  .  .  .  .  .  .  .  o  .  .  .  .
            8  .  .  .  .  .  .  .  .  .  .  .  x  .  .  .
            9  .  .  .  .  .  .  .  .  .  .  .  .  o  .  .
            10 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
            11 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
            12 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
            13 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
            14 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
        """
        offset = 3
        matrix = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', 'x', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', 'o', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', 'o', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', 'x', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'x', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'o', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'x', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'o', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
        table = self._create_table(matrix)

        expected = ['.', '.', 'x', 'o', 'o', 'x', 'x', 'o', 'x', 'o', '.', '.']
        current_list = utils.get_diagonal(table, offset)

        self.assertListEqual(expected, current_list)

    def test_take_fifth_diagonal_below_main(self):
        """
               0  1  2  3  4  5  6  7  8  9  10 11 12 13 14
            0  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
            1  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
            2  .  .  .  .  .  x  .  .  .  .  .  .  .  .  .
            3  .  .  .  .  .  .  o  .  .  .  .  .  .  .  .
            4  .  .  .  .  .  .  .  o  .  .  .  .  .  .  .
            5  .  .  .  .  .  .  .  .  x  .  .  .  .  .  .
            6  .  o  .  .  .  .  .  .  .  x  .  .  .  .  .
            7  .  .  o  .  .  .  .  .  .  .  o  .  .  .  .
            8  .  .  .  o  .  .  .  .  .  .  .  x  .  .  .
            9  .  .  .  .  o  .  .  .  .  .  .  .  o  .  .
            10 .  .  .  .  .  o  .  .  .  .  .  .  .  .  .
            11 .  .  .  .  .  .  o  .  .  .  .  .  .  .  .
            12 .  .  .  .  .  .  .  o  .  .  .  .  .  .  .
            13 .  .  .  .  .  .  .  .  o  .  .  .  .  .  .
            14 .  .  .  .  .  .  .  .  .  o  .  .  .  .  .
        """
        offset = -5
        matrix = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', 'x', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', 'o', '.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', 'o', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.', 'x', '.', '.', '.', '.', '.', '.'],
                 ['.', 'o', '.', '.', '.', '.', '.', '.', '.', 'x', '.', '.', '.', '.', '.'],
                 ['.', '.', 'o', '.', '.', '.', '.', '.', '.', '.', 'o', '.', '.', '.', '.'],
                 ['.', '.', '.', 'o', '.', '.', '.', '.', '.', '.', '.', 'x', '.', '.', '.'],
                 ['.', '.', '.', '.', 'o', '.', '.', '.', '.', '.', '.', '.', 'o', '.', '.'],
                 ['.', '.', '.', '.', '.', 'o', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', 'o', '.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', 'o', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.', 'o', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'o', '.', '.', '.', '.', '.']]
        table = self._create_table(matrix)

        expected = ['.', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
        current_list = utils.get_diagonal(table, offset)

        self.assertListEqual(expected, current_list)

    def test_take_second_opposite_diagonal_above_main(self):
        """
               0  1  2  3  4  5  6  7  8  9  10 11 12 13 14
            0  .  .  .  .  .  .  .  .  .  .  .  .  o  .  .
            1  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
            2  .  .  .  .  .  x  .  .  .  .  x  .  .  .  .
            3  .  .  .  .  .  .  o  .  .  x  .  .  .  .  .
            4  .  .  .  .  .  .  .  o  o  .  .  .  .  .  .
            5  .  .  .  .  .  .  .  x  x  .  .  .  .  .  .
            6  .  o  .  .  .  .  .  .  .  x  .  .  .  .  .
            7  .  .  o  .  .  .  .  .  .  .  o  .  .  .  .
            8  .  .  .  o  .  .  .  .  .  .  .  x  .  .  .
            9  .  .  .  x  o  .  .  .  .  .  .  .  o  .  .
            10 .  .  .  .  .  o  .  .  .  .  .  .  .  .  .
            11 .  .  .  .  .  .  o  .  .  .  .  .  .  .  .
            12 .  .  .  .  .  .  .  o  .  .  .  .  .  .  .
            13 .  .  .  .  .  .  .  .  o  .  .  .  .  .  .
            14 .  .  .  .  .  .  .  .  .  o  .  .  .  .  .
        """
        offset = 2
        matrix = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'o', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', 'x', '.', '.', '.', '.', 'x', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', 'o', '.', '.', 'x', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', 'o', 'o', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', 'x', 'x', '.', '.', '.', '.', '.', '.'],
                  ['.', 'o', '.', '.', '.', '.', '.', '.', '.', 'x', '.', '.', '.', '.', '.'],
                  ['.', '.', 'o', '.', '.', '.', '.', '.', '.', '.', 'o', '.', '.', '.', '.'],
                  ['.', '.', '.', 'o', '.', '.', '.', '.', '.', '.', '.', 'x', '.', '.', '.'],
                  ['.', '.', '.', 'x', 'o', '.', '.', '.', '.', '.', '.', '.', 'o', '.', '.'],
                  ['.', '.', '.', '.', '.', 'o', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', 'o', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', 'o', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', 'o', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'o', '.', '.', '.', '.', '.']]
        table = self._create_table(matrix)

        expected = ['.', '.', '.', 'x', '.', '.', '.', 'x', 'o', 'x', 'x', '.', 'o']
        current_list = utils.get_opposite_diagonal(table, offset)

        self.assertListEqual(expected, current_list)

    def test_take_eighth_opposite_diagonal_below_main(self):
        """
               0  1  2  3  4  5  6  7  8  9  10 11 12 13 14
            0  .  .  .  .  .  .  .  .  .  .  .  .  o  .  .
            1  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
            2  .  .  .  .  .  x  .  .  .  .  x  .  .  .  .
            3  .  .  .  .  .  .  o  .  .  x  .  .  .  .  .
            4  .  .  .  .  .  .  .  o  o  .  .  .  .  .  .
            5  .  .  .  .  .  .  .  x  x  .  .  .  .  .  .
            6  .  o  .  .  .  .  .  .  .  x  .  .  .  .  .
            7  .  .  o  .  .  .  .  .  .  .  o  .  .  .  .
            8  .  .  .  o  .  .  .  .  .  .  .  x  .  .  o
            9  .  .  .  x  o  .  .  .  .  .  .  .  o  .  .
            10 .  .  .  .  .  o  .  .  .  .  .  .  x  .  .
            11 .  .  .  .  .  .  o  .  .  .  .  x  .  .  .
            12 .  .  .  .  .  .  .  o  .  .  x  .  .  .  .
            13 .  .  .  .  .  .  .  .  o  x  .  .  .  .  .
            14 .  .  .  .  .  .  .  .  x  o  .  .  .  .  .
        """
        offset = -8
        matrix = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'o', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', 'x', '.', '.', '.', '.', 'x', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', 'o', '.', '.', 'x', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', 'o', 'o', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', 'x', 'x', '.', '.', '.', '.', '.', '.'],
                  ['.', 'o', '.', '.', '.', '.', '.', '.', '.', 'x', '.', '.', '.', '.', '.'],
                  ['.', '.', 'o', '.', '.', '.', '.', '.', '.', '.', 'o', '.', '.', '.', '.'],
                  ['.', '.', '.', 'o', '.', '.', '.', '.', '.', '.', '.', 'x', '.', '.', 'o'],
                  ['.', '.', '.', 'x', 'o', '.', '.', '.', '.', '.', '.', '.', 'o', '.', '.'],
                  ['.', '.', '.', '.', '.', 'o', '.', '.', '.', '.', '.', '.', 'x', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', 'o', '.', '.', '.', '.', 'x', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', 'o', '.', '.', 'x', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', 'o', 'x', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', 'x', 'o', '.', '.', '.', '.', '.']]
        table = self._create_table(matrix)

        expected = ['x', 'x', 'x', 'x', 'x', '.', 'o']
        current_list = utils.get_opposite_diagonal(table, offset)

        self.assertListEqual(expected, current_list)
