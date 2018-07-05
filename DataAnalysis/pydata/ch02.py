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


def get_count(sequence):
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


if __name__ == "__main__":
    path = os.path.join(BASE_PATH, "usagov_bitly_data2012-03-16-1331923249.txt")

    records = format_load(path)
    # get time zones
    time_zones = [rec['tz'] for rec in records if 'tz' in rec]
    print(time_zones[:10])
    print(records[0])
    counts = get_count(time_zones)
    top = top_counts(counts)
    print(top)
