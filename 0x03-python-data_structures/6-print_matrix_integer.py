#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # join the formatted elements of each row with spaces
        row_str = " ".join("{:d}".format(col) for col in row)
        # print the row string
        print(row_str)
