# -*- coding: utf-8 -*-
# Author:leali
# Description: Py3的多继承
# Version:v1.0
# Date:5/21/2018-11:09 AM

class A:
    def bar(self):
        print("A.bar")


class B(A):
    def bar1(self):
        print("B.bar")


class C(A):
    def bar(self):
        print("C.bar")


class D(B, C):
    def bar1(self):
        print("D.bar")


if __name__ == "__main__":
    d = D()
    d.bar()
