#!/usr/bin/python3
"""Defining a rectangular class."""

class Rectangle:
    """This represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle.
        Args:
            width (int): width of a new rectangle.
            height (int): height of a new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/sets widths of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width has to be integer")
        if value < 0:
            raise ValueError("width has to be >=0")
        self.__width = value

    @property
    def height(self):
        """"Get/setsheight of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height has to be integer")
        if value < 0:
            raise ValueError("height has to be >=0")
        self.__height = value

    def area(self):
        """Returns area of rectangle."""
        return (self.__width * self.__height)

    def primeter(self):
        """Returns perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width *2) + (self.__height * 2))
