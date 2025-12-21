#!/usr/bin/python3
"""hsagdjhgsdja"""


class Rectangle:
    "sdfsdfsd"
    pass

    def __init__(self, width=0, height=0):
        "jhkdhf"
        self.width = width
        self.height = height
    
    @property
    def width(self):
        self.__width = width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        self.__height = height

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if svalue < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
