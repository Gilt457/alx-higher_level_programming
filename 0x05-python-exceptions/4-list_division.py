#!/usr/bin/python3
"""This module contains a function that divides two lists element."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide two lists element by element and return a new list.

    Args:
        my_list_1 (list): The first list of numbers.
        my_list_2 (list): The second list of numbers.
        list_length (int): The number of elements to divide.

    Returns:
        list: A new list of length list_length containing the quotients.
    """
    new_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except (TypeError, ZeroDivisionError, IndexError) as error:
            print(error)
            div = 0
        finally:
            new_list.append(div)
    return new_list
