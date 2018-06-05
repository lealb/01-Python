# -*- coding: utf-8 -*-
# Author:leali
# Description: 类的特殊成员
# Version:v1.0
# Date:5/22/2018-10:17 AM

class Foo(object):
    """
    这是一个测试类，类的__doc__方法可以调用该内容
    """

    def __init__(self, id, name, age):
        """
        类的构造函数
        :param id:
        :param name:
        :param age:
        """
        self.__id = id
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        """
        在对象()的时候被调用
        :param args:
        :param kwargs:
        :return:
        """
        print("__call__")

    def __str__(self):
        """
        打印对象
        :return:
        """
        return "This is :"

    # 以下是索引操作
    def __getitem__(self, key):
        print("__getitem__", key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print("__delitem__", key)
    # 以下是分片处理,在py3中__getslice__被废弃
    #__getslice__(), __setslice__() and __delslice__() were killed. The syntax a[i:j] now translates to
    # a.__getitem__(slice(i, j)) (or __setitem__() or __delitem__(),
    # when used as an assignment or deletion target, respectively).

    # https://stackoverflow.com/questions/27850161/what-should-i-use-instead-of-getslice?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    def __del__(self):
        """
        类的析构函数，清理资源
        :return:
        """
        print("__del__被调用了")


if __name__ == "__main__":
    f = Foo(123, "Leal", 25)
    f()
    print(f)
    print(f.name)
    print(f.__doc__)  # 表示类的描述信息
    print(f.__module__)  # __module__ 表示当前操作的对象在那个模块
    print(f.__class__)  # __class__     表示当前操作的对象的类是什么
    print(Foo.__dict__)  # 获取类的成员，即：静态字段、方法
    print(f.__dict__)  # 获取对象的成员
    result = f['k1']      # 自动触发执行 __getitem__
    f['k2'] = 'leal'   # 自动触发执行 __setitem__
    del f['k1']           # 自动触发执行 __delitem__
