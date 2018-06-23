# -*- coding: utf-8 -*-
# Author:leali
# Description: 讨论共享信息的q同一个还是copy一份的，目前看来id是不一样的
# copy,通过pickle序列化和反序列化拿到
# Version:v1.0
# Date:2018-06-20-02:21 PM

from multiprocessing import Process, Queue, Pipe, Manager
import os
import time
import random


# 写数据进程执行的代码
def write(q):
    print("Process to write: %s,ID=%s" % (os.getpid(), id(q)))
    for value in ['A', 'B', 'C']:
        print("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())
    q.put(12233)


# 读数据进程执行的代码
def read(q):
    print("Process to read: %s,ID=%s" % (os.getpid(), id(q)))
    while True:
        value = q.get()
        print("Get %s from queue." % value)


def test_queue():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入：
    pw.start()
    # 启动子进程pr，读取：
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程里的死循环，无法等待结束，只能强制终止
    pr.terminate()


def pipe_send(conn, message):
    conn.send(message)
    conn.close()


def test_pipe():
    """
    考虑实际用处呢？
    :return:
    """
    parent_conn, child_conn = Pipe()
    message = input("Input Message:")
    p = Process(target=pipe_send, args=(child_conn, message,))
    p.start()
    print(parent_conn.recv())
    p.join()


def t_manager(d, l, n):
    d[n] = n
    d['sdf'] = 234
    l.append(n)
    # print(l)


def test_manager():
    """
    数据共享
    :return:
    """
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(2))
        p_list = []
        for i in range(10):
            p = Process(target=t_manager, args=(d, l, i,))
            p.start()
            # 把进程对象加入列表
            p_list.append(p)
        for j in p_list:
            j.join()
        print(d)
        print(l)


if __name__ == '__main__':
    # 父进程创建Queue,并传给各个子进程
    # 类似于socket通信，主进程和子进程互相传递消息
    """
    在Unix/Linux下，可以使用fork()调用实现多进程。
    要实现跨平台的多进程，可以使用multiprocessing模块。
    进程间通信是通过Queue、Pipes等实现的
    """
    # test_queue()
    # test_pipe()
    test_manager()