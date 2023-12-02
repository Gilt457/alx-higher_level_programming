#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # Validate the index
    if not 0 <= idx <= len(my_list) - 1:
        raise IndexError("Index out of range")

    # Replace the element at the specified index
    my_list[idx] = element
    return my_list
