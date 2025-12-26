#!/usr/bin/python3
"hjdsfkhd"


class BaseGeometry:
    "dgdfgd"
    def __init__(self, width, height):
        if (type(width) and type(height) is int) and width * height > 0:
            self.__width = width
            self.__height = height
        raise Exception

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif int(value) <= 0:
            raise ValueError("{} must be greater than 0".format(name))
