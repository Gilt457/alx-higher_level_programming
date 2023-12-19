#!/usr/bin/python3
"""Create a MagicClass that matches a given bytecode from Holberton."""

from math import pi


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Create a MagicClass.

        Args:
            radius (int or float): The radius of the new MagicClass.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate the area of the MagicClass."""
        return pi * self.__radius ** 2

    def circumference(self):
        """Calculate the circumference of the MagicClass."""
        return 2 * pi * self.__radius
