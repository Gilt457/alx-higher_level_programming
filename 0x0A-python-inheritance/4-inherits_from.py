#!/usr/bin/python3
"""Defines a function to check inheritance of a class."""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a subclass of a_class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare with obj's type.
    Returns:
        True if obj is an instance of a subclass of a_class.
        False otherwise.
    """
    return issubclass(type(obj), a_class) and not type(obj) is a_class
