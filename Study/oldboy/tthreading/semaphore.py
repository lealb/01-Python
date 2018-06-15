# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:2018-06-14-01:40 PM
import threading
import time


class TestThread(threading.Thread):
    """
     信号量用来控制线程并发数的，
     BoundedSemaphore或Semaphore管理一个内置的计数 器，每当调用acquire()时-1，调用release()时+1
    """
    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(1)
            semaphore.release()


if __name__ == "__main__":
    semaphore = threading.Semaphore(5)
    threads = []
    for i in range(23):
        threads.append(TestThread())
    for t in threads:
        t.start()
