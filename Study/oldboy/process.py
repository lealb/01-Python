# -*- coding: utf-8 -*-
# Description: 进度条测试
# 2018/2/1 10:34
import sys, time

if __name__ == '__main__':
    for i in range(100):
        # sys.stdout.write("".join(["*", "%", str(i)]))
        # sys.stdout.flush()
        print("*", end="", flush=True)
        time.sleep(0.5)
