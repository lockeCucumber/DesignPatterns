# -*- coding: utf-8 -*-
# 1．Bridge模式使用“对象间的组合关系”解耦了抽象和实现之间固有的绑定关系，使得抽象和实现可以沿着各自的维度来变化。
# 2．所谓抽象和实现沿着各自维度的变化，即“子类化”它们，得到各个子类之后，便可以任意它们，从而获得不同路上的不同汽车


class AbstractRoad(object):
    '''公路基类'''
    car = None
 
class AbstractCar(object):
    '''车辆基类'''
 
    def run(self):
        pass
 
class Street(AbstractRoad):
    '''市区街道'''
 
    def run(self):
        self.car.run()
        print("在市区街道上行驶")
 
class SpeedWay(AbstractRoad):
    '''高速公路'''
 
    def run(self):
        self.car.run()
        print("在高速公路上行驶")
 
 
class Car(AbstractCar):
    '''小汽车'''
    def run(self):
        print("小汽车在")
 
class Bus(AbstractCar):
    '''公共汽车'''
    def run(self):
        print("公共汽车在")
 
 
if __name__ == "__main__":
    #小汽车在高速上行驶
    road1 = SpeedWay()
    road1.car = Car()
    road1.run()
 
    road2 = SpeedWay()
    road2.car = Bus()
    road2.run()