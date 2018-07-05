# -*- coding: utf-8 -*-
# Author:leali
# Description: 测试运行效率问题
# Version:v1.0
# Date:2018-07-03-03:51 PM
import random
import cProfile


def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in l1 if i < 0.5]
    return [i * i for i in l2]


def f2(lIn):
    l1 = [i for i in lIn if i < 0.5]
    l2 = sorted(l1)
    return [i * i for i in l2]


def f3(lIn):
    l1 = [i * i for i in lIn]
    l2 = sorted(l1)
    return [i for i in l1 if i < (0.5 * 0.5)]


if __name__ == "__main__":
    lIn = [random.random() for i in range(100000)]
    cProfile.run('f1(lIn)')
    cProfile.run('f2(lIn)')
    cProfile.run('f3(lIn)')
