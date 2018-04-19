# -*- coding: utf-8 -*-
# Author:leali
# Description:  线程测试
# Version:v1.0
# Date:4/19/2018-2:32 PM

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        time.sleep(3)
        print("Thread Name:", self.getName())
        global x

        lock.acquire()
        for i in range(3):
            x += 1
        time.sleep(1)
        print(x)
        lock.release()

    def fun1(self):
        self.start()
        # self.join()  # join() 会使当前线程执行
        print("fun1 done")

    def fun2(self):
        self.start()
        # self.join()  # join() 会使当前线程执行
        print("fun2 done")


if __name__ == "__main__":
    # t1 = MyThread('A')
    # t2 = MyThread('B')
    # t2.setDaemon(True) # 强制杀死子线程,设置为TRUE 不会执行子线程，如果加join
    # t1.fun1()
    # t2.fun2()
    lock = threading.RLock()
    t1 = []
    for i in range(10):
        t1.append(MyThread(str(i)))
    x = 0
    for i in t1:
        i.start()
