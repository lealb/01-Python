# -*- coding: utf-8 -*-
# Description: python 实例
# 4/9/17:9:42 PM
import cmath,random

num = int(input("请输入一个数字: "))
# num_sqrt = num ** 0.5
num_sqrt = cmath.sqrt(num)
if num_sqrt.imag != 0:
    print('{0} 的平方根为 {1:0.3f}+{2:0.3f}i'.format(num, num_sqrt.real, num_sqrt.imag))
else:
    print('{0} 的平方根为 {1:0.3f}'.format(num, num_sqrt.real))

print(random.randint(1,100)) # 随机生成1-100的随机数
