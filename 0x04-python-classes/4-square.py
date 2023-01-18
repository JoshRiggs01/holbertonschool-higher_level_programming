#!/usr/bin/python3
class Square:
    """
    Defines a square by:
    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
    if size is equal to 0, print an empty line
    """
    def __init__(self, size=0):
        """
        Initialize square with size
        """
        self.size = size

    def area(self):
        """
        Calculates the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints square of size with #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """
        Getter for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

        
