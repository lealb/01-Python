# -*- coding: utf-8 -*-
# Description:如何进行和实现反向迭代
# 2017/6/21:2:37
from random import randint


def testIter():
    data = [randint(-10, 10) for _ in range(10)]

    print(data)
    # print(reversed(data)) # list_reverseiterator
    print(list(reversed(data)))
    print(data[::-1])


# 实例 实现分隔迭代器
class FloatRange(object):
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    # 正向迭代器
    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    # 反向迭代器
    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


if __name__ == "__main__":
    # testIter()

    for x in reversed(FloatRange(1.0, 5.0, 0.5)):
        print(x, end=" ")
