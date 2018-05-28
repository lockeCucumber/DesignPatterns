# -*- coding: utf-8 -*-
'用类实现一个迭代器'

class Iter(object):

    def __init__(self, value, max_count):
        self.value = value
        self.max_count = max_count
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.count += 1
        return self.value

    def next(self):
        return self.__next__()