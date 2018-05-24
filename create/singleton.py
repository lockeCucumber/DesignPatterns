#!/usr/bin/env python
# -*- coding: utf-8 -*-
'单例模式'
import threading
import time

count = 0
id_set = set()

# 简单形式的单例模式，单线程ok，多线程有风险
class Singleton(object):
    '使用__new__'
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance
    def __init__(self):
        global count
        time.sleep(1)
        count += 1

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
    '使用__new__加锁'
    __instance = None

    @make_synchronized
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance
    
    def __init__(self):
        global count
        time.sleep(1)
        count += 1

# 定义类时就创建instance，实现多线程的单例
def _singleton(cls):
    instance = cls()
    instance.__call__ = lambda: instance
    return instance

@_singleton
class Singleton3:
    '使用__call__'
    def __init__(self):
        global count
        time.sleep(1)
        count += 1

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
    '使用装饰器处理类'
    def __init__(self):
        global count
        time.sleep(1)
        count += 1

# 本来想用于测试多线程情况，发现这个测试方法不对
def test(cls_param):
    def work():
        global id_set
        s = cls_param()
        id_set.add(id(s))

    tasks = []
    for _ in xrange(2000):
        t = threading.Thread(target=work)
        tasks.append(t)

    for i in tasks:
        i.start()
    for i in tasks:
        i.join()

    print cls_param.__doc__ ,count, len(id_set)

count = 0
id_set = set()
print '使用__new__创建单例，多线程结果'
test(Singleton)

count = 0
id_set = set()
print '在__new__基础上加互斥锁，多线程结果'
test(Singleton2)

count = 0
id_set = set()
print '使用__call__创建单例，多线程结果'
test(Singleton3)

count = 0
id_set = set()
print '给类使用装饰器创建单例，多线程结果'
test(Singleton4)