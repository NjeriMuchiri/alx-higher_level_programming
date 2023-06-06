#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Define unitests  for max_integer function"""

    def test_ordered_list(self):
        """Tests an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Tests an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Tests a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Tests an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Tests a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Tests a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Tests a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Tests a string."""
        string = "Ann"
        self.assertEqual(max_integer(string), 'n')

    def test_list_of_strings(self):
        """Tests a list of strings."""
        strings = ["Ann", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Tests an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_list_with_loop(self):
        """Tests a list with loop"""
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 25)

    def test_neg_numbers(self):
        """Tets a list with neg numbers"""
        self.assertEqual(max_integer([-10, -5, -2, -1]), -1)

    def test_zero_number(self):
        """Tets for a list with zeros"""
        self.assertEqual(max_integer([0, 0]), 0)

if __name__ == '__main__':
    unittest.main()
