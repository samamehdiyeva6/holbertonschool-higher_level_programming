#!/usr/bin/python3
if __name__ == "__main__":
    argv = "Hello"
    list = argv.split()
    if len(list) % 2 == 0:
        print(f"{len(list)} arguments:")
    elif len(list) % 2 != 0:
        print(f"{len(list)} argument:")
    else:
        print("0 arguments.")

    for i in range(0, len(list)):
        print("{}: {}".format(i+1, list[i]))
