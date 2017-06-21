# -*- coding: utf-8 -*-
# Description:关于字符串
# 2017/6/21:3:22
import re, os

# 4.1 如何拆分含有多种分隔符的字符串
# 方法1 依次分割
def mySplit(s, ds):
    res = [s]
    for d in ds:
        t = []
        list(map(lambda x: t.extend(x.split(d)), res))
        res = t
    return [x for x in res if x]


# 方法2 正则表达式 推荐
def testRe(s, ds):
    import re
    return re.split(r'[' + ds + ']+', s)


# 4.2 如何判断字符池a是否是以字符串b开头或结尾
# 字符串end/startwith方法
# 多个匹配使用元组
def testEnd():
    s = "123@45.com"
    print(s.endswith('.com'))
    print(s.startswith('11'))


# 示例 给指定目录的.py .sh文件给用户赋予以执行权限 Linux
def chmodToFile(path):  # 程序未验证
    import os, stat
    # 获得指定目录下的文件
    getfile = [name for name in os.listdir(path) if name.endwith(('.py', '.sh'))]
    # 权限赋值
    for file in getfile:
        # oct(os.stat(file).st_mode) # 查看权限
        os.chmod(file, os.stat(file).st_mode | stat.S_IXUSR)


# 通过正则表达式元组 把日期yyyy-mm-dd 转换为mm/dd/yyyy
# 可加强正则表达式的用法
def testFile():
    path = ""
    log = os.read(path)
    re.sub('(\d{4}-\d{2}-\d{2})', r'\2/\3/\1', log)


# 4.4 小字符串拼接
# 方法1 字符串对象不停建立释放 浪费内存
def testAddStr(str):
    # + __add__
    astr = " "
    for s in str:
        astr += s
    return astr


def testPart():
    str1 = ['we', 'wer', 'wer', 'sdfg']
    print(testAddStr(str1))
    # 方法2 使用内置join方法
    print(';'.join(str1))
    print(''.join(str1))
    str2 = ['we', 132, 3454, 'sdfg']
    # print(''.join(str1)) # error
    print(''.join(str(r) for r in str2))


# 4.5 字符串对齐
def testJust():
    # 字符串just center对齐函数
    a = 23
    print(str(a).ljust(4, '0'))
    print(str(a).rjust(4, '0'))
    print(str(a).center(4, '0'))


def testFormat():
    # format < > ^
    a = 23
    print(format(str(a), '<4'))
    print(format(str(a), '>4'))
    print(format(str(a), '^4'))


# 示例
def testDict():
    dict1 = {
        'WErtete': 2535,
        'FGHer': 32,
        'SDFertwet': 256
    }

    # 获取最宽的字符串长度 key 对齐
    w = max(map(len, dict1.keys()))
    for k in dict1:
        print(k.ljust(w), ':', dict1[k])


# 去掉不需要的空白
# 1. 内置函数Strip 只能删除两端
def testStrip1():
    s = '  er  df  '
    print(s.strip())
    print(s.lstrip())
    print(s.rstrip())


# 2.切片+ 拼接 任意
def testStrip2():
    s = '123:werwer'
    print(s[:3] + s[4:])


# 3 replace 正则表达式
def testStrip3():
    s = '234\twerrw\tfssdf\n\wer\rwe'
    print(s.replace('\t', ''))
    import re
    print(re.sub('[\t\n\r]', '', s))


# 4 translate
def testTranslate():
    # 可用于加密
    import string
    s = 'abc5436346xyz'
    print(s.maketrans('abcxyz', 'xyzabc'))


if __name__ == "__main__":
    str = 'ab;cd|efg|hi,,jkl|mn\topq;rst,uvw\tsyz'
    print(mySplit(str, ';|,\t'))

    print(testRe(str, ';|,\t'))
