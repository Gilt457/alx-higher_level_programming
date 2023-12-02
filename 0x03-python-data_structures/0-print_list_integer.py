#!/usr/bin/python3
# -----------------------------------------------------------
# Python script that:
# shows how to print all integers in a list
#
# (C) 2022 Lepatio Borel, Mbouda, Cameroon
# email lepatioborel@gmail.com
# -----------------------------------------------------------


def print_list_integer(numbers=[]):
    """Prints all intergers of a list

    Args:
      numbers: the list argument whose items will be printed
    """

    # Iterate through list
    for integer in numbers:
        print("{:d}".format(integer))
