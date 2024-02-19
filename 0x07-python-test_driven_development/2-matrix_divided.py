#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
    - matrix: a list of lists of integers or floats
    - div: a number (integer or float)

    Returns:
    A new matrix with all elements divided by div and rounded to 2 decimal places.
    """
    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
