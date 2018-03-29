#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
抽象工厂模式
抽象工厂模式是工厂方法模式的归纳
通常一开始时使用工厂方法，因为它更简单。
如果后来发现应用需要许多工厂方法，那么将创建一系列对象的过程合并在一起更合理，
从而最终引入抽象工厂。
链接：https://www.jianshu.com/p/42f6cbd29e76
'''
from animal import Animal, Dog, Cat
from factory_method import AnimalFactory, DogFactory, CatFactory

class Shop(object):
    def __init__(self, factory):
        self.animal = factory.create_animal()
    
    def show(self):
        print 'look:'
        self.animal.eat()

if __name__ == '__main__':
    shop = Shop(DogFactory())
    shop.show()

    shop = Shop(CatFactory())
    shop.show()


# 使用工厂方法和抽象工厂设计模式。两种模式都可以用于以下几种场景:
# (a)想要追踪对象的创建时,
# (b)想要将对象的创建与使用解耦时，
# (c)想要优化应用的性能和资源占用时。