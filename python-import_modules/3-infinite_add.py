#!/usr/bin/python3
import sys

if __name__ == "__main__":
    list = sys.argv[1:]
    sum = 0
    for i in range(0, len(list)):
        sum += int(list[i])
