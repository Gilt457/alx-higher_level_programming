#!/usr/bin/python3
"""
This module has a function that indents texts
"""


def text_indentation(text):
    """This function prints a text with 2 new lines after each ".", "?", or ":"

    Parameters:
        text (str): The string to be printed

    Raises:
        TypeError: If text is not a string

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    index = 0
    while index < len(text) and text[index] == " ":
        index += 1

    for char in text[index:]:
        print(char, end="")
        if char == "\n" or char in ".?:":
            if char in ".?:":
                print("\n")
            index += 1
            while index < len(text) and text[index] == " ":
                index += 1
        else:
            index += 1
