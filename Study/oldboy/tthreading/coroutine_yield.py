# -*- coding: utf-8 -*-
# Author:leali
# Description: yield The lowest level of the implementation of Coroutine
# Version:v1.0
# Date:2018-06-24-03:15 PM


def customer(name):
    """
    Generator by yield
    yield 能保持上下文
    :return:
    """
    print("Customer Start:")
    while True:
        result = yield
        print("%s Eating %s " % (name, result))


def producer(conn):
    """
    next get generator
    :return:
    """
    next(conn)
    i = 0
    print("Producer Start:")
    while i < 5:
        print("Making ", i)
        conn.send(i)
        i += 1


if __name__ == "__main__":
    c1 = customer("Leal")
    # c2 = customer("Jane")
    producer(c1)
    # producer(c2)
