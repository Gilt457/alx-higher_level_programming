#!/usr/bin/python3
"""BaseGeometry class definition."""


class BaseGeometry:
    """Represent a base geometry object."""

    def area(self):
        """Raise an exception for unimplemented method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if a parameter is a positive integer.

        Args:
            name (str): The parameter name.
            value (int): The parameter value.
        Raises:
            TypeError: If value is not an int.
            ValueError: If value is not positive.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be positive")
