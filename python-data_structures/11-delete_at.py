#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Əgər index səhvdirsə, heç bir şey etməyəcək
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Verilən index-dəki elementi silirik
    my_list = my_list[:idx] + my_list[idx+1:]
    return my_list
