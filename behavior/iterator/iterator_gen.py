# -*- coding: utf-8 -*-
'结合yield做一个生成器，实现一个迭代器'

def gen(value, max_count):
    for _ in range(max_count):
        yield value