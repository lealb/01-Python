# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:4/13/2018-9:04 AM

import sys


def test_exit():
    """
    控制程序退出，正常退出为0
    :return:
    """
    try:
        sys.exit(1)
    except SystemExit:
        print(SystemExit.code)
        sys.exit(0)


if __name__ == "__main__":
    # 命令行参数List，第一个元素是程序本身路径 实现程序外部向程序传递参数
    print(sys.argv)
    # test_exit()
    # 获取系统当前默认编码 py3默认为utf8，去除了setdefaultencoding 方法
    print(sys.getdefaultencoding())
    # 获取文件系统
    print(sys.getfilesystemencoding())
    # 返回模块搜索路径 可用于模块加载
    print(sys.path)
    # 返回操作系统平台名称 win32/win64 linux2
    print(sys.platform)

