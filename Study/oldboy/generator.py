# -*- coding: utf-8 -*-
# Description: 
# 2018/3/21 17:09
import time


def fibo(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b, end=',')
        a, b = b, a + b
        n += 1
    return 'done'


def fibo_generator(n):
    n, a, b = 0, 0, 1
    while n < n:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


def consumer(name):
    print('%s Ready eat big' % name)
    while True:
        big = yield
        print("Big %s generator, Eat by %s!" % (big, name))


def produce(name):
    c1 = consumer('A')
    c2 = consumer('B')
    next(c1)
    next(c2)
    print('%s Ready make big!!' % name)
    for i in range(10):
        time.sleep(1)
        print('Get two bigs')
        c1.send(i)
        c2.send(i + 1)


if __name__ == '__main__':
    # fibo(10)
    fg = fibo_generator(10)
    # next(fg)
    produce('Leal')
    while True:
        try:
            x = next(fg)
            print(x, end=',')
        except StopIteration as ex:
            print('Generator return value:', ex.value)
            break
