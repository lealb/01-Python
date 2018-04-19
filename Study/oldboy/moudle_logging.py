# -*- coding: utf-8 -*-
# Author:leali
# Description: logging,需要用的时候可以引入高级操作（Logger,Handler,Formatter,Filter）
# Version:v1.0
# Date:4/19/2018-12:09 AM

import logging


def simple_test(file):
    """
    通过下面的方式进行简单配置输出方式与日志级别,默认日志追加模式
    :param file: 文件存储
    :return:
    """
    logging.basicConfig(filename=file, level=logging.INFO)

    logging.debug('debug message')
    logging.info('info message')
    logging.warn('warn message')
    logging.error('error message')
    logging.critical('critical message')


# logging:配置日志格式
def displaying_format_massages():
    '''
    format参数中可能用到的格式化串
    %(name)s Logger的名字
    %(levelno)s 数字形式的日志级别
    %(levelname)s 文本形式的日志级别
    %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
    %(filename)s 调用日志输出函数的模块的文件名
    %(module)s 调用日志输出函数的模块名
    %(funcName)s 调用日志输出函数的函数名
    %(lineno)d 调用日志输出函数的语句所在的代码行
    %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
    %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
    %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
    %(thread)d 线程ID。可能没有
    %(threadName)s 线程名。可能没有
    %(process)d 进程ID。可能没有
    %(message)s用户输出的消息
    '''

    # format：指定handler使用的日志显示格式。
    logging.basicConfig(format="%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s - %(message)s")
    logging.warning("warning")


# logging:配置日志时间格式
def displaying_date_message():
    # datefmt：指定日期时间格式,也就是“%(asctime)s”的格式
    logging.basicConfig(format="%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s - %(message)s",
                        datefmt="%Y-%m-%d %I:%M:%S %p")
    logging.warning("warning")


if __name__ == "__main__":
    file = "data/logger.log"
    # simple_test(file)
    displaying_format_massages()
    # displaying_date_message()