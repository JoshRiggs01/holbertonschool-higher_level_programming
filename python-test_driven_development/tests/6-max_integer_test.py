#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([1, 3, 4, 4, 2]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([2]), 4)

if __name__ == '__main__':
    unittest.main()
