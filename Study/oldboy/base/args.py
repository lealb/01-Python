# -*- coding: utf-8 -*-
# Author:leali
# Description: *args、**kwargs的使用
# Version:v1.0
# Date:2018-07-03-01:30 PM


l = [1, 2, 3]
t = (4, 5, 6)
d = {'a': 7, 'b': 8, 'c': 9}


def test1(*args, **kwargs):
    print("%s:%s" % (args, kwargs))


def for_test1():
    test1()
    test1(1, 2, 3)
    test1(1, 2, 3, 'gr')
    test1(a=1, b=2, c=3)
    test1(a=1, b=2, c=3, zzz="hello")
    test1(1, 2, 3, a=1, b=2, c=3)
    test1(*l, **d)
    test1(*t, **d)
    test1(1, 2, *t)
    test1(q="warning", **d)
    test1(1, 2, *t, q="warning", **d)


def test2(args1, args2, *args, **kwargs):
    print("%s-%s-%s:%s" % (args1, args2, args, kwargs))


def for_test2():
    # test2() #--():{}
    test2(1, 2, 3)
    test2(1, 2, 3, 'gr')
    test2(args1=1, args2=2, c=3)
    test2(args1=1, args2=2, c=3, zzz="hello")
    test2(1, 2, 3, a=1, b=2, c=3)
    test2(*l, **d)
    test2(*t, **d)
    test2(1, 2, *t)
    test2(1,2,q="warning", **d)
    test2(1, 2, *t, q="warning", **d)


if __name__ == "__main__":
    """
    *args:不确定要往函数中传入多少个参数，或者想往函数中以列表和元祖的形式传递参数--参数均会转换为()
    **kwargs: 不确定妖王函数中传入多少个关键词参数，或者想传入字典的值作为关键词参数
    约定俗成的写法，可以用其他的参数，但是不推荐
    """
    # for_test1()
    for_test2()
