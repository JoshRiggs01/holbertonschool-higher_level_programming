#!/usr/bin/python3
"""Unittest for max_integer([])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test fixture for max_integer function."""

    def single_int_test(self):
        """single integer tests"""
        v1 = [36]
        self.assertEqual(max_integer(v1), 36)

    def multi_int_test(self):
        """list of integers"""
        v1 = [2, 3, 5, 8, 13, 21, 34]
        test = max_integer(v1)
        self.assertEqual(test, 34)

    def not_int_test(self):
        """non integer test"""
        v1 = [2, 3, 5, "hi", 13, 21, 34]
        test = max_integer(v1)
        self.assertRaises(TypeError, max_integer, test)

    def test_empty(self):
        """empty list"""
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def test_negative(self):
        """list of negative integers"""
        l = [-2, -6, -1]
        result = max_integer(l)
        self.assertEqual(result, -1)

    def test_float(self):
        """list including a float"""
        l = [3, 4.5, 2]
        result = max_integer(l)
        self.assertEqual(result, 4.5)

    def test_not_list(self):
        """not a list"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        """list of one var: should return the value"""
        l = [45]
        result = max_integer(l)
        self.assertEqual(result, 45)

    def test_identical(self):
        """list of same integers"""
        l = [8, 8, 8, 8, 8]
        result = max_integer(l)
        self.assertEqual(result, 8)

    def test_strings(self):
        """list of one var with string variable"""
        l = ["hi", "hello"]
        result = max_integer(l)
        self.assertEqual(result, "hi")

    def test_none(self):
        """test with none as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()