#!/usr/bin/python3
def delete_at(my_list=None, idx=0):
    """Delete an element from a list at a given index."""
    if my_list is None:
        my_list = []
    if 0 <= idx < len(my_list):
        my_list.pop(idx)
    return my_list
