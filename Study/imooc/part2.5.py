# -*- coding: utf-8 -*-
# Description:如何快速找到多个字典的公共键
# 2017/6/20:18:00
from random import randint, sample
from functools import reduce

if __name__ == "__main__":
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
