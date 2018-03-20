# -*- coding: utf-8 -*-
# Description: 高阶函数使用
# 2018/3/20 15:05
from functools import reduce


def square(x):
    """:return a square result"""
    return x * x


def add(x, y):
    """:return x+y result"""
    return x + y


def simple_test(list1):
    return list(map(square, list1)), reduce(add, list1)


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2int(s):
    """user-defined int() functions
    decimal number
    """
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def user_reversed(x, y):
    """
    In py2, sorted is higher-order function,if you need compare characters with ignore case,
    can convert lower()/upper()
    :param x:
    :param y:
    :return:
    """
    if x > y:
        return -1
    if x < y:
        return 1
    return 0


def user_sum(*args):
    """
    as system-defined sum()
    :param args:
    :return:
    """
    res = 0
    for i in args:
        res += i
    return res


def lazy_sum(*args):
    """
    closure example
    :param args:
    :return:
    """

    def use_sum():
        res = 0
        for i in args:
            res += i
        return res

    return use_sum


def user_map(func, seq):
    result = []
    for x in seq:
        result.append(func(x))
    return result


def user_reduce(func, seq):
    tally = seq[0]
    for ne in seq[1:]:
        tally = func(tally, ne)
    return tally


def get_not_empty_str(str):
    return filter(lambda s: s and s.strip(), str)


if __name__ == '__main__':
    l1 = [1, 3, 2, 34, 231, -2, -23, 243]
    print(simple_test(l1))
    print(user_map(lambda x: x * x * x, l1))
    print(str2int('234') + 2, int('234') + 2)
    # print(sorted(l1, user_reversed))
    print(lazy_sum(-23, 2, 3, 45))
    print(lazy_sum(-23, 2, 3, 45)())
    print(user_reduce(lambda x, y: x / y, l1))
    print(list(filter(lambda x: x % 2 > 0, range(-5, 5))))
