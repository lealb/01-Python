# -*- coding: utf-8 -*-
# Description: 关于基本形式
# 2017/6/20:13:33

from random import randint, sample
from functools import reduce
from collections import OrderedDict, deque
from time import time
import pickle
import os


# 2.1 如何在列表、字典、集合中根据条件删选数据
def getData():
    list1 = [randint(-10, 10) for _ in range(10)]  # 过滤负数
    dist1 = {x: randint(50, 100) for x in range(1, 21)}
    set1 = set(list1)

    # l[start:end:span]
    # 遍历 [start,end)，间隔为 span，当 span>0 时顺序遍历, 当 span<0 时，逆着遍历。
    # start 不输入则默认为 0，end 不输入默认为长度。

    # 一般遍历写法
    res = []
    for i in range(0, len(list1)):
        if list1[i] > 0:
            res.append(list1[i])
    print(list1)
    print(res, ",", end="")
    print()
    # 链式写法 列表解析
    print(list(x for x in list1 if x > 0))
    # 匿名函数
    print(filter(lambda x: x >= 0, list1))
    print(filter(lambda x: x >= 80, dist1))
    print({k: v for k, v in dist1.items() if v >= 90})
    print({x for x in set1 if x % 3 == 0})
    # 使用timeit 可以测出时间快慢 timeit + 执行代码


# 2.2 如何为元组的每个元素命名，提高程序的可读性
def nameData():
    # 通过类似其他语言的枚举形式实现
    # 方法1 常量赋值
    NAME, AGE, SEX, EMAIL = range(4)
    student = ("Leal", 24, "Male", "xxx@cc.com")

    print(student[NAME])

    # 方法2 使用内置collections 的 nametuple

    from collections import namedtuple

    Student = namedtuple('Student', ["name", "age", "sex", "email"])
    s = Student("Leal", 24, "Male", "xxx@cc.com")
    print(s.name)
    print(isinstance(s, tuple))


# 2.3 统计随机序列中元素的出现频度
def getNumByData():
    # 方法1 使用原序列构造成字典形式后遍历
    data = [randint(20, 100) for _ in range(30)]
    res = dict.fromkeys(data, 0)
    for i in data:
        res[i] += 1
    print(sorted(res.values(), reverse=True))

    # 方法2 使用collections的Counter方法
    from  collections import Counter

    res1 = Counter(data)
    print(res1)
    # 通过most_common函数统计出词频最高的
    print(res1.most_common(3))

    # 通过正则表达式统计单词
    import re
    txt = open('part2.3').read()
    res2 = Counter(re.split('\W+', txt))
    print(res2.most_common(5))


# 2.4 如何根据字典中的值的大小，对字典的项排序
def orderByKey():
    # 内置函数sorted
    data = {x: randint(50, 100) for x in "abcdefgh"}
    print(sorted(data))
    # zip 拼接为元组
    # py2的itervalues->values
    zipdata = zip(data.values(), data.keys())

    print(sorted(zipdata))
    # 方法2 内置key
    print(sorted(data.items(), key=lambda x: x[1]))


# 2.5 如何快速找到多个字典的公共键
def findCommonKey():
    def getRandDict():
        return {x: randint(1, 4) for x in sample("abcdefgh", randint(1, 7))}

    dict1, dict2, dict3 = getRandDict(), getRandDict(), getRandDict()
    # 方法1 传统遍历
    res1 = []
    for k in dict1:
        if k in dict2 and k in dict3:
            res1.append(k)
    print(res1)

    # 方法2viewkeys
    res2 = reduce(lambda a, b: a & b, map(dict.keys(), [dict1, dict2, dict3]))
    print(res2)


# 2.6 如何让字典保持有序
# 测试用法
def testOrder():
    # dict1 = {} 正常无序字典
    # 有序字典
    dict1 = OrderedDict()
    dict1["b"] = {(2, 30)}
    dict1["q"] = {(3, 36)}
    dict1["d"] = {(4, 38)}
    dict1["c"] = {(5, 39)}
    dict1["s"] = {(7, 40)}
    dict1["t"] = {(9, 46)}
    dict1["c"] = {(6, 50)}
    print(dict1)


# 场景示例
# 比赛成绩录入字典 依次输出排名
def testPlayer():
    result = OrderedDict()
    player = list("ABCDEFGH")
    start = time()
    for i in range(len(player)):
        input()  # 敲击回车作为时间结束标志
        p = player.pop(randint(0, 7 - i))
        end = time()
        print("成绩录入：")
        print(i + 1, p, end - start)
        result[p] = (i + 1, end - start)

    print("名次输出:")
    print(result)
    # 字典存储方便不需要遍历即可查找到某一位palyer的成绩情况


# 2.7 实现用户的历史纪录(最对n条)
# 猜数方法
def guessDigt(g, t):
    if g == t:
        print("Right")
        return True
    if g > t:
        print("Greater-Than")
    else:
        print("Less-Than")
    return False


# 主函数
def partSenven():
    # 实现方法
    T = randint(10, 100)
    # 存储历史数据 采用队列先进先出的规律
    if os.path.exists('part2.7'):
        # 以byte 的形式写入与读出
        hisdata = pickle.load(open('part2.7', 'rb'))
        print(hisdata)
    else:
        hisdata = deque([], 5)
    while True:
        gnum = input()
        if gnum.isdigit():
            gnum = int(gnum)
            # 存储历史
            hisdata.append(gnum)
            if guessDigt(gnum, T):
                # 存为文件
                pickle.dump(hisdata, open('part2.7', 'wb'))
                break
        elif gnum == "h":
            print("历史输入:", hisdata)
        else:
            print("Input a Number")


if __name__ == "__main__":
    getData()
