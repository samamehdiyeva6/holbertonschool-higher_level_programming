#!/usr/bin/python3
"sdfsdfds"


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            new_dict = {}
            for attr in attrs:
                if isinstance(attr, str) and attr in self.__dict__:
                    new_dict[attr] = self.__dict__[attr]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for attr in json.keys():
            self.__dict__[attr] = json[attr]
        return self.__dict__
