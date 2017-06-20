# -*- coding: utf-8 -*-
# Description:如何根据字典中的值的大小，对字典的项排序
# 2017/6/20:17:33
from random import randint

if __name__ == "__main__":
    # 内置函数sorted
    data = {x: randint(50, 100) for x in "abcdefgh"}
    print(sorted(data))
    # zip 拼接为元组
    # py2的itervalues->values
    zipdata = zip(data.values(), data.keys())

    print(sorted(zipdata))
    # 方法2 内置key
    print(sorted(data.items(), key=lambda x: x[1]))
