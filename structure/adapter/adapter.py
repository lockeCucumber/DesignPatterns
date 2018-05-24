# -*- coding: utf-8 -*-
class OldCourse(object):
    """
    老的课程类
    """

    def show(self):
        """
        显示关于本课程的所有信息
        """
        print("show description")
        print("show teacher of course")
        print("show labs")


class Page(object):
    """
    使用课程对象的客户端
    """

    def __init__(self, course):
        self.course = course

    def render(self):
        self.course.show()


class NewCourse(object):
    """
    新的课程类, 为了模块化显示课程信息，实现了新的课程类
    """
    def show_desc(self):
        """
        显示描述信息
        """
        print("show description")

    def show_teacher(self):
        """
        显示老师信息
        """
        print("show teacher of course")

    def show_labs(self):
        """
        显示实验
        """
        print("show labs")


class Adapter(object):
    """
    适配器, 尽管实现了新的课程类，但是在很多代码中还是需要使用 OldCourse.show() 方法
    """

    def __init__(self, course):
        self.course = course

    def show(self):
        """
        适配方法，调用真正的操作
        """
        self.course.show_desc()
        self.course.show_teacher()
        self.course.show_labs()


if __name__ == '__main__':
    old_course = OldCourse()
    page = Page(old_course)
    page.render()
    print("")
    new_course = NewCourse()
    # 新课程类没有 show 方法，我们需要使用适配器进行适配
    adapter = Adapter(new_course)
    page = Page(adapter)
    page.render()

# 在上面的代码中，我们原本有一个OldCourse类，它有一个方法OldCourse.show用于显示课程的所有相关信息，
# 并且在Page对象中用到。现在，为了适应模块化显示的需求，我们开发了新的课程类NewCourse，它只能分别显示课程的部分信息。
# 现在为了使NewCourse对象能在Page对象中也能正常工作，我们使用了适配器模式来兼容。
# 在适配器Adapter中，我们实现了Adapter.show()方法，它会调用NewCourse的一系列方法来完成显示整个课程信息的需求。
# 这样一来，我们直接将Adapter对象传递给Page对象就可以兼容老的接口，使系统正常运行。
