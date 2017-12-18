# -*- coding: utf-8 -*-
# Description: 测试线程
# 4/9/17:10:06 PM

import threading
import time


class TestThread(object):
    def __init__(self, num, total):
        self.num = num
        self.total = total

    def get_range(self):
        ranges = []
        offset = int(self.total / self.num)
        for i in range(self.num):
            if i == self.num - 1:
                ranges.append((i * offset, self.total))
            else:
                ranges.append((i * offset, (i + 1) * offset))
        return ranges

    def printNum(self, start, end):
        for i in range(start, end):
            print(i, end=",")
        print()

    def run(self):
        startTime = time.time()
        thread_list = []
        n = 0
        for ran in self.get_range():
            start, end = ran
            print('thread %d start:%s,end:%s' % (n, start, end))
            n += 1
            thread = threading.Thread(self.printNum(start, end))
            thread.start()
            thread_list.append(thread)
        for i in thread_list:
            i.join()
        print("Muti-Thread Time:ms %f" % (time.time() - startTime))


if __name__ == "__main__":
    myThread = TestThread(100, 50000)
    myThread.run()
    t1 = time.time()
    myThread.printNum(0, 50000)
    print("Non-Thread Time:ms %f" % (time.time() - t1))
