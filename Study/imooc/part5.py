# -*- coding: utf-8 -*-
# Description: 关于文件
# 2017/6/21:22:46

# 5.1 如何读写文件
# py2 中需要f.write(s.encode('utf8))/f.read().decode('utf8 )
# py3 会自动编码
def writeFile(filename, s):
    try:
        f = open(filename, 'w', encoding='utf8')
        f.write(s)
    except:
        FileExistsError
    finally:
        f.close()


def readFile(filename):
    try:
        f = open(filename, 'r', encoding='utf8')

        print(f.read())
    except:
        FileExistsError
    finally:
        f.close()


# 5.2 如何处理二进制文件
# 5.3 如何设置文件缓冲
def setBuffer(filename, s, bufsize):
    # 全缓冲 buffering >1的整数n n为缓冲大小
    # 行缓冲 1
    # 无缓冲 0
    try:
        f = open(filename, 'w', encoding='utf8', buffering=bufsize)
        f.write(s)
    except:
        Exception
    finally:
        f.close()


# 5.4 如何将文件映射到内存
# 使用标准库中mmap
# 5.5 如何访问文件状态
# 1 系统调用 os 模块下调用stat  fstat lstat获取文件状态 2 快捷函数 标准库中os.path下的一些函数
def getFileState(filename):
    import os, stat
    # 文件类型
    print(os.stat(filename))
    print(stat.S_ISDIR(os.stat(filename).st_mode))  # 文件夹
    print(os.path.isdir(filename))
    print(stat.S_ISREG(os.stat(filename).st_mode))  # 普通文件
    # 权限
    print(os.stat(filename).st_mode & stat.S_IRUSR)  # 有值即有权限
    # 文件时间
    print(os.stat(filename).st_atime)  # 最后操作时间
    print(os.path.getatime(filename))
    import time
    print(time.localtime(os.stat(filename).st_atime))
    # 文件大小
    print(os.stat(filename).st_size)
    print(os.path.getsize(filename))


# 如何使用临时文件
def useTemFile(s):
    # 使用标准库中temfile
    from tempfile import TemporaryFile, NamedTemporaryFile
    try:
        f = TemporaryFile()
        f1 = NamedTemporaryFile()

        f1.name = "df"
        f.write(s)
    except:
        Exception
    finally:
        f.close()  # 临时文件关闭会自动删除


if __name__ == "__main__":
    filename = "py3.txt"
    s = "你好"
    # writeFile(filename, s)
    # readFile(filename)
    # setBuffer(filename, s * 100, 2048)
    # readFile(filename)
    getFileState(filename)
