#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    if len(argv) % 2 == 0:
        print(f"{len(argv)} arguments:")
    elif len(argv) % 2 != 0:
        print(f"{len(argv)} argument:")
    else:
        print("0 arguments.")

    for i in range(0, len(argv)):
        print("{}: {}".format(i+1, argv[i]))
