#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Delete an item at a specific position in a list."""
    # Check if the index is valid
    if 0 <= idx < len(my_list):
        # Loop through the list from the index to the end
        for i in range(idx, len(my_list) - 1):
            # Swap the current element with the next one
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        # Remove the last element of the list
        my_list.pop()
    # Return the modified list
    return my_list
