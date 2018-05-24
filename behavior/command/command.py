# -*- coding: utf-8 -*-

import abc


class VmReceiver(object):
    """
    命令接收者，真正执行命令的地方
    """

    def start(self):
        print("Virtual machine start")

    def stop(self):
        print("Virtual machine stop")


class Command(object):
    """
    命令抽象类
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        """
        命令对象对外只提供 execute 方法
        """
        pass


class StartVmCommand(Command):
    """
    开启虚拟机的命令
    """

    def __init__(self, recevier):
        """
        使用一个命令接收者初始化
        """
        self.recevier = recevier

    def execute(self):
        """
        真正执行命令的时候命令接收者开启虚拟机
        """
        self.recevier.start()


class StopVmCommand(Command):
    """
    停止虚拟机的命令
    """

    def __init__(self, recevier):
        """
        使用一个命令接收者初始化
        """
        self.recevier = recevier

    def execute(self):
        """
        真正执行命令的时候命令接收者关闭虚拟机
        """
        self.recevier.stop()


class ClientInvoker(object):
    """
    命令调用者
    """

    def __init__(self, command):
        self.command = command

    def do(self):
        self.command.execute()


if __name__ == '__main__':
    recevier = VmReceiver()
    start_command = StartVmCommand(recevier)
    # 命令调用者同时也是客户端，通过命令实例也执行真正的操作
    client = ClientInvoker(start_command)
    client.do()

    # 能告诉命令接收者执行不同的操作
    stop_command = StopVmCommand(recevier)
    client.command = stop_command
    client.do()

# 以上代码中，我们通过启动和停止 Linux 虚拟机的例子实现了命令模式。通过命令模式，使命令调用者ClinetInvoker和命令接收者VmRecevier之间解耦，前者不必知道后者具体是怎么操作虚拟机的，只需要通过ClientInvoker.do()方法调用Command.execute()方法能完成虚拟机的相关操作。

# 总的来说，命令模式的封装性很好：每个命令都被封装起来，对于客户端来说，需要什么功能就去调用相应的命令，而无需知道命令具体是怎么执行的。同时命令模式的扩展性很好，在命令模式中，在接收者类中一般会对操作进行最基本的封装，命令类则通过对这些基本的操作进行二次封装，当增加新命令的时候，对命令类的编写一般不是从零开始的，有大量的接收者类可供调用，也有大量的命令类可供调用，代码的复用性很好。
