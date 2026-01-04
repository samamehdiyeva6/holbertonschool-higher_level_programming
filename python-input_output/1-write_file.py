#!/usr/bin/python3
"sdfsdfds"


def write_file(filename="", text=""):
    "fsdbhfsjk"
    try:
        with open(filename, 'w', encoding="utf-8") as f:
            return f.write(text)
    except FileNotFoundError:
        with open(filename, 'w', encoding="utf-8") as f:
            return f.write(text)
