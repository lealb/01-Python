# -*- coding: utf-8 -*-
# Description:如何拆分含有多种分隔符的字符串
# 2017/6/21:3:22

# 方法1 依次分割
def mySplit(s, ds):
    res = [s]
    for d in ds:
        t = []
        list(map(lambda x: t.extend(x.split(d)), res))
        res = t
    return [x for x in res if x]

# 方法2 正则表达式 推荐
def testRe(s, ds):
    import re
    return re.split(r'[' + ds + ']+', s)


if __name__ == "__main__":
    str = 'ab;cd|efg|hi,,jkl|mn\topq;rst,uvw\tsyz'
    print(mySplit(str, ';|,\t'))

    print(testRe(str, ';|,\t'))
