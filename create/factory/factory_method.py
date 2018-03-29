#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
工厂方法模式
创建抽象的工厂接口类，抽象的产品接口类。
产品接口派生产品子类，对于每一个产品子类，从工厂接口派生工厂子类，负责该产品的创建
'''
from animal import Animal, Dog, Cat

class AnimalFactory(object):
    def create_animal(self):
        raise NotImplementedError("can not use create_animal on AnimalFactory")

class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

animal_factory = DogFactory()
dog = animal_factory.create_animal()
dog.eat()

animal_factory = CatFactory()
cat = animal_factory.create_animal()
cat.eat()

# 如此一来，增加产品时不用改原有代码，只需要增加产品子类和工厂子类即可(加个FishFactory，Fish)
# 实际上，对于Java等强类型语言工厂方法可以使用，python是弱类型的，感觉没必要用
# 对于python实际上直接用下面方式就行
dog = Dog()
cat = Cat()

