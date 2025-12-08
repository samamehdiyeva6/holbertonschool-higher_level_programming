#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

if __name__ == "__main__":
    def element_at(my_list, idx):
        if idx < 0 or idx > len(my_list)-1:
            return None
        else:
            return my_list[idx]

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
