# -*- coding: utf-8 -*-
# Author:leali
# Description: 几种常见的算法比较
# Version:v1.0
# Date:2018-07-11-10:29 AM
import random


def cost_time(f):
    """
    计算时间装饰器
    :param f:
    :return:
    """

    def warpper(*args, **kwargs):
        from time import time
        start = time()
        result = f(*args, **kwargs)

        end = time()
        print("Cost time：%s(s)" % (end - start))
        return result

    return warpper


@cost_time
def insert_sort(lists):
    """
    插入排序,O(n^2) 稳定
    默认选取list[1]作为待插值，依次与前面的 i-1个已排序的元素比较，寻找插入的位置
    :param lists:
    :return:
    """
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
        # print(i, lists)
    return lists


@cost_time
def shell_sort(lists):
    """
    希尔排序 非稳定
    缩小增量排序，改进的插入排序,step 的确定很重要，一般为len/10
    :param lists:
    :return:
    """
    count = len(lists)
    step = count // 10
    group = count // step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group //= step
    return lists


@cost_time
def bubble_sort(lists):
    """
    冒泡排序:O(n^2)
    :param lists:
    :return:
    """
    count = len(lists)
    for i in range(1, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


@cost_time
def quick_sort(lists, left, right):
    """
    快速排序
    :param lists:
    :param left:
    :param right:
    :return:
    """
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


@cost_time
def select_sort(lists):
    """
    选择排序
    :param lists:
    :return:
    """
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists


if __name__ == "__main__":
    lists = [random.randint(1, 10000) for i in range(0, 2000)]
    print(lists)
    lists_len = len(lists)
    print("Insert_Sort:" + str(insert_sort(lists)))
    print("Shell_Sort:" + str(shell_sort(lists)))
    print("Bubble_Sort：" + str(bubble_sort(lists)))
    # print("Quick_Sort:" + str(quick_sort(lists, 0, lists_len - 1)))
    print("Select_Sort:" + str(select_sort(lists)))
