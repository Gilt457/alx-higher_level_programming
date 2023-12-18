#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divide two lists element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        list: A new list of length list_length containing all the divisions.
    """
    new_list = []
    for i in range(list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except (TypeError, ZeroDivisionError, IndexError) as e:
            print(e)
            new_list.append(0)
    return new_list
