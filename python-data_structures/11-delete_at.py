#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if the index is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the same list if index is invalid
    
    # Remove the item by concatenating parts before and after the index
    return my_list[:idx] + my_list[idx+1:]