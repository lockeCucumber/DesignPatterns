#!/usr/bin/env python
# -*- coding: utf-8 -*-
'单例模式'
import threading

# 简单形式的单例模式，单线程ok，多线程有风险
class Singleton(object):
    __instance = None
    x = 0

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, num):
        self.num = num

# 添加同步锁的单例模式（懒汉加同步锁，挺好）
try:
    from synchronize import make_synchronized
except ImportError:
    def make_synchronized(func):
        func.__lock__ = threading.Lock()

        def synced_func(*args, **kwargs):
            with func.__lock__:
                return func(*args, **kwargs)
        return synced_func

class Singleton2(object):
    __instance = None
    x = 0

    @make_synchronized
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, num):
        self.num = num

# 定义类时就创建instance，实现多线程的单例
def _singleton(cls):
    instance = cls()
    instance.__call__ = lambda: instance
    return instance

@_singleton
class Singleton3:
    x = 0

# 理解方便的定义类时就创建instance，实现多线程的单例
def singleton(cls):
    instances = dict()  # 初始为空
    def _singleton(*args, **kwargs):
        if cls not in instances:  #如果不存在, 则创建并放入字典
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton

@singleton
class Singleton4(object):
    x = 0

    def __init__(self, num):
        self.num = num

# 本来想用于测试多线程情况，发现这个测试方法不对
def test():
    def work():
        s = Singleton4(1)
        s.x += 1
        print s.x

    tasks = []
    for _ in xrange(400000):
        t = threading.Thread(target=work)
        tasks.append(t)

    for i in tasks:
        i.start()
    for i in tasks:
        i.join()
test()