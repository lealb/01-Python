# -*- coding: utf-8 -*-
# Description:
# 2017/6/10:0:56

def getStrByList(list):
    if list is None:
        return None
    str = ''
    length = len(list)
    for i in range(length):
        if int(i) == length - 1:
            str += 'and'
        str += list[i]+","
    return str


spam = ['apples', 'bananas', 'tofu', 'cats']
print(getStrByList(spam))
