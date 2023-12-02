#!/usr/bin/python3

def no_c(my_string):
    """Remove all occurrences of 'c' or 'C' from a string."""
    # Use a list comprehension to filter out the unwanted characters
    updated_str = ''.join([i for i in my_string if i not in 'cC'])
    return updated_str
