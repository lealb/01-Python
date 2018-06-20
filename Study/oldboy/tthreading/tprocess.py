# -*- coding: utf-8 -*-
# Author:leali
# Description: fork 创造进程
# Version:v1.0
# Date:2018-06-20-01:48 PM
import os
import time
import random
from multiprocessing import Process, Pool
import subprocess


def test_fork():
    print('Process (%s) start...' % os.getpid())
    # Only works on Unix/Linux/Mac:
    pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


def run_proc(name):
    """
    fork by multiprocessing
    :param name:
    :return:
    """
    print('Run child process %s (%s)' % (name, os.getpid()))


def long_time_task(name):
    """
    进程池的方式批量创建子进程
    :param name:
    :return:
    """
    print("Run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s run %0.f seconds." % (name, (end - start)))


def test_subprocess1():
    print("$ nslookup www.yangcongchufang.com")
    r = subprocess.call(['nslookup', 'www.yangcongchufang.com'])
    print("Exit code: ", r)


def test_subprocess():
    print("$ nslookup")
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b"set q=mx\nyangcongchufang.com\nexit\n")
    print(output.decode("utf-8"))
    print("Exit code:", p.returncode)


if __name__ == "__main__":
    # print('Parent process %s.' % os.getpid())
    # p = Process(target=run_proc, args=('test_code',))
    # print('Child process will start.')
    # p.start()
    # p.join()
    # print('Child process end.')
    print("Parent process %s." % os.getpid())
    # Pool的默认大小是CPU的核数
    # task0，1，2，3是立刻执行的，而task4要等待前面某个task完成后才执行，
    # 这是因为Pool的默认大小设置成了4(p = Pool(4))，代表着最多同时执行4个进程
    # p = Pool(4)
    # for i in range(5):
    #     p.apply_async(long_time_task, args=(i,))
    # print("Waiting for all subprocess done...")
    # p.close()  # 不能继续添加新的Process
    # p.join()
    # print("All subprocess done.")
    test_subprocess1()
