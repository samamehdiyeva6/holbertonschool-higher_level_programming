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
        value = next(self.iterator)   # may raise StopIteration
        self.count += 1
        return value

