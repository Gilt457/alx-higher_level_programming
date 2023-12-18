#!/usr/bin/python3
def magic_calculation(a, b):
    """Calculate a magic value based on a and b."""
    result = 0
    for i in range(1, 3):
        try:
            # Raise an exception if i is greater than a
            assert i <= a, 'Too far'
            # Add a power b divided by i to the result
            result += a ** b / i
        except (AssertionError, ZeroDivisionError):
            # Set the result to b plus a and stop the loop
            result = b + a
            break
    return result
