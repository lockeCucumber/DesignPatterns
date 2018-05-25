# -*- coding: utf-8 -*-

class Mediator(object):
    online_list = []

    @classmethod
    def register(cls, person):
        cls.online_list.append(person)

    @classmethod
    def send(cls, send_p, recv_p, msg):
        if send_p in cls.online_list and recv_p in cls.online_list:
            recv_p.recv(send_p, msg)

class Person(object):
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

    def recv(self, send_p, msg):
        print '{} send msg {}'.format(send_p.name, msg)

p1 = Person('locke')
p2 = Person('lucy')

Mediator.register(p1)
Mediator.register(p2)
Mediator.send(p1,p2,'i love u')


# 中介者模式（Mediator Pattern）是用来降低多个对象和类之间的通信复杂性。
# 这种模式提供了一个中介类，该类通常处理不同类之间的通信，并支持松耦合，使代码易于维护。
# 中介者模式属于行为型模式。每个人通过平台发送消息，通过平台接收消息。