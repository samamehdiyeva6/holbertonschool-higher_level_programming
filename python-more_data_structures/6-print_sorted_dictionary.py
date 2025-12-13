#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list = []
    for i in a_dictionary.keys():
        list.append(i)
    list.sort()
    for j in list:
        print(j + ": " + a_dictionary.get(j))
