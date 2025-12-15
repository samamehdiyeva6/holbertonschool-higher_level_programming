#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        string = ""
        for i in range(0, x):
            string += str(my_list[i])
        print string
    except IndexError:
        print("This index doesn't exist")
