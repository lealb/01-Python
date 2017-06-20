# -*- coding: utf-8 -*-
# Description:如何在列表、字典、集合中根据条件删选数据
# 2017/6/20:13:33

from random import randint

# eg
if __name__ == "__main__":

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
