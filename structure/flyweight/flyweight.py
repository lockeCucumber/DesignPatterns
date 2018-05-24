#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import abc

class FlyweightBase(object):
    __metaclass__ = abc.ABCMeta

    _instances = dict()
    @abc.abstractmethod
    def __init__(self,*args,**kwargs):
        #继承的子类必须初始化,这里用abc使用
        raise NotImplementedError
 
    def __new__(cls, *args, **kwargs):
        #print(cls._instances,type(cls))
        return cls._instances.setdefault(
            (cls,args,tuple(kwargs.items())),
            super(FlyweightBase,cls).__new__(cls)
        )
 
    def test_data(self):
        pass
class Spam(FlyweightBase):
    '''精子类'''
 
    def __init__(self,a,b):
        self.a = a
        self.b = b
 
    def test_data(self):
        print "精子准备好了",self.a,self.b
class Egg(FlyweightBase):
    '''卵类'''
    def __init__(self,x,y):
        self.x = x
        self.y = y
 
    def test_data(self):
        print "卵子准备好了",self.x,self.y
 
 
 
spam1 = Spam(1,'abc')
spam2 = Spam(1,'abc')
spam3 = Spam(3,'DEF')
 
egg1 = Egg(1,'abc')
#egg2 = Egg(4,'abc')
assert spam1 is spam2
assert egg1 is not spam1
print(id(spam1),id(spam2))
spam2.test_data()
egg1.test_data()
print(egg1._instances)
print(egg1._instances.keys())

# Flyweight模式，顾名思义，就是共享元数据
# 在我们面向对象设计过程中，我们常常会面临着对象实例过多的问题，如果对象实例过多这将是我们系统性能提高的一个瓶颈。
# 假设我们要设计一个星空场景，现在我们需要实例星星对象，我们可以实例每一颗星星，但随着我们实例星星对象增多整个场景就越来越慢了，
# 如果你实例了1000+颗星星要你去维护，这可是一个吃力不讨好的工作。我们必须找到一个合适的方法解决以上问题，这就是今天要介绍的享元模式（Flyweight）。
 
# 享元模式（Flyweight）：运用共享的技术有效地支持大量细粒度的对象。
#
# 抽象享元角色（Flyweight）：此角色是所有的具体享元类的超类，为这些类规定出需要实现的公共接口或抽象类。那些需要外部状态(External State)的操作可以通过方法的参数传入。抽象享元的接口使得享元变得可能，但是并不强制子类实行共享，因此并非所有的享元对象都是可以共享的。
#
# 具体享元(ConcreteFlyweight)角色：实现抽象享元角色所规定的接口。如果有内部状态的话，必须负责为内部状态提供存储空间。享元对象的内部状态必须与对象所处的周围环境无关，从而使得享元对象可以在系统内共享。有时候具体享元角色又叫做单纯具体享元角色，因为复合享元角色是由单纯具体享元角色通过复合而成的。
#
# 复合享元(UnsharableFlyweight)角色：复合享元角色所代表的对象是不可以共享的，但是一个复合享元对象可以分解成为多个本身是单纯享元对象的组合。复合享元角色又称做不可共享的享元对象。这个角色一般很少使用。
#
# 享元工厂(FlyweightFactoiy)角色：本角色负责创建和管理享元角色。本角色必须保证享元对象可以被系统适当地共享。当一个客户端对象请求一个享元对象的时候，享元工厂角色需要检查系统中是否已经有一个符合要求的享元对象，如果已经有了，享元工厂角色就应当提供这个已有的享元对象；如果系统中没有一个适当的享元对象的话，享元工厂角色就应当创建一个新的合适的享元对象。
#
# 客户端(Client)角色：本角色还需要自行存储所有享元对象的外部状态。
#
# 内部状态与外部状态：在享元对象内部并且不会随着环境改变而改变的共享部分，可以称之为享元对象的内部状态，反之随着环境改变而改变的，不可共享的状态称之为外部状态。