#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Pad the tuples with zeros if they have less than two elements
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    # Add the first two elements of each tuple and return the result
    return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
