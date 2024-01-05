#!/usr/bin/python3
"""Tests for max_integer([..]) function."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):
    """Tests for max_integer([..]) function."""

    def test_sorted_list(self):
        """Test a sorted list of integers."""
        sorted_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(sorted_list), 4)

    def test_random_list(self):
        """Test a random list of integers."""
        random_list = [1, 2, 4, 3]
        self.assertEqual(max_integer(random_list), 4)

    def test_max_at_start(self):
        """Test a list with a max value at the start."""
        max_at_start = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_start), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_single_element_list(self):
        """Test a list with only one element."""
        single_element_list = [7]
        self.assertEqual(max_integer(single_element_list), 7)

    def test_float_list(self):
        """Test a list of floats."""
        float_list = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(float_list), 15.2)

    def test_mixed_list(self):
        """Test a list of mixed ints and floats."""
        mixed_list = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(mixed_list), 15.5)

    def test_string_input(self):
        """Test a string input."""
        string_input = "Brennan"
        self.assertEqual(max_integer(string_input), 'r')

    def test_string_list(self):
        """Test a list of strings."""
        string_list = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(string_list), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
