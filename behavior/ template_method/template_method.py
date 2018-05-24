# -*- coding: utf-8 -*-

import abc


class Fishing(object):
    """
    钓鱼模板基类
    """
    __metaclass__ = abc.ABCMeta

    def finishing(self):
        """
        钓鱼方法中，确定了要执行哪些操作才能钓鱼
        """
        self.prepare_bait()
        self.go_to_riverbank()
        self.find_location()
        print("start fishing")

    @abc.abstractmethod
    def prepare_bait(self):
        pass

    @abc.abstractmethod
    def go_to_riverbank(self):
        pass

    @abc.abstractmethod
    def find_location(self):
        pass


class JohnFishing(Fishing):
    """
    John 也想去钓鱼，它必须实现钓鱼三步骤
    """

    def prepare_bait(self):
        """
        从淘宝购买鱼饵
        """
        print("John: buy bait from Taobao")

    def go_to_riverbank(self):
        """
        开车去钓鱼
        """
        print("John: to river by driving")

    def find_location(self):
        """
        在岛上选择钓点
        """
        print("John: select location on the island")


class SimonFishing(Fishing):
    """
    Simon 也想去钓鱼，它也必须实现钓鱼三步骤
    """

    def prepare_bait(self):
        """
        从京东购买鱼饵
        """
        print("Simon: buy bait from JD")

    def go_to_riverbank(self):
        """
        骑自行车去钓鱼
        """
        print("Simon: to river by biking")

    def find_location(self):
        """
        在河边选择钓点
        """
        print("Simon: select location on the riverbank")


if __name__ == '__main__':
    # John 去钓鱼
    f = JohnFishing()
    f.finishing()

    # Simon 去钓鱼
    f = SimonFishing()
    f.finishing()

# 模板方法模式是结构最简单的行为型设计模式，在其结构中只存在父类与子类之间的继承关系。
# 通过使用模板方法模式，可以将一些复杂流程的实现步骤封装在一系列基本方法中，
# 在抽象父类中提供一个称之为模板方法的方法来定义这些基本方法的执行次序，而通过其子类来覆盖某些步骤，
# 从而使得相同的算法框架可以有不同的执行结果。模板方法模式提供了一个模板方法来定义算法框架，而某些具体步骤的实现可以在其子类中完成。
