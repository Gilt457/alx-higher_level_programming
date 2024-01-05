#!/usr/bin/python3
"""This module contains a function to print a square."""

def print_square(size):
    """This function prints a square using the # symbol.

    Parameters:
        size (int): The size of the square's side.
    Raises:
        TypeError: If size is not an int.
        ValueError: If size is negative.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
