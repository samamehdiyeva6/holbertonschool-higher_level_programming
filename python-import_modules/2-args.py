#!/usr/bin/python3
from argv_2 import arg

if __name__ == "__main__":
    argv = "Hello"
    length  = len(argv)
    if length % 2 == 0:
        print(f"{length} arguments:")
    elif length % 2 != 0:
        print(f"{length} argument:")
    else:
        print("0 arguments.")

    list = argv.split()
    for i in range(1, length+1):
        print("{}: {}".format(i, list[i-1]))
