#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
简单工厂模式
使用场景：创建对象种类少，客户仅知道传入参数，对如何创建对象不关心
容易违背迪米特法则（高内聚低耦合），简单场景下使用
'''
from animal import Animal, Dog, Cat

# 工厂函数
def create_animal(name):
    if name == 'dog':
        return Dog()
    elif name == 'cat':
        return Cat()
    else:
        raise Exception("error input")

dog = create_animal('dog')
dog.eat()
cat = create_animal('cat')
cat.eat()