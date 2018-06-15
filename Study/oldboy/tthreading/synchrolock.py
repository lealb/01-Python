# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:2018-06-13-08:15 PM

import time
import threading

num = 100  # 设定一个共享变量
thread_list = []

# 使用同步锁解决
lock = threading.Lock()


def add_num():
    global num  # 在每个线程中都获取这个全局变量
    # num-=1
    lock.acquire()
    temp = num
    # print('--get num:', num)
    time.sleep(0.00001)
    num = temp - 1  # 对此公共变量进行-1操作
    lock.release()


def test1():
    for i in range(100):
        t = threading.Thread(target=add_num)
        t.start()
        # join 可以解决，但用join呗，join会把整个线程给停住，
        # 造成了串行，失去了多线程的意义，而我们只需要把计算(涉及到操作公共数据)的时候串行执行
        # t.join()
        thread_list.append(t)

    for t in thread_list:  # 等待所有线程执行完毕
        t.join()

    print('final num:', num)


if __name__ == "__main__":
    test1()
