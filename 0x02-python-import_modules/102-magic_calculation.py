#!/usr/bin/python3

def magic_calculation(num1, num2):
    """Match bytecode provided by Holberton School"""
    from magic_calculation_102 import add, sub

    x = num1 < num2
    if x:
        c = add(num1, num2)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(num1, num2)
