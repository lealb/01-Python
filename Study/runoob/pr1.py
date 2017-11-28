# -*- coding: utf-8 -*-
# Description: 有四个数字1-4，能组成多少个各不相同且无重复数字的三位数，各是多少
# 多种解题思路，掌握常规循环及其相关优化和最值法
# 学会利用已有函数，位运算等
# 2017/9/5 14:31


# 常规方法
# 优化1 使用continue
# 优化2 i！=j!=k
def testWay1():
    number = []
    for i in range(1, 5):  # [1,2,3,4]
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and j != k and k != i:  # Pythonic i!=j!=k
                    number.append(i * 100 + j * 10 + k)
    return number


# 混合迭代器
def testWay2():
    list_num = [1, 2, 3, 4]
    number = [i * 100 + j * 10 + k for i in list_num for j in list_num
              for k in list_num if i != j and j != k and k != i]
    return number


# 通过范围分解数字，避免循环
def testWay3():
    number = []
    for i in range(123, 433):
        a = i % 10  # 个
        b = i // 10 % 10
        c = i // 100
        if a != b and b != c and c != a and 0 < a < 5 and 0 < b < 5 and 0 < c < 5:
            number.append(i)
    return number


# 自带函数
from itertools import permutations


def testWay4():
    number = []
    for i in permutations([1, 2, 3, 4], 3):
        number.append(i)
        # k = ""
        # for j in range(0, len(i)):
        #     k += str(i[j])
        #     number.append(int(k))
    return number


# 位运算
# 从00 01 10 到 11 10 01
def testWay5():
    number = []
    for i in range(6, 58):
        a = i >> 4 & 3
        b = i >> 2 & 3
        c = i & 3
        if a ^ b and b ^ c and c ^ a:
            number.append((a + 1) * 100 + (b + 1) * 10 + c + 1)
    return number


if __name__ == '__main__':

    number = testWay5()
    line = 0
    print("Total number is ", len(number))
    print("Follows  is")
    for l in number:
        print(l, end=" ")
        line += 1
        if line == 10:
            print()
            line = 0
