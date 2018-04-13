# -*- coding: utf-8 -*-
# Author:leali
# Description: 序列化与反序列化,还可自定义对象进行处理，未完成
# Version:v1.0
# Date:4/13/2018-10:35 AM
import json
import pickle
import time
import random
import os

LENGTH = 1024 * 10240


def test_pickle():
    """
    dumps 将数据通过特殊的形式转换为只有py语言识别的字符串
    loads 解析特殊字符串
    dump/load 转换/解析 操作文件
    参数说明：对象持久化
    obj: 要持久化保存的对象；
    file: 一个拥有 write() 方法的对象，并且这个 write() 方法能接收一个字符串作为参数。
    这个对象可以是一个以写模式打开的文件对象或者一个 StringIO 对象，或者其他自定义的满足条件的对象。
    protocol: 这是一个可选的参数，默认为 0 ，如果设置为 1 或 True，
    则以高压缩的二进制格式保存持久化后的对象，否则以ASCII格式保存
    :return:
    """
    data = {"k1": 123, "k2": "hello"}
    after = pickle.dumps(data)
    print(after)
    with open("pickle.pk", 'wb') as file:
        # 转换并写入文件
        pickle.dump(data, file)

    with open("pickle.pk", "rb") as file:
        res = pickle.load(file)
        print(res)


def test_cpickle():
    d = {}
    a = []
    for i in range(LENGTH):
        a.append(random.randint(0, 255))

    d["a"] = a

    print("dumping...")

    t1 = time.time()
    pickle.dump(d, open("tmp1.dat", "wb"), True)
    print("pickle-dump-True: %.3fs" % (time.time() - t1))

    t1 = time.time()
    pickle.dump(d, open("tmp2.dat", "wb"))
    print("pickle-dump-False: %.3fs" % (time.time() - t1))

    t1 = time.time()
    json.dump(d, open("tmp3.dat", "w"))
    print("json-dump: %.3fs" % (time.time() - t1))

    s1 = os.stat("tmp1.dat").st_size
    s2 = os.stat("tmp2.dat").st_size
    s3 = os.stat("tmp3.dat").st_size

    print("%d, %d, %.2f%%" % (s1, s2, 100.0 * s1 / s2))
    print("%d, %d, %.2f%%" % (s1, s3, 100.0 * s1 / s3))

    print("loading...")

    t1 = time.time()
    with open("tmp1.dat", "rb") as obj1:
        pickle.load(obj1)
    print("pickle-load-True: %.3fs" % (time.time() - t1))

    t1 = time.time()
    with open("tmp2.dat", "rb") as obj2:
        pickle.load(obj2)
    print("pickle-load-False: %.3fs" % (time.time() - t1))
    t1 = time.time()
    with open("tmp3.dat", "rb") as obj3:
        json.load(obj3)
    print("json-load-True: %.3fs" % (time.time() - t1))


if __name__ == "__main__":
    """
    性能比较：
    json，序列化和解析用时长，但压缩率为pickle的40%
    pickle，时间短
    需要与外部系统交互时用json模块；
    需要将少量、简单Python数据持久化到本地磁盘文件时可以考虑用pickle模块；
    需要将大量Python数据持久化到本地磁盘文件或需要一些简单的类似数据库的增删改查功能时，可以考虑用shelve模块
    """
    # test_pickle()
    test_cpickle()
