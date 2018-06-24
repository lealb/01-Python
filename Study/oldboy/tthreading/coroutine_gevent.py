# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:2018-06-24-03:28 PM
from greenlet import greenlet
import gevent
from urllib.request import urlopen
import time
from gevent import monkey


monkey.patch_all()


# def test1():
#     print(1)
#     gre2.switch()
#     print(2)
#
#
# def test2():
#     print(3)
#     gre1.switch()
#     print(4)


def get_page(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))
    with open("test.html", "wb") as f:
        f.write(data)


def get_time(f):
    def swapper(urls):
        start = time.time()
        result = f(urls)
        end = time.time()
        print("Speed %s s" % (end - start))
        return result

    return swapper


@get_time
def test_for(urls):
    for url in urls:
        get_page(url)


@get_time
def test_gevent(urls):
    jobs = [gevent.spawn(get_page, url) for url in urls]
    gevent.joinall(jobs, timeout=5)


if __name__ == "__main__":
    """
    greenlet 切换对象
    """
    # gre1 = greenlet(test1)
    # print(gre1)
    # gre2 = greenlet(test2)
    # gre2.switch()
    urls = ["https://www.python.org/", "https://www.yahoo.com/", "https://github.com/"]
    test_for(urls)
    test_gevent(urls)
