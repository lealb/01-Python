# -*- coding: utf-8 -*-
# Description: 一般函数
# 2018/3/21 14:17


def show_shopping_car():
    saving = 1000000
    shopping_car = [
        ('Mac', 9000),
        ('Kindle', 800),
        ('Tesla', 700000),
        ('Python', 105)
    ]

    print("Shopping".center(50, '*'))
    for i, v in enumerate(shopping_car, 1):
        print('\033[35;1m %s: %s\033[0m' % (i, v))

    expense = 0
    for i in shopping_car:
        expense += i[1]
    print('\033[35;1m %s\033[0m' % (saving - expense))


def add(*tuples):
    """
    Variable-length argument
    存放未命名的变量参数
    :param tuples:
    :return:
    """
    sum = 0
    for v in tuples:
        sum += v
    return sum


def print_info1(**kwargs):
    """
    存放命名的变量参数
    :param kwargs:
    :return:
    """
    print(kwargs)
    for i in kwargs:
        print('%s:%s' % (i, kwargs[i]))
    return


def print_info2(name, *args, **kwargs):
    # def print_info1(name, **kwargs,*args): error
    print('Name:%s' % name)
    print('Args:%s' % args)
    print('Kwargs:%s' % kwargs)


def f1(*args):
    print('f-args:%s', args)


def f2(**kwargs):
    print('f-kwargs:%s' % kwargs)


def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


def factorial_new(n):
    """
    负数没有阶乘
    0的阶乘是1
    :param n:
    :return:
    """
    if n < 0:
        return -1
    if n <= 1:
        return 1
    return n * factorial_new(n - 1)


def fibo(n):
    before = 0
    after = 1
    for i in range(n - 1):
        result = before + after
        before = after
        after = result
    return result


def fibo_new(n):
    """
    默认的最大的递归深度为989
    :param n:
    :return:
    """
    if n <= 1:
        return n
    return fibo_new(n - 1) + fibo_new(n - 2)


if __name__ == '__main__':
    # show_shopping_car()
    print(add(1, 2, 3, 4))
    print(add(1, 2, 3))
    print_info1(name='alex', sex='man', hobby='boy')
    print_info2('alex', 18, hobby='girl', nationality='China')
    f1(*[1, 2, 5])
    f2(**{'name': 'alex'})
    print(factorial(5))
    print(factorial_new(5))
    print(fibo(10), end=" ")
    print(fibo_new(10))
