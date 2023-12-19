#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, side):
        """Initialize a new square.

        Args:
            side (int): The side of the new square.
        """
        self.side = side

    @property
    def side(self):
        """Get/set the current side of the square."""
        return self.__side

    @side.setter
    def side(self, value):
        if type(value) is not int:
            raise TypeError("side must be an integer")
        if value < 0:
            raise ValueError("side must be >= 0")
        self.__side = value

    def area(self):
        """Return the current area of the square."""
        return self.__side ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__side == 0:
            print("")
        else:
            for _ in range(self.__side):
                print("#" * self.__side)
