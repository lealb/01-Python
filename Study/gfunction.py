# -*- coding: utf-8 -*-

# 高阶函数 map
def format_name(s):
    # 1.return s[0].upper()+s[1:].lower()
    # 2.return s.capitalize()
    return s.title()


print(map(format_name, ['adam', 'lisa', 'bart']));
# py 3
print(list(map(format_name, ['adam', 'lisa', 'bart'])));


def f(x):
    return x * x


print(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# 为什么打印的是内存地址？
# reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值
from functools import reduce


def prod(x, y):
    return x * y


print(reduce(prod, [2, 4, 5, 7, 12]))


# filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，
# 返回 true或 false，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list
def is_odd(x):
    return x % 2 == 1


print(list(filter(is_odd, [1, 4, 2, 546, 5, 768, 4, 2, 6, 3, 8])))


# 删除None或空字符
def is_not_empty(s):
    return s and len(s.strip()) > 0


print(list(filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])))
# s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。
# 当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')
import math


def is_sqr(x):
    r = int(math.sqrt(x))
    return r * r == x
    # return math.sqrt(x) % 1 == 0
    # return math.sqrt(x).is_integer()


print(list(filter(is_sqr, range(1, 101))))


# 传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0


# py3 error
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case))
# return cmp(s1.lower(),s2.lower())
# py 3 2
a = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(a, key=str.lower))


# Python的函数不但可以返回int、str、list、dict等数据类型，还可以返回函数
def calc_prod(lst):
    def a():
        return reduce((lambda x, y: x * y), lst)

    return a
    # def lazy_prod():
    #     def f(x, y):
    #         return x * y
    #     return reduce(f, lst, 1)
    # return lazy_prod


f = calc_prod([1, 2, 3, 4])
print(f())


# 闭包 内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数
def count():
    fs = []
    for i in range(1, 4):
        def f(m=i):
            return m * m

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())
# 因为函数只在执行时才去获取外层参数i，
# 若函数定义时可以获取到i，问题便可解决。而默认参数正好可以完成定义时获取i值且运行函数时无需参数输入的功能

# 关键字lambda 表示匿名函数，冒号前面的 x 表示函数参数。
print(list(filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])))


# 好玩的语法糖 装饰器
# 内置的装饰器有三个，分别是staticmethod、classmethod和property，作用分别是把类中定义的实例方法变成静态方法、类方法和类属性
def new_fn(f):
    def fn(x):
        print('call' + f.__name__ + '()')
        return f(x)

    return fn


@new_fn
def f1(x):
    return x * 2


g1 = new_fn(f1)
print(g1(5))
print(f1(2))

# 通用参数的 耗时装饰器 无参
import time, functools


def performance1(f):
    # 这两个是python中的可变参数。*args表示任何多个无名参数，
    # 它是一个tuple；**kwargs表示关键字参数，它是一个dict。
    # 并且同时使用*args和**kwargs时，必须*args参数列要在**kwargs前
    def fn(*args, **kwargs):
        t1 = time.time()
        t2 = time.time()
        print('call %s() in %fs' % (f.__name__, (t2 - t1)))
        return f(*args, **kwargs)

    return fn


@performance1
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(10))


# 有参 decorator
def performance(unit):
    def perf_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            # print('[%s] %s()...' % (prefix, f.__name__))
            t1 = time.time()
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print('call %s() in %f%s' % (f.__name__, t, unit))
            return f(*args, **kw)

        return wrapper

    return perf_decorator


@performance("ms")
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(10))


# @decorator可以动态实现函数功能的增加，
# decorator还改变了函数的__doc__等其它属性。
# 如果要让调用者看不出一个函数经过了@decorator的“改造”，就需要把原函数的一些属性复制到新函数中：
def f1():
    pass


print(f1.__name__)
print(factorial.__name__)

# 偏函数
print(int('1001010', 2))
int2 = functools.partial(int, base=2)  # 二进制转换
print(int2('10101010'))
# sorted_ignore_case = functools.partial(sorted, cmp=lambda s1, s2: cmp(s1.upper(), s2.upper()))
sorted_ignore_case = functools.partial(sorted, key=str.lower)
print(sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit']))

# 包和模块
# 当新版本的一个特性与旧版本不兼容时，该特性将会在旧版本中添加到__future__中，以便旧的代码能在旧版本中测试新特性。
