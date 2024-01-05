#!/usr/bin/python3
"""
This module contains a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """This function multiplies two matrices

    Args:
        m_a (list of lists of int/float): Matrix to be multiplied
        m_b (list of lists of int/float): Matrix to be multiplied

    Raises:
        TypeError: If m_a or m_b is not a list
        TypeError: If m_a or m_b is not a list of lists
        TypeError: If one element of list of lists is not int/float
        TypeError: If row of m_a or m_b are not the same size
        ValueError: If m_a or m_b is empty
        ValueError: If m_a and m_b cannot be multiplied

    Returns:
        A new list which is the outcome of the multiplication

    """

    # Check if m_a and m_b are lists
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    # Check if m_a and m_b are lists of lists
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Check if m_a and m_b contain only integers or floats
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Check if each row of m_a and m_b are of the same size
    row_len_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_len_a:
            raise TypeError("each row of m_a must should be of the same size")
    row_len_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_len_b:
            raise TypeError("each row of m_b must should be of the same size")

    # Check if m_a and m_b can be multiplied
    if row_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Transpose m_b
    transposed_b = []
    for i in range(row_len_b):
        new_row = []
        for j in range(len(m_b)):
            new_row.append(m_b[j][i])
        transposed_b.append(new_row)

    # Multiply m_a and transposed_b
    result = []
    for row_a in m_a:
        new_row = []
        for col_b in transposed_b:
            dot_product = 0
            for k in range(row_len_a):
                dot_product += row_a[k] * col_b[k]
            new_row.append(dot_product)
        result.append(new_row)

    return result
