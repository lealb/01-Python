# -*- coding: utf-8 -*-
# Author:leali
# Description: 单例模式，7种实现单例模式的方法
# Version:v1.0
# Date:2018-06-09-08:48 PM

class Test():
    """
     默认情况下是没有单例模式的
    """
    pass


class Singleton1(object):
    """
   方法一、staticmethod
   该方法的要点是在__init__抛出异常，禁止通过类来实例化，只能通过静态get_instance函数来获取实例；
   因为不能通过类来实例化，所以静态get_instance函数中可以通过父类object.__new__来实例化
   """
    instance = None

    def __init__(self):
        raise SyntaxError('can not instance, please use get_instance')

    @staticmethod
    def get_instance():
        if Singleton1.instance is None:
            Singleton1.instance = object.__new__(Singleton1)
        return Singleton1.instance


class Singleton2(object):
    """
    方法二、classmethod
    同1，初始化__init__抛出异常
    """
    instance = None

    def __init__(self):
        raise SyntaxError('can not instance,please use get_instance')

    @classmethod
    def get_instance(cls):
        if Singleton2.instance is None:
            Singleton2.instance = object.__new__(Singleton2)
        return Singleton2.instance


class Singleton3(object):
    """
    类属性方法
    """
    instance = None

    def __init__(self):
        raise SyntaxError('can not instance,please use get_instance')

    def get_instance(self):
        if Singleton3.instance is None:
            Singleton3.instance = object.__new__(Singleton3)
        return Singleton3.instance


class Singleton4(object):
    """
    __new__方法
    重写
    """

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            # cls.instance = object.__new__(cls, *args)
            cls.instance = super(Singleton4, cls).__new__(cls, *args, **kwargs)
        return cls.instance


def Singleton5(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance


@Singleton5
class MyClass:
    """
    装饰器方法
    单例类本身根本不知道自己是单例的,因为他本身(自己的代码)并不是单例的
    """
    pass


class Singleton6(type):
    """
    元类 metaclass
    """

    # python2 可以通过这样的方式实现
    # def __init__(cls, name, bases, dct):
    #     super(Singleton6, cls).__init__(name, bases, dct)
    #     cls.instance = None

    def __new__(cls, name, bases, attrs):
        attrs["_instance"] = None
        return super(Singleton6, cls).__new__(cls, name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton6, cls).__call__(*args, **kwargs)
        return cls._instance


# python2
class Foo(object):
    __metaclass__ = Singleton6


# python3
class Foo1(metaclass=Singleton6):
    pass


class Singleton7(object):
    """
    名字覆盖
    """
    def __call__(self):
        return self


if __name__ == "__main__":
    # test1 = Singleton2.get_instance()
    # test2 = Singleton2.get_instance()
    Singleton = Singleton7()
    test1 = Singleton()
    test2 = Singleton()
    print("test1:", id(test1))
    print("test2:", id(test2))
