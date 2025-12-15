#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value.isdigit():
            return True
            print("{:d}".format(value))
        else:
            return False
    except Exception:
        pass
