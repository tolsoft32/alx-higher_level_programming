#!/usr/bin/python3

"""Defining a rectangle class."""

class Rectangle:
    """Representing a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle.

        Args:
            width (int): width of rectangle.
            height (int): height of a rectangle.
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Get/sets width of rectangle."""
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
            """Get/sets height of rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height has t be integer")
            if value < 0:
                raise ValueError("height has be >=0")
            self.__height = value
