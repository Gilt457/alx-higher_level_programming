#!/usr/bin/python3
def remove_element(list_to_modify=[], position=0):
    """Removes an element from a list at a given position."""
    if position >= 0 and position < len(list_to_modify):
        list_to_modify.pop(position)
    return list_to_modify
