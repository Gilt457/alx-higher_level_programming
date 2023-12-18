#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    div = None
    try:
        div = a / b
    except (TypeError, ZeroDivisionError) as e:
        print("Error: {}".format(e))
    else:
        print("Inside result: {}".format(div))
    return div
