# -*- coding: utf-8 -*-
# Description: 一个整数，它加上100是个完全平方数，再加上168又是一个完全平方数，求该数
# 2017/9/5 17:51
import math


def isSqrt(num):
    a = int(math.sqrt(num))
    return a * a == num


def testWay1():
    num = []
    for i in range(-100, 10000):
        if isSqrt(i + 100) and isSqrt(i + 268):
            num.append(i)
    return num


if __name__ == '__main__':
    result = testWay1()
    for i in result:
        print(i, end="\t")
