#!/usr/bin/python3

"""Let define a Rectangle class."""

class Rectangle:
    """"This is a Rectangle class."""

    def __init__(self, width=0, height=0):
        """Initializes new Rectangle.
        Arguments:
        width(int): The width of new rectangle.
        height(int): The height of new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """set value of width."""
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self._width = value

    @property
    def height(self):
        """Get/set height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set value of height."""
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("value must be >= 0.")
        self.__height = value
