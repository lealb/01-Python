# -*- coding: utf-8 -*-
# Description: 统计随机序列中元素的出现频度
# 2017/6/20:15:27

from random import randint

if __name__ == "__main__":
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
