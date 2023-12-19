#!/usr/bin/python3
"""A module that defines a Square class."""


class Square:
    """A class that represents a square."""

    def __init__(self, size=0):
        """Create a new square with a given size.

        Parameters:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Access or modify the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
