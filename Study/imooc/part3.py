# -*- coding: utf-8 -*-
# Description: 如何实现可迭代对象和迭代器对象
# 2017/6/20:19:49

# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
# 字符串，列表或元组对象都可用于创建迭代器：
from random import randint
import sys
import requests
import math
from itertools import islice

# 有点疑惑
def testIter():
    list1 = [randint(10, 100) for _ in range(10)]
    it = iter(list1)  # 创建迭代器对象
    print(next(it))  # 输出迭代器的下一个元素
    # 使用常规for语句进行遍历：
    for x in iter(list1):
        print(x, end=" ")
    # 使用next 函数
    while True:
        try:
            print(next(it), end=" ")
        except StopIteration:
            sys.exit()


# 案例测试 爬去城市天气信息并实时显示
from collections import Iterable, Iterator


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    # 爬去城市天气信息
    def getWeather(self, city):
        url = "http://wthrcdn.etouch.cn/weather_mini?city=" + city
        req = requests.get(url)
        data = req.json()['data']['forecast'][0]
        return "%s: %s/%s" % (city, data['low'], data['high'])

    # 重写next
    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

# 如何使用生成器函数实现可迭代对象
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

# 如何进行和实现反向迭代
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

# 使用切片做迭代器操作
def testLice():
    f = open("part2.3")
    lines = f.readlines()  # 文件会全部加载到内存中

    # print(lines[2:5])
    # 返回头部
    f.seek(0)
    # for line in f:
    #     print(line)
    for line in islice(f, 3, 6):
        print(line)
    print(list(islice(f, 4)))
    print(list(islice(f, 3, None)))
    # islice 迭代器会消耗原来的迭代 即从之前的迭代位置开始

if __name__ == "__main__":
    # testIter()
    for x in WeatherIterable(["北京", "上海", "广州", "深圳"]):
        print(x)
        # testYield()
    # print(primeNumbers(2, 10))

    print(list(PrimeNumber(1, 10)))
    # testIter()

    for x in reversed(FloatRange(1.0, 5.0, 0.5)):
        print(x, end=" ")


