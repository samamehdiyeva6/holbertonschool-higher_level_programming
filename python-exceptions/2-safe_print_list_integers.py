#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for i in range(x):
        try:
            # yalnız int olanları çap et
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            # int olmayanları səssizcə at
            pass

    print()
    return count
