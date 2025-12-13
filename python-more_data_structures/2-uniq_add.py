#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for i in my_list:
        count = 0
        for j in new_list:
            if i == j:
                count += 1
        if count == 0:
            new_list.append(i)
    total = 0
    for k in new_list:
        total += k
    return total
