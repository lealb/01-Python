# -*- coding: utf-8 -*-
# Author:leali
# Description: with 原理测试
# Version:v1.0
# Date:5/18/2018-4:48 PM

class WithTest(object):
    def __enter__(self):
        print("Execute Enter:")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Execute Exit:")
        print("错误类型:", exc_type)
        print("错误类型对应的值:", exc_val)
        print("代码中错误发生的位置:", exc_tb)

    def do_something(self):
        bar = 1 / 0
        return bar + 10


if __name__ == "__main__":
    with WithTest() as test:
        test.do_something()

