#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    if not isinstance(roman_string, str):
        return 0
    total = 0
    pre_v = 0
    for i in reversed(roman_string):
        value = roman.get(i, 0)

        if value < pre_v:
            total -= value
        else:
            total += value
        pre_v = value
    return total
