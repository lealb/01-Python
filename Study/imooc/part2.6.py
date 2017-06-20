# -*- coding: utf-8 -*-
# Description:如何让字典保持有序
# 2017/6/20:18:35
from collections import OrderedDict
from time import time
from random import randint


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


if __name__ == "__main__":
    testPlayer()
