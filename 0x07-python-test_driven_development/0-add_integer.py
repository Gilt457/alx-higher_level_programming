#!/usr/bin/python3
"""This module contains a function that adds two integers."""


def add_integer(a, b=98):
    """Return the sum of a and b as integers.

    If a or b is a float, it is converted to an int before adding.

    Args:
        a (int or float): The first number to add.
        b (int or float, optional): The second number to add. Defaults to 98.

    Returns:
        int: The sum of a and b as integers.

    Raises:
        TypeError: If a or b is not an int or a float.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
