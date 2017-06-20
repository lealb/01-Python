# -*- coding: utf-8 -*-
# Description: 使用切片做迭代器操作
# 2017/6/21:3:05
from itertools import islice


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
    testLice()
