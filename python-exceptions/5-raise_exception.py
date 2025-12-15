#!/usr/bin/python3
def raise_exception():
    try:
        raise Exception
    except Exception:
        print("Exception has been raised")
