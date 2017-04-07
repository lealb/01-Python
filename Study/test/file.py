# -*- coding: utf-8 -*-
# Description: 文件的操作
# 4/6/17:4:14 PM
import pprint
import os
import pickle

if not os.path.exists("../../res/test.txt"):
    # 创建文件
    os.mknod("../../res/test.txt")
try:
    # 打开一个文件
    f = open("../../res/test.txt", "w")
    f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
    f = open("../../res/test.txt", "r")
    # print(f.read()) 读取文件内容，size 默认或者为负数读取全部文件
    # print(f.readline()) 读取一行 忽略\n
    print(f.readlines())  # 返回该文件中包含的所有行
except OSError as err:
    print("OS error: {0}".format(err))
finally:
    # 关闭打开的文件
    f.close() # 可使用with
"""
python的pickle模块实现了基本的数据序列和反序列化。
通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象
pickle.dump(obj, file, [,protocol])
"""

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4 + 6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output = open('../../res/data.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(data1, output)
# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

# 读取
# 使用pickle模块从文件中重构python对象
pkl_file = open('../../res/data.pkl', 'rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)
data2 = pickle.load(pkl_file)
pprint.pprint(data2)
output.close()
