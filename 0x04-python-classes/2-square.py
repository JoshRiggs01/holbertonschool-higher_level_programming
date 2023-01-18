#!/usr/bin/python3
"""
this class define a square
"""
class Square:

    def __init__(self, size=0):


        """
        Initialize the square with a size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

            def area(self)
            """
            Return the current square area
            """
            return self.__size ** 2
