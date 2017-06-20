# -*- coding: utf-8 -*-
# Description:如何使用生成器函数实现可迭代对象
# 2017/6/20:22:35

import sys
import math


# 生成器函数 - 斐波那契
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


# 测试生成器
def testYield():
    f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
    while True:
        try:
            print(next(f), end=" ")
        except StopIteration:
            sys.exit()


# 指定范围内的素数 1不是质数
def primeNumbers(min, max):
    res = []
    for num in range(min, max + 1):
        # 质数大于1
        if num > 1:
            for j in range(2, int(math.sqrt(num) + 1)):
                if num % j == 0:
                    break
            else:
                res.append(num)

    return res


# 示例 通过类构造生成器
class PrimeNumber(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # 是否质数
    def isPrime(self, num):
        if num < 2:
            return False
        else:
            for i in range(2, int(math.sqrt(num) + 1)):
                if num % i == 0:
                    return False
        return True

    # 重写构造器
    def __iter__(self):
        for num in range(self.start, self.end + 1):
            if self.isPrime(num):
                yield num


if __name__ == "__main__":
    # testYield()
    # print(primeNumbers(2, 10))

    print(list(PrimeNumber(1, 10)))
