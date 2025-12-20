#!/usr/bin/python3
"""This is an empty Square class."""


class Square:
    """Defines a square with a size attribute."""

    def __init__(self, size=0, position=(0, 0)):
            "sduhfushd"
            self.size = size
            self.position = position

    @property
    def size(self):
        "bkhh"
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
    
    @property
    def position(self):
        "jhvjv"
        return self.__position

    @position.setter
    def position(self, value):
        "ghfhfh"
        if (not isinstance(value, tuple)
        or len(value) != 2 or
        not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        "jhfhgf"
        return self.__size ** 2

    """hgjhg"""
    def my_print(self):
        "jnkhjh"
        if self.__size == 0:
            print("")
            return
        
        [print("") for i in range(0, self.__position[1])]
        for j in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
