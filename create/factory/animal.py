#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Animal(object):
    def eat(self):
        raise NotImplementedError('can not use eat on Animal')

class Dog(Animal):
    def eat(self):
        print 'dog eat food'

class Cat(Animal):
    def eat(self):
        print 'cat eat food'