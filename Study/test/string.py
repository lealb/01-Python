# -*- coding: utf-8 -*-
# Description: 测试py3的字符串函数
# 17-4-5:下午2:49
str = """
测试字符串函数功能\n
"""
print(str)
tstr = "this is a test str"
print(tstr.capitalize())  # 转换字符串首字符
print('1'.center(3, '0'))  # 填充居中指定长度的字符串，默认为"" 010
# count(str, beg= 0,end=len(string))
# 字符解码
# bytes.decode(encoding="utf-8", errors="strict")
# encode(encoding='UTF-8',errors='strict') 以 encoding 指定的编码格式编码字符串
# endswith(suffix, beg=0, end=len(string)) 检查字符串是否以 obj 结束
"""
expandtabs(tabsize=8)把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 
http://www.runoob.com/python3
列表
元组
字典
"""

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b
