#!/usr/bin/env python3
def uppercase(str):
    for char in str:
        if char.islower():
            char = chr(ord(char) - 32)
        print(char, end="")
    print()

