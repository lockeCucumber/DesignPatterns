# -*- coding: utf-8 -*-
import abc

class AbsShow(object):
    """
    抽象显示对象
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def show(self):
        pass


class AdminShow(AbsShow):
    """
    管理员的显示操作
    """

    def show(self):
        return "show with admin"


class UserShow(AbsShow):
    """
    普通用户的显示操作
    """

    def show(self):
        return "show with user"


class Question(object):
    """
    问题对象，使用策略模式之后的作法
    """

    def __init__(self, show_obj):
        self.show_obj = show_obj

    def show(self):
        return self.show_obj.show()



if __name__ == '__main__':
    q = Question(show_obj=AdminShow())
    print(q.show())
    # 替换原来的显示对象，体现了策略模式的互换行为
    q.show_obj = UserShow()
    print(q.show())

# 上面的代码中，我们将原来的 Question.show 抽象成了 AbsShow ，这个操作类负责显示信息。
# 然后我们分别基于该抽象类实现管理员显示类 AdminShow 和用户显示类 UserShow ，
# 这样一来我们就使操作和使用这些操作的客户端完全分开了。在最后我们重新实现了 Question ，
# 并且 Question.show 方法直接调用显示对象的显示方法。这样一来我们将 Question 对象和显示方法进行了解耦，
# 增加新的显示方法时，只需要增加新的显示对象就可以了。同时，在代码中还可以看到我们可以动态改变 Question 的显示方式，这也体现了策略模式的互换行为。
