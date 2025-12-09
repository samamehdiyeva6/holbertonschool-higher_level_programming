#!/usr/bin/python3
def no_c(my_string):
    new_list = list(my_string)
    str = ""
    for i in new_list:
        if i != "c" or i != "C":
            str += i
    return str
