# -*- coding: utf-8 -*-
# Author:leali
# Description: 简单线程测试
# Version:v1.0
# Date:2018-06-13-03:37 PM
import threading
import time


def watch_movie(name="肖申克的救赎", second=4):
    print("Start watch movie %s at %s" % (name, time.ctime()))
    time.sleep(second)
    print("End watch movie at ", time.ctime())


def listen_music(name="贝多芬的悲伤", second=2):
    print("Start listen music %s at %s" % (name, time.ctime()))
    time.sleep(second)
    print("End listen music at ", time.ctime())


def get_time(func):
    """
    计算运行时间装饰器
    :param func:
    :return:
    """

    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Spend:%s" % (end_time - start_time))

    return wrapper


@get_time
def single_thread():
    watch_movie()
    listen_music()


@get_time
def multi_thread():
    """
    坑：target赋值为方法名，不能加括号否则会变成串行执行的单线程状态
    :return:
    """
    t1 = threading.Thread(target=watch_movie)
    t2 = threading.Thread(target=listen_music)
    # 设置其守护线程，会忽视其执行
    # 给最后一个调用线程设置守护线程似乎没多少意义
    t2.setDaemon(True)

    t1.start()
    t2.start()


# 线程实现方式二
class TestThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print("Run Number:", self.num)


if __name__ == "__main__":
    # print("Single:")
    # single_thread()
    # print("Multi:")
    # multi_thread()
    t1 = TestThread(1)
    t2 = TestThread(2)
    t1.start()
    t2.start()

