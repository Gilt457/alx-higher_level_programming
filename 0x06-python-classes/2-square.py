#!/usr/bin/python3

"""A module that defines a Square class."""


class Square:
    """A class that represents a square."""

    def __init__(self, size=0):
        """Create a new Square instance.

        Parameters:
            size (int): The length of the square's side.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
