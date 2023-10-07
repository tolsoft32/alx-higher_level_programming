#!/usr/bin/python3
""""Defining a rectangle class."""

class Rectangle:
    """This represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes new rectangle.
        Args:
            width (int): width of new rectangle.
            height (int): height of new rectangle.
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Gets/set width of rectangle."""
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
                raise TypeError("height has to be integer")
            if value < 0:
                raise ValueError("height has to be >-0")
            self.__height = value

        def area(self):
            """Returns area of rectangle."""
            return (self.__width * self.__height)

        def perimeter(self):
            """Return perimeter of rectangle."""
            if self.__width == 0 or self.__height == 0:
                return (0)
            return ((self.__width * 2) + (self.__height * 2))
