#!/usr/bin/python3

class CountedIterator:
    "hgjgfkj"
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.count = 0

    def get_count(self):
        return self.count

    def __iter__(self):
        return self

    def __next__(self):
    value = next(self.iterable)   # element götür
    self.count += 1               # SAYI ARTIR
    return value
