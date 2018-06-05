# -*- coding: utf-8 -*-
# Author:leali
# Description: 模块学习-random
# Version:v1.0
# 2018/3/23 16:05

import random


def set_random_seed(seed):
    random.seed(seed)


def random_num():
    """
    random.random 用于随机生成0-1.0的随机浮点数
    random.uniform(a, b)，用于生成一个指定范围内的随机符点数
    :return:
    """
    print(random.random())
    print(random.uniform(10, 20))
    print(random.uniform(20, 10))


def get_random_num(minnum, maxnum, number):
    """
    random.randint(a, b)，用于生成一个指定范围内的整数
    :param minnum: 下限
    :param maxnum: 上限
    :param number: 个数
    :return: 排序后的列表
    """
    num = []
    for i in range(0, number):
        num.append(random.randint(minnum, maxnum))
    print(list(sorted(num)))


def get_random_choice():
    """
    random.randrange([start], stop[, step])，从指定范围内，按指定基数递增的集合中 获取一个随机数
    random.choice(sequence)。参数sequence表示一个有序类型
    random.shuffle(x[, random])，用于将一个列表中的元素打乱
    random.sample(sequence, k)，从指定序列中随机获取指定长度的片断 与R的sample相同
    :return:
    """
    print(random.randrange(10, 100, 2))
    print(random.choice(range(10, 100, 2)))
    be_list = ["Python", "is", "powerful", "simple", "and so on..."]
    random.shuffle(be_list)
    print(list(be_list))
    # 从list中随机获取5个元素，作为一个片断返回
    print(random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))


if __name__ == '__main__':
    # get_random_num(1, 10, 10)
    # random_num()
    get_random_choice()
