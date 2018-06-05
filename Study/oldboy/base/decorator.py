# -*- coding: utf-8 -*-
# Author:lealid
# Description: 装饰器的使用,此外还有很多高级操作，例如同步锁等等使用的案例，待完善
# Version:v1.0
# 2018/3/23 9:57
import time
from functools import wraps


def foo1(func):
    """
    函数名作为参数
    :param func:
    :return:
    """
    print('foo1')
    func()


def bar():
    print('bar')
    time.sleep(1)


def foo2():
    """
    函数作为返回值
    :return:
    """
    print('foo2')
    return bar


def foo3():
    print('foo3')
    x = 1

    def bar1():
        print('bar%d' % x)

    return bar1


def show_time(func):
    """
    打印运行时间的装饰器
    :param func:
    :return:
    """

    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Spend %s" % (end_time - start_time))

    return wrapper


origin = [0, 0]
legal_x = [0, 50]
legal = [0, 50]


def create(pos=origin):
    """
    当闭包完成后，忍让能够保持住当前的运行环境
    :param pos:
    :return:
    """

    def player(direction, step):
        """
        采用闭包记录上次移动的位置，在此基础上继续移动
        :param direction:
        :param step:
        :return:
        """
        pos[0] += direction[0] * step
        pos[1] += direction[1] * step
        return pos

    return player


def make_filter(keep):
    """
    闭包可以根据外部作用域的局部变量来得到不同的结果
    :param keep:
    :return:
    """

    def the_filter(file_name):
        """
        根据不同的过滤条件可以过滤不同的文件
        :param file_name:
        :return:
        """
        with open(file_name) as file:
            lines = file.readlines()
        return (line for line in lines if keep in line)

    return the_filter


@show_time
def bar1():
    print('bar1')
    time.sleep(1)


def show_time_withparm(func):
    """
    带参数的装饰器
    :param func:
    :return:
    """

    def warpper(a, b):
        start = time.time()
        result = func(a, b)
        end = time.time()
        print("Speed %s" % (end - start))
        return result

    return warpper


@show_time_withparm
def add(a, b):
    time.sleep(1)
    return a + b


def show_time_with_notsure_parm(func):
    """
    带不定长参数的装饰器
    :param func:
    :return:
    """

    def warpper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Speed %s" % (end - start))
        return result

    return warpper


@show_time_with_notsure_parm
def add(*args, **kwargs):
    sum = 0
    for i in args:
        sum += i
    time.sleep(1)
    return sum


def logger(flag=False):
    """
    嵌套带参数的装饰器
    :param flag:
    :return:
    """

    def show_time_with_notsure_parm(func):
        """
        带不定长参数的装饰器
        :param func:
        :return:
        """

        def warpper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print("Speed %s" % (end - start))
            if flag:
                print('启动日志记录')
            return result

        return warpper

    return show_time_with_notsure_parm


@logger(True)
def add_with(*args, **kwargs):
    sum = 0
    for i in args:
        sum += i
    time.sleep(1)
    return sum


def make_bold(fn):
    def warpper():
        return '<b>' + fn() + '</b'

    return warpper


def make_italic(fn):
    def warpper():
        return '<i>' + fn() + '</i>'

    return warpper


@make_italic
@make_bold
def say_hello():
    return 'hello'


class Fun(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        start = time.time()
        self._func()
        end = time.time()
        print("Speed: %s" % (end - start))


@Fun
def divide():
    # if b == 0:
    #     return 0
    time.sleep(1)
    print('Class decorator:%f' % (3 / 2))


def logged(func):
    """
    装饰器会极大地复用了代码，但是这样导致原函数的元信息丢失
    :param func:
    :return:
    """

    @wraps(func)  # 使用前__name__为with_logging
    def with_logging(*args, **kwargs):
        """
        可采用functools的warps方法进行复制
        :param args:
        :param kwargs:
        :return:
        """
        print(func.__name__ + "as called")
        return func(*args, **kwargs)

    return with_logging


@logged
def test_warp():
    """
    测试装饰器复用代码但是原函数的元信息
    """
    print(test_warp.__name__)
    print(test_warp.__doc__)
    return 0


if __name__ == '__main__':
    # foo1(bar)
    # foo2()()
    # foo3()()
    # player = create()
    # print(player([1, 0], 10))
    # print(player([0, 1], 15))
    # print(player([1, 1], 10))
    # for i in make_filter('bar')('test'):
    #     print(i)
    # bar = show_time(bar)
    # bar()
    # bar1()
    # print(add(1234224223, 23234234234))
    # print(add(1, 2, 3, 4, 5, 6))
    # print(add_with(1, 2, 3, 4, 5, 6))
    # print(say_hello())
    # divide()
    test_warp()
