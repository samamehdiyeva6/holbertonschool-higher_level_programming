#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(0, x):
            print(int(my_list[i]), end = "")
    except IndexError:
        print("This index doesn't exist")
