#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    :param matrix: The input 2-dimensional array.
    :return: A new matrix with each value being the square of the corresponding value in the input matrix.
    """
    return [[num ** 2 for num in row] for row in matrix]
