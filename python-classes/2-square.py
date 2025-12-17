#!/usr/bin/python3
"""This is an empty Square class."""


class Square:
    """Defines a square with a size attribute."""

    def __init__(self, size=0):
        """Initializes a square with a given size."""

        try:
            if not isinstance(size, int):
                print("size must be an integer")

            if size < 0:
                print("size must be >= 0")
            
            else:
                self.__size = size
