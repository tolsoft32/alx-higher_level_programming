#!/usr/bin/python3

class Square:
    """Square class define."""

    def __init__(self, size=0):
        """Initialize new square
        Attribute:
            size (int): size og the new square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer.")
        elif size < 0:
            raise ValueError("size must be >=0.")
        self.__size = size

    def area(self):
        """This method return area of the square"""
        return (self.__size * self.__size)
