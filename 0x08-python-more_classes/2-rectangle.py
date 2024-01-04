#!/usr/bin/python3
"""Rectangle class definition."""


class Rectangle:
    """A class that represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Create a new Rectangle instance.

        Parameters:
            width (int): The rectangle's width.
            height (int): The rectangle's height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get or set the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate and return the rectangle's area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate and return the rectangle's perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width + self.__height) * 2)
