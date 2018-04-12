#!/usr/bin/env python
# -*- coding: utf-8 -*-
'建造者模式'
'''
建造者模式将产品的创建流程提取到指挥者中，建造者则扮演机器人的角色，
没有自主意识，只知道按照命令做相应的工作，建造者模式的适应场景有限且明确，
在特定场景下的优势是比较明显的
'''

class Builder(object):
    """基类"""
    def Part1(self):
        # 不同类型的产品，该步骤的细节可能不同
        raise NotImplementedError()      

    def Part2(self):
        # 不同类型的产品，该步骤的细节可能不同
        raise NotImplementedError()

class Builder1(Builder):
    """派生类，生产builder1类型的产品""" 
    def Part1(self):
        print 'builder1 Part1'

    def Part2(self):
        print 'builder1 Part2'

class Builder2(Builder):
    """派生类，生产builder2类型的产品"""
    def Part1(self):
        print 'builder2 Part1'

    def Part2(self):
        print 'builder2 Part2'

class Director(object):
    """指挥者，负责组织产品的构建过程"""
    def Build(self, builder):
        builder.Part1()
        builder.Part2()

def client():
    director = Director()
    director.Build(Builder1())
    director.Build(Builder2())
