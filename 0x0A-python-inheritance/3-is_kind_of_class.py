#!/usr/bin/python3
"""Module that contains a function to check class inheritance."""


def is_kind_of_class(obj, a_class):
    """Verify if an object is an instance or inherits from a class.

    Parameters:
        obj (any): The object to verify.
        a_class (type): The class to compare the type of obj with.
    Returns:
        True if obj is an instance or inherits from a_class.
        False otherwise.
    """
    return isinstance(obj, a_class)
