# -*- coding: utf-8 -*-
# Author:leali
# Description: 多态性
# Version:v1.0
# Date:5/21/2018-11:27 AM

class F(object):
    def show(self):
        print("F.show")


class S1(F):
    def show(self):
        print("S1.show")


class S2(F):
    def show(self):
        print("S2.show")


def Func(obj):
    obj.show()


if __name__ == "__main__":
    f = F()
    s1 = S1()
    s2 = S2()
    Func(f)
    Func(s1)
    Func(s2)
