#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments"""
    import sys

    sum = 0  
    for index, argument in enumerate(sys.argv[1:]):  
        sum += int(argument)
    print("{}".format(sum))
