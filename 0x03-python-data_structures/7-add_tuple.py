#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples element-wise."""
    # Pad the shorter tuple with zeros
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    max_len = max(len_a, len_b)
    tuple_a += (0,) * (max_len - len_a)
    tuple_b += (0,) * (max_len - len_b)

    # Use a list comprehension to add the elements
    new_tuple = tuple([a + b for a, b in zip(tuple_a, tuple_b)])
    return new_tuple
