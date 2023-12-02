#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Return a new list with the element replaced at the given index."""
    if not my_list:  # Check if the list is empty
        return my_list
    if 0 <= idx < len(my_list):  # Check if the index is valid
        new_list = my_list.copy()  # Make a copy of the list
        new_list[idx] = element  # Replace the element at the index
        return new_list
    return my_list  # Return the original list if the index is invalid
