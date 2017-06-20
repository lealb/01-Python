# -*- coding: utf-8 -*-
# Description: 实现用户的历史纪录(最对n条)
# 2017/6/20:19:03
from random import randint
from collections import deque
import pickle
import os


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


if __name__ == "__main__":
    # 实现方法
    #
    T = randint(10, 100)
    # 存储历史数据 采用队列先进先出的规律
    if os.path.exists('part2.7'):
        # 以byte 的形式写入与读出
        hisdata = pickle.load(open('part2.7','rb'))
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
