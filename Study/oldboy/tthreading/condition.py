# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:2018-06-14-02:36 PM


import threading
import time
from random import randint


class Producer(threading.Thread):
    def run(self):
        global products
        while True:
            val = randint(0, 100)
            print('Producer-', self.name, ":Append-" + str(val), products)
            if lock_con.acquire():
                products.append(val)
                lock_con.notify()
                lock_con.release()
            time.sleep(3)


class Consumer(threading.Thread):
    def run(self):
        global products
        while True:
            lock_con.acquire()
            if len(products) == 0:
                lock_con.wait()
            print('Consumer-', self.name, ":Delete" + str(products[0]), products)
            del products[0]
            lock_con.release()
            time.sleep(0.25)


if __name__ == "__main__":
    """
    wait()：条件不满足时调用，线程会释放锁并进入等待阻塞；
    notify()：条件创造后调用，通知等待池激活一个线程；
    notifyAll()：条件创造后调用，通知等待池激活所有线程。
    """

    products = []
    lock_con = threading.Condition()
    threads = []
    for i in range(5):
        threads.append(Producer())
    threads.append(Consumer())
    for t in threads:
        t.start()
    for t in threads:
        t.join()
