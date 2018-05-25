# -*- coding: utf-8 -*-

import copy

def Memento(obj, deep=False):
    # 对你要做快照的对象做快照
    state = (copy.copy if deep else copy.deepcopy)(obj.__dict__)
    def Restore():
        obj.__dict__ = state
    return Restore

class Transaction:

    deep = False
    def __init__(self, *targets):
        self.targets = targets
        self.Commit()
    # 模拟事务提交，其实就是初始化给每个对象往self.targets赋值
    def Commit(self):
        self.states = [Memento(target, self.deep) for target in self.targets]
    # 回滚其实就是调用Memento函数，执行其中的闭包，将__dict__恢复
    def Rollback(self):
        for state in self.states:
            state()

# 装饰器的方式给方法添加这个事务的功能
def transactional(method):
    # 这里的self其实就是要保存的那个对象，和类的实例无关
    def wrappedMethod(self, *args, **kwargs):
        state = Memento(self)
        try:
            return method(self, *args, **kwargs)
        except:
            # 和上面的回滚一样，异常就恢复
            state()
            raise
    return wrappedMethod

class NumObj(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return '<%s: %r>' % (self.__class__.__name__, self.value)
    def Increment(self):
        self.value += 1

    @transactional
    def DoStuff(self):
        # 赋值成字符串，再自增长肯定会报错的
        self.value = '1111'
        self.Increment()

if __name__ == '__main__':

    n = NumObj(-1)
    print n
    t = Transaction(n)
    try:
        for i in range(3):
            n.Increment()
            print n
        # 这里事务提交会保存状态从第一次的-1到2
        t.Commit()
        print '-- commited'
        for i in range(3):
            n.Increment()
            print n
        n.value += 'x' # will fail
        print n
    except:
        # 回滚只会回顾到上一次comit成功的2 而不是-1
        t.Rollback()
        print '-- rolled back'
    print n
    print '-- now doing stuff ...'
    try:
        n.DoStuff()
    except:
        print '-> doing stuff failed!'
        import traceback
        traceback.print_exc(0)
        pass
    # 第二次的异常回滚n还是2, 整个过程都是修改NumObj的实例对象
    print n

# 备忘录模式一个最好想象的例子：undo! 它对对象的一个状态进行了’快照’， 在你需要的时候恢复原貌。
# 做前端会有一个场景：你设计一个表单，当点击提交会对表单内容 验证，这个时候你就要对用户填写的数据复制下来，当用户填写的不正确或者格式不对等问题， 
# 就可以使用快照数据恢复用户已经填好的，而不是让用户重新来一遍，不是嘛？