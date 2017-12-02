# -*- coding: utf-8 -*-
# Description: 测试线程
# 4/9/17:10:06 PM

# # 为线程定义一个函数
# def print_time( threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
#
# # 创建两个线程
# try:
#     _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#     _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#     print ("Error: 无法启动线程")
#
# while 1:
#     pass

import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    for i in range(13300*(step+1))


for i in range(1, 11):
    myThread(i, "Thread" + str(i), i).start()
    time.sleep(1)
for i in range(1,11):
    myThread(i, "Thread" + str(i), i).join()
print("退出主线程")
