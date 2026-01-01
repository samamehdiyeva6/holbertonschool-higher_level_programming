#!/usr/bin/python3

class CountedIterator:
    "hgjgfkj"
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        item = next(self._iterable)
        self._count += 1
        return item
