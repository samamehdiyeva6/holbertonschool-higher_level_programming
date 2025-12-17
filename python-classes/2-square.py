#!/usr/bin/python3
"""This is an empty Square class."""


class Square:
    """Defines a square with a size attribute."""

    def __init__(self, size=0):
        """Initializes a square with a given size."""

        try:
            if isinstance(size, int):
                self.__size = size
            else:
                raise TypeError
        except TypeError:
            print("size must be an integer")

        try:
            if size < 0:
                self.__size = size
            else:
                raise ValueError
        except ValueError:
            print("size must be >= 0")
