#!/usr/bin/python3

"""A module that defines a Square class."""


class Square:
    """A class that represents a square shape."""

    def __init__(self, size=0):
        """Create a new square instance.

        Parameters:
            size (int): The length of the square's side.
        """
        self.size = size

    @property
    def size(self):
        """Access or modify the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare two squares for equality."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare two squares for inequality."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare two squares for less than."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare two squares for less than or equal."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare two squares for greater than."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare two squares for greater than or equal."""
        return self.area() >= other.area()
