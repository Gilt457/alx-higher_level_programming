#!/usr/bin/python3
"""A function that prints a name."""


def print_name(first, last=""):
    """Display a name.

    Args:
        first (str): The first name to display.
        last (str): The last name to display.
    Raises:
        TypeError: If first or last are not strings.
    """
    if type(first) is not str:
        raise TypeError("first must be a string")
    if type(last) is not str:
        raise TypeError("last must be a string")
    print("My name is {} {}".format(first, last))
