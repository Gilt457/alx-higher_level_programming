#!/usr/bin/python3
"""
MyList class that inherits from list
"""


class MyList(list):
    """a list subclass"""
    def __init__(self):
        """creates the object"""
        super().__init__()

    def print_sorted(self):
        """prints the list in sorted order"""
        print(sorted(self))
