# -*- coding: utf-8 -*-
# Author:leali
# Description: 常用模块学习-time
# Version:v1.0
# 2018/3/23 14:19
import time
from datetime import datetime
from datetime import date
from datetime import timedelta
import random


def test():
    """
    测试相关方法
    :return:
    """
    # %a %b %d %H:%M:%S %Y
    print(time.asctime())  # Fri Mar 23 14:31:00 2018
    print(time.ctime())  # Fri Mar 23 14:35:25 2018
    # time.struct_time(tm_year=2018, tm_mon=3, tm_mday=23, tm_hour=14, tm_min=31,
    # tm_sec=46, tm_wday=4, tm_yday=82, tm_isdst=0)
    print(time.localtime())
    print(time.strptime("20180323142923", "%Y%m%d%H%M%S"))  # str->struct_time
    print(time.mktime(time.localtime()))  # struct_time->timestamp
    print(time.gmtime(time.time() - 86640))  # utc timestamp->struct_time
    print(time.strftime("%Y%m%d%H%M%S", time.gmtime()))  # utc timestamp->str

    # datetime

    print(datetime.now())  # 2018-03-23 15:16:41.015798
    print(date.fromtimestamp(time.time()))  # timestamp->datetime 2018-03-23
    # 获取指定时间
    print(datetime.now() + timedelta(1))  # 明天
    print(datetime.now() + timedelta(-1))  # 前一天
    print(datetime.now() + timedelta(hours=1))
    print(datetime.now() + timedelta(minutes=10))
    # 时间替换
    print(datetime.now().replace(minute=3, hour=2))


def get_order_num():
    """
    获得订单号，一般订单流水号号是当前时间+6位流水号
    :return:
    """
    # %f ms
    timestamp = time.strftime("%Y%m%d%H%M%S", time.gmtime())
    num = random.randint(100000, 999999)
    return "".join((timestamp, str(num)))


if __name__ == '__main__':
    # test()
    print(get_order_num())
