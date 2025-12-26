#!/usr/bin/python3
"hjdsfkhd"


class Rectangle(BaseGeometry):
    "dgdfgd"
    def __init__(self, width, height):
        if (type(width) and type(height) is int) and width * height > 0:
            self.__width = width
            self.__height = height
        raise Exception
