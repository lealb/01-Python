# -*- coding: utf-8 -*-
# Description: 变量与数据类型
# 2018/1/4 20:11

def print_num():
    global num
    print(num)
    num = 10
    print(num)


if __name__ == '__main__':
    num = 5
    print_num()
    