#!/usr/bin/python3
"""Module that defines a function to print x elements of a list."""


def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    printed = 0
    for item in my_list[:x]:
        try:
            print(item, end="")
            printed += 1
        except Exception:
            break
    print()
    return printed
