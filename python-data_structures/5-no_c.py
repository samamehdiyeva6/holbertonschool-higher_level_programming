#!/usr/bin/python3
def no_c(my_string):
    list = list(my_string)
    str = ""
    for i in list:
        if i != "c" or i != "C":
            str += i
