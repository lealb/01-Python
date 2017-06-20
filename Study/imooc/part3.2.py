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


if __name__ == "__main__":
    # testIter()
    for x in WeatherIterable(["北京", "上海", "广州", "深圳"]):
        print(x)
