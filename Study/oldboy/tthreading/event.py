# -*- coding: utf-8 -*-
# Author:leali
# Description: 同步条件，与条件变量类似，只是少了锁
# Version:v1.0
# Date:2018-06-19-03:49 PM

import threading
import time


class Boss(threading.Thread):
    """
    event.isSet()：返回event的状态值；
    event.wait()：如果 event.isSet()==False将阻塞线程；
    event.set()： 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
    event.clear()：恢复event的状态值为False。
    """

    def run(self):
        print("BOSS：今晚大家都要加班到22:00。")
        print("isSet:", event.isSet())
        event.isSet() or event.set()
        time.sleep(3)
        print("BOSS：<22:00>可以下班了。")
        event.isSet() or event.set()


class Worker(threading.Thread):
    def run(self):
        # 等待同步条件的线程结束，即再次激活
        event.wait()
        print("Worker：哎……命苦啊！")
        time.sleep(0.25)
        event.clear()
        event.wait()
        print("Worker：OhYeah!")


if __name__ == "__main__":
    event = threading.Event()
    threads = []
    for i in range(5):
        threads.append(Worker())
    threads.append(Boss())
    for t in threads:
        t.start()
    for t in threads:
        t.join()
