#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        list = []
        for i in range(0, len(my_list_1)):
            list.append(my_list_1[i] / my_list_2[i])
        return list
    except TypeError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")
    finally:
        return list
