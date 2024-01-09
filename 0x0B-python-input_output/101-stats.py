#!/usr/bin/python3
"""Reads from standard input and computes metrics
"""

import sys


# Define a function to print the metrics
def print_metrics(file_size, codes):
    """Print accumulated metrics
    """
    print("File size: {}".format(file_size))
    for code in sorted(codes):
        print("{}: {}".format(code, codes[code]))


# Initialize variables
file_size = 0
codes = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0

try:
    # Loop through the standard input
    for line in sys.stdin:
        # Split the line by spaces
        line = line.split()

        # Increment the line count
        line_count += 1

        # Update the file size
        try:
            file_size += int(line[-1])
        except (IndexError, ValueError):
            # Ignore invalid values
            pass

        # Update the codes dictionary
        try:
            status_code = line[-2]
            if status_code in valid_codes:
                codes[status_code] = codes.get(status_code, 0) + 1
        except IndexError:
            # Ignore invalid indices
            pass

        # Print the metrics every 10 lines
        if line_count == 10:
            print_metrics(file_size, codes)
            line_count = 0

    # Print the final metrics
    print_metrics(file_size, codes)

except KeyboardInterrupt:
    # Handle keyboard interrupt
    print_metrics(file_size, codes)
    raise
