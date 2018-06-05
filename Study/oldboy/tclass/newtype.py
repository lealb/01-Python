# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:6/5/2018-3:03 PM


class MyType(type):
    """
    类的生成 调用 顺序依次是 __new__ --> __init__ --> __call__
    """
    def __init__(self, *args, **kwargs):
        print("MyType __init__:", *args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("MyType __call__:", *args, **kwargs)
        obj = self.__new__(self)
        print("obj:", obj, *args, **kwargs)
        print("self:", self)
        self.__init__(obj, *args, **kwargs)
        return obj

    def __new__(cls, *args, **kwargs):
        print("MyType __new__:", *args, **kwargs)
        return type.__new__(cls, *args, **kwargs)


class Foo(object, metaclass=MyType):
    def __init__(self, name):
        self.name = name
        print("Foo __init__:")

    def __new__(cls, *args, **kwargs):
        print("Foo __new__:", cls, *args, **kwargs)
        return object.__new__(cls)


if __name__ == "__main__":
    f = Foo('Leal')
    print("f:", f)
    print("f.name:", f.name)
