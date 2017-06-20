# -*- coding: utf-8 -*-
# Description:如何为元组的每个元素命名，提高程序的可读性
# 2017/6/20:15:13

if __name__ == "__main__":
    # 通过类似其他语言的枚举形式实现
    # 方法1 常量赋值
    NAME, AGE, SEX, EMAIL = range(4)
    student = ("Leal", 24, "Male", "xxx@cc.com")

    print(student[NAME])

    # 方法2 使用内置collections 的 nametuple

    from collections import namedtuple

    Student = namedtuple('Student', ["name", "age", "sex", "email"])
    s = Student("Leal", 24, "Male", "xxx@cc.com")
    print(s.name)
    print(isinstance(s, tuple))
