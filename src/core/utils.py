import numpy as np


def get_diagonal(table, offset):
    """ Get diagonal from table

                Get a list elements referencing the diagonal by offset from main diagonal

        :param table: matrix to get diagonal
        :param offset: Offset of the diagonal from the main diagonal.
                       Can be positive or negative. Defaults to main diagonal (0).
        :return: list elements from request diagonal
    """
    diagonal = np.diag(table, k=offset).tolist()
    return diagonal


def get_opposite_diagonal(table, offset):
    """ Get diagonal from table

                Get a list elements referencing the opposite
                diagonal by offset from opposite diagonal
                Positive get below, and negative get higher diagonal from opposite diagonal
                   0  1  2  3  4
                0  a  a  a  a  .
                1  a  a  a  .  b
                2  a  a  .  b  b
                3  a  .  b  b  b
                4  .  b  b  b  b

        :param table: matrix to get diagonal
        :param offset: Offset of the opposite diagonal from the main diagonal.
                       Can be positive or negative. Defaults to opposite diagonal (0).
        :return: list elements from request opposite diagonal
    """
    column_inverted = table[:, ::-1]
    transposed = column_inverted.transpose()
    inverted_opp_diagonal = np.diag(transposed, k=-offset).tolist()
    opposite_diagonal = inverted_opp_diagonal[::-1]
    return opposite_diagonal