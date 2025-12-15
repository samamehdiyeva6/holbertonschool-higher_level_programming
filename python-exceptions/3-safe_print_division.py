#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
    except Exception:
        return None
    finally:
        print("{:d}".format(res))
