#!/usr/bin/python3
"""Defines a function that divides a matrix by a number."""


def matrix_divided(matrix, div):
    """Divides each element of a matrix by a number.

    Args:
        matrix (list): A matrix of ints or floats as a list of lists.
        div (int/float): The number to divide by.
    Raises:
        TypeError: If matrix is not a list of lists of numbers.
        TypeError: If matrix has rows of different lengths.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is zero.
    Returns:
        A new matrix with the division results as a list of lists.
    """
    # Check if matrix is a valid list of lists of numbers
    if (not isinstance(matrix, list) or not matrix or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float))
                    for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    # Check if matrix has rows of equal length
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a valid number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of matrix by div and round to two decimals
    return [[round(num / div, 2) for num in row] for row in matrix]
