#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 and idx >= len(my_list):
        return my_list
    else:
        new_list = []
        for i in range(0, len(my_list)):
            if i != idx:
                new_list.append(my_list[i])
        my_list = new_list
        return my_list
