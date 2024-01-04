#!/usr/bin/python3
"""Rectangle class definition."""


class Rectangle:
    """A class that represents a rectangle.

    Attributes:
        number_of_instances (int): The total number of Rectangle objects.
        print_symbol (any): The symbol used to print the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Create a new Rectangle object.

        Args:
            width (int): The rectangle's width.
            height (int): The rectangle's height.
        """
        self.__class__.number_of_instances += 1
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
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the rectangle's area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the rectangle's perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles by their area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle object.
        Returns:
            Rectangle: The rectangle with the larger or equal area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a new Rectangle object with equal width and height.

        Args:
            size (int): The size of the square.
        Returns:
            Rectangle: The new square object.
        """
        return cls(size, size)

    def __str__(self):
        """Return a string representation of the rectangle.

        Uses the print_symbol attribute to print the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            rect += [str(self.print_symbol) for j in range(self.__width)]
            if i < self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """Return a formal representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a farewell message when the rectangle is deleted."""
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")
