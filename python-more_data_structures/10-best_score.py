#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    else:
        max = list(a_dictionary.values())[0]
        key = list(a_dictionary.keys())[0]
        for i in a_dictionary.keys():
            if max < a_dictionary[i]:
                max = a_dictionary[i]
                key = i
        return key
