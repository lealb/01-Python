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


if __name__ == "__main__":
    filename = "py3.txt"
    s = "你好"
    writeFile(filename, s)
    readFile(filename)
