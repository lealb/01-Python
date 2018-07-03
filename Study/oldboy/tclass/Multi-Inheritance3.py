# -*- coding: utf-8 -*-
# Author:leali
# Description: Py3的多继承
# Version:v1.0
# Date:5/21/2018-11:09 AM


class A(object):
    def go(self):
        print("Go A")

    def stop(self):
        print("Stop A")

    def pause(self):
        print("Not Implemented")


class B(A):
    def go(self):
        # super(B, self).go()
        print("Go B")


class C(A):
    def go(self):
        super(C, self).go()
        print("Go C")

    def stop(self):
        super(C, self).stop()
        print("Stop C")


class D(B, C):
    def go(self):
        super(D, self).go()
        print("Go D")

    def stop(self):
        super(D, self).stop()
        print("Stop D")

    def pause(self):
        print("Wait D")


class E(B, C):
    pass


if __name__ == "__main__":
    a = A()
    b = B()
    c = C()
    d = D()
    e = E()

    # 说明下列代码的输出结果

    a.go()
    print("*"*10)
    b.go()
    print("*"*10)
    c.go()
    print("*"*10)
    d.go()
    print("*"*10)
    e.go()
    print("*"*10)

    a.stop()
    print("*"*10)
    b.stop()
    print("*"*10)
    c.stop()
    print("*"*10)
    d.stop()
    print("*"*10)
    e.stop()
    print("*"*10)

    a.pause()
    print("*"*10)
    b.pause()
    print("*"*10)
    c.pause()
    print("*"*10)
    d.pause()
    print("*"*10)
    e.pause()
    print(D.mro())
