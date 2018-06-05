# -*- coding: utf-8 -*-
# Author:leali
# Description: 反射？应该寻找相关资料好好补充
# Version:v1.0
# Date:6/5/2018-3:36 PM

class Foo():
    def __init__(self):
        self.name = "Leal"

    def func(self):
        return 'func'


if __name__ == "__main__":
    obj = Foo()
    # #### 检查是否含有成员 ####
    print("hasattr name:", hasattr(obj, 'name'))
    print("hasattr func1:", hasattr(obj, 'func1'))

    # #### 获取成员 ####
    print("getattr name:", getattr(obj, 'name'))
    getattr(obj, 'func')

    # #### 设置成员 ####
    setattr(obj, 'age', 18)
    setattr(obj, 'show', lambda num: num + 1)

    # #### 删除成员 ####
    delattr(obj, 'name')
    delattr(obj, 'func')
