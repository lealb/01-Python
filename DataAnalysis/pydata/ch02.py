# -*- coding: utf-8 -*-
# Author:leali
# Description: pydata 2nd
# Version:v1.0
# Date:2018-07-05-02:56 PM


import os
import json

BASE_PATH = "D:\\04-Documents\\pydata\\ch02"


def format_load(path):
    """
    format load file by path
    :param path:user-defined path
    :return: formatted data
    """
    with open(path) as file:
        try:
            records = [json.loads(line) for line in file]
        except Exception as ex:
            print("Load Excption:", ex)
    return records


def get_counts(sequence):
    """
    standard python
    :param sequence:
    :return:
    """
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


def get_count2(sequence):
    from collections import defaultdict
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts


def top_counts(count_dict, n=10):
    """
    get top n by count dict
    :param count_dict:
    :param n:
    :return:
    """
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]


def cost_time(func):
    """
    cost time
    :param func:
    :return:
    """
    from time import time
    def warpper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print("Speed %s" % (end - start))
        return result

    return warpper


@cost_time
def get_top_time_zones1(data, n=10):
    """
    way 1
    :param n:
    :return:
    """
    time_zones = [rec['tz'] for rec in records if 'tz' in rec]
    # print(time_zones[:10])
    # print(data[0])
    counts = get_counts(time_zones)
    top = top_counts(counts, n)
    top2 = sorted(counts.items(), key=lambda d: d[1], reverse=True)[:n]
    top3 = sorted(counts.items(), key=lambda d: d[1])[-n:]
    # print(counts)
    print(top2)


@cost_time
def get_top_time_zones2(data, n=10):
    """
    way 2 by Counter
    :param n:
    :return:
    """
    from collections import Counter
    time_zones = [rec['tz'] for rec in data if 'tz' in rec]
    counts = Counter(time_zones)
    print(counts.most_common(n))


@cost_time
def get_top_time_zones3(data, n=10):
    from pandas import DataFrame, Series
    from matplotlib import pyplot as plt
    import pandas as pd
    import numpy as np
    import pylab
    # 初始化一些参数
    # initiation some parameters
    plt.rc('figure', figsize=(10, 6))
    np.set_printoptions(precision=4)
    frame = DataFrame(data)
    # data_frame[data_frame['tz'] == ''] = "Unknown"
    top = frame["tz"].value_counts()[:10]
    print(top)
    # missing value handling
    # fillna 查一下直接复制与fillna的区别
    clean_tz = frame['tz'].fillna('Missing')
    clean_tz[clean_tz == ''] = "Unknown"
    clean_tz_counts = clean_tz.value_counts()
    print(clean_tz_counts[:10])
    # draw by plot,can't get image
    # 为什么不能画图
    plt.figure(figsize=(10, 4))
    clean_tz_counts[:10].plot(kind='barh', rot=0)
    pylab.show()
    # Series
    results = Series([x.split()[0] for x in frame.a.dropna()])
    print(results[:5])
    results_counts = results.value_counts()
    print(results_counts[:8])

    # group
    cframe = frame[frame.a.notnull()]
    operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
    print(operating_system[:5])
    # group sum
    by_tz_os = cframe.groupby(['tz', operating_system])
    agg_counts = by_tz_os.size().unstack().fillna(0)
    print(agg_counts[:10])
    # Use to sort in ascending order
    indexer = agg_counts.sum(1).argsort()
    print(indexer[:10])
    count_subset = agg_counts.take(indexer)[-10:]
    print(count_subset)

    # draw
    plt.figure()
    count_subset.plot(kind='barh', stacked=True)
    plt.figure()
    normed_subset = count_subset.div(count_subset.sum(1), axis=0)
    print(normed_subset)
    normed_subset.plot(kind='barh', stacked=True)


if __name__ == "__main__":
    path = os.path.join(BASE_PATH, "usagov_bitly_data2012-03-16-1331923249.txt")

    records = format_load(path)
    # get time zones
    # get_top_time_zones1(records)
    # get_top_time_zones2(records)
    get_top_time_zones3(records)
