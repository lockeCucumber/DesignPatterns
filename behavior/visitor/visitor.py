#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Visitor(object):
    def __init__(self, type_):
        self.type_ = type_


class Obj(object):
    def __init__(self, visitor):
        self.visitor_type = visitor.type_
        self.sell_price = 100

    def show(self):
        if self.visitor_type == 'buyer':
            print('to buyer: it sell ￥', self.sell_price)
        elif self.visitor_type == 'seller':
            print('to seller: it cost ￥', self.sell_price * 0.8)
        else:
            print("undefined")


def main():
    seller = Visitor('seller')
    obj = Obj(seller)
    obj.show()
    buyer = Visitor('buyer')
    obj = Obj(buyer)
    obj.show()


if __name__ == '__main__':
    main()
