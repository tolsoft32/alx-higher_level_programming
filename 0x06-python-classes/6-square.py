#!/usr/bin/python3
class Square:
    """Square class

    defining square class
    """

    def __init__(self, size=0, position=(0,0)):
        """__init__

        __init__ method initializes the size of value of square

        Args:
            size(:obj :int, optional): The size of the square

        Raises:
            TypeError: If 'size' type is not 'int'
            
            ValueError: If 'size'is lesser than '0'.
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if self.__check_tuple(position) is False \
            or self.__check_indexes(position) is False \
            or self.__check_integers(position) is False \
            or self.__check_values(position) is False:
                raise TypeError('position must be a tuple of 2 positive integers')

        self.__postion = position

    def _check_tuple(self, position):
        if type(position) is tuple:
            return True

        return False

    def __check_indexes(Self, position):
        if len(position) == 2:
            return True

        return False

    def __check_integers(self, position):
        if type(position[0]) is int and type(position[1]) is int:
            return True

        return False

    def __check_values(self, position):
        if position[0] >= 0 and position[1] >= 0:
            return True

        return False

    def area(self):
        """Return the current square area

        """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return None

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print('')

        for j in range(1, self.area() + 1):
            if j % self.__size == 1:
                print('{:>{w}}'.format('#', w=self.__position[0] + 1), end='')
            else:
                print('#', end='')

            if j % self.__size == 0 and j > 0:
                print()
