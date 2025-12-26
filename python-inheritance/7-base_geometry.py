#!/usr/bin/python3
"hjdsfkhd"


class BaseGeometry:
    "dgdfgd"
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value):
            raise TypeError("<name> must be an integer")
        if int(value) <= 0:
            raise ValueError("<name> must be greater than 0")
