#!/usr/bin/python3

"""A module that defines a Square class."""


class Square:
    """A class that represents a square shape."""

    def __init__(self, size):
        """Create a new Square instance.

        Parameters:
            size (int): The length of the square's side.
        """
        self.__size = size
