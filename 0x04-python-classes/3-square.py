#!/usr/bin/python3
class Square:
    """
    Class Square that defines a square by:
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0)
    size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception with the message size must be >= 0
    Public instance method: def area(self): that returns the current square area
    Public instance method: def my_print(self): that prints in stdout the square with the character #:
    if size is equal to 0, print an empty line
    """
    def __init__(self, size=0):
        """
        Initialize class with optional size

        Args:
        size (int): The size of the square. Default is 0.

        Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        Getter method for private attribute size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for private attribute size

        Args:
        value (int): The value to set size to

        Raises:
        TypeError: If value is not an integer
        ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Method that returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Method that prints in stdout the square with the character #.
        If size is equal to 0, print an empty line
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
