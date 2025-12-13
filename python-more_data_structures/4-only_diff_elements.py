#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    list = []
    for i in set_1:
        for j in set_2:
            if i != j:
                list.append(i)
    return list
