# -*- coding: utf-8 -*-


class User(object):
    """
    用户类
    """
    def is_login(self):
        return True

    def has_privilege(self, privilege):
        return True


class Course(object):
    """
    课程类
    """
    def can_be_learned(self):
        return True


class Lab(object):
    """
    实验类
    """
    def can_be_started(self):
        return True


class Client(object):
    """
    客户类，用于开始一个实验
    """
    def __init__(self, user, course, lab):
        self.user = user
        self.course = course
        self.lab = lab

    def start_lab(self):
        """
        开始实验，需要一系列的判断：用户是否登陆，课程是否可以学习，实验是否可以开始。判断非常繁琐！
        """
        if self.user.is_login() and self.course.can_be_learned() and self.lab.can_be_started():
            print("start lab")
        else:
            print("can not start lab")


class FacadeLab(object):
    """
    新的Lab类，应用了面向对象模式
    """

    def __init__(self, user, course, lab):
        self.user = user
        self.course = course
        self.lab = lab

    def can_be_started(self):
        if self.user.is_login() and self.course.can_be_learned() and self.lab.can_be_started():
            return True
        else:
            return False


class NewClient(object):
    """
    新的客户类，使用外观模式
    """
    def __init__(self, facade_lab):
        self.lab = facade_lab

    def start_lab(self):
        """
        开始实验，只需要判断 FacadeLab 是否可以开始
        """
        if self.lab.can_be_started:
            print("start lab")
        else:
            print("can not start lab")


if __name__ == '__main__':
    user = User()
    course = Course()
    lab = Lab()
    client = Client(user, course, lab)
    client.start_lab()

    print("Use Facade Pattern:")
    facade_lab = FacadeLab(user, course, lab)
    facade_client = NewClient(facade_lab)
    facade_client.start_lab()

# 所谓外观模式，就是将各种子系统的复杂操作通过外观模式简化，让客户端使用起来更方便简洁。
# 比如你夏天晚上出门时，要关闭电灯，关闭电视机，关闭空调，如果有了一个总开关，通过它可以关闭电灯，电视机和空调，你出门的时候关闭总开关就行了。
# 在这个例子中，你就是客户端，总开关就是外观模式的化身
