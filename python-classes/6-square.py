#!/usr/bin/python3
"""This is an empty Square class."""


class Square:
    """Defines a square with a size attribute."""

    def __init__(self, size=0):
        """Initializes a square with a given size."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Initializes a square with a given size."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    """hgjhg"""
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            for i in value:
                if i < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")