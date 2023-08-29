#!/usr/bin/python3

"""Defining a Square class """

class Square:
    """square representation."""

    def __init__(self, size=0):
        """this initializes a new square.
        Attributes:
            size (int): size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
