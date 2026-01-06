#!/usr/bin/python3
"dsgdsg"
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        with open(filename, encoding="utf-8") as f:
            return pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, encoding="utf-8") as f:
            return pickle.load(f)
