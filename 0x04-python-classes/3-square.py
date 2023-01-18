#!/usr/bin/python3
"""                                                                                       
Defines a square by its size.                                                             
"""

class Square:


    def __init__(self, size=0):
        """
        Initializes the square with an optional size.
        """
        self.size = size

    @property
    def size(self):
        """
        Gets the current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area.
        """
        return self.__size ** 2
