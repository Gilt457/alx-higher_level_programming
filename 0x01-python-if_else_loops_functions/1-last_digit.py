#!/usr/bin/python3
import random

def last_digit(number):
    if number < 0:
        return number % -10
    else:
        return number % 10

number = random.randint(-10000, 10000)
result = last_digit(number)
print(f"Last digit of {number} is {result} ", end="")

if result > 5:
    print(f"and is greater than 5")
elif result == 0:
    print(f"and is 0")
else:
    print(f"and is less than 6 and not 0")

