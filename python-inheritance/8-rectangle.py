#!/usr/bin/python3
"hjdsfkhd"
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    "dgdfgd"
    def __init__(self, width, height):
        if (type(width) and type(height) is int):
            if width < 0:
                raise Exception("width must be greater than 0")
            if height < 0:
                raise Exception("height must be greater than 0")
            self.__width = width
            self.__height = height
        raise Exception("width must be greater than 0")
