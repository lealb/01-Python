# -*- coding: utf-8 -*-
# Author:leali
# Description: 多继承，分新式类和经典类两种搜索方式
# Version:v1.0
# Date:5/21/2018-10:19 AM
class A():
    def bar(self):
        print "A.bar"

class B(A):
    def bar1(self):
        print "B.bar"

class C(A):
    def bar(self):
        print "C.bar"


class D(B, C):
    """
    经典类采取的为深度优先搜索D->B->A->C
    新式类采取的为广度优先搜索D->B->C->A
    在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
    """
    # def bar(self):
    #     print "D.bar"


if __name__ == "__main__":
    """
    对经典类来说，输出A.bar
    对新式类来说，输出C.bar
    在Py3中，全部要求为新式类
    """
    d = D()
    d.bar()
