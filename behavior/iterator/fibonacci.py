# -*- coding: utf-8 -*-
'一个斐波那契的生成器'

def generat_fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

a = generat_fib()
for i in a:
    print i
    if i > 10:
        break