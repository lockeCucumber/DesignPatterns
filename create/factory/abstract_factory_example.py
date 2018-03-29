#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
抽象工厂模式
抽象工厂模式是工厂方法模式的归纳
通常一开始时使用工厂方法，因为它更简单。
如果后来发现应用需要许多工厂方法，那么将创建一系列对象的过程合并在一起更合理，
从而最终引入抽象工厂。
链接：https://www.jianshu.com/p/42f6cbd29e76
'''

#游戏模式分为两种，儿童是Frog，成人是Wizard,对应的工厂类是*World
class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Frog encounters {} and {}!'.format(self,
        obstacle, obstacle.action()))


class Bug:

    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld:

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Frog World -------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


    def interact_with(self, obstacle):
        print(
            '{} the Wizard battles against {} and {}!'.format(
            self,
            obstacle,
            obstacle.action()))


class Ork:

    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizardWorld:

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Wizard World -------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()

class GameEnvironment:

    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)

def validate_age(name):
    try:
        age = raw_input('Welcome {}. How old are you? '.format(name))
        age = int(age)
    except ValueError as err:
        print("Age {} is invalid, please try again...".format(age))
        return (False, age)
    return (True, age)

def main():
    name = raw_input("Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()

main()

# 使用工厂方法和抽象工厂设计模式。两种模式都可以用于以下几种场景:
# (a)想要追踪对象的创建时,
# (b)想要将对象的创建与使用解耦时，
# (c)想要优化应用的性能和资源占用时。