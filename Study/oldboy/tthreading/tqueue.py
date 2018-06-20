# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:2018-06-19-04:37 PM
import threading
import queue
from time import sleep
from random import randint


class Production(threading.Thread):
    def run(self):
        while True:
            r = randint(0, 100)
            q.put(r)
            print("生产出来%s号包子" % r)
            sleep(1)


class Process(threading.Thread):
    def run(self):
        while True:
            re = q.get()
            print("吃掉%s号包子" % re)


if __name__ == "__main__":
    q = queue.Queue(3)
    threads = [Production(), Production(), Process()]
    for t in threads:
        t.start()
