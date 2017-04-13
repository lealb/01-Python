# -*- coding: utf-8 -*-
# Description: 数据结构
# 4/6/17:9:24 AM

a = [1, 4, -3, 45, 23, 67, 42, 456, 23, 45]
# list.append(x)	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]
a.append(-34)
a.insert(3, -54)
a.remove(67)
a.pop(2)
a.count(23)
a.sort()
print(a)
# 将列表当做堆栈使用
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

# 将列表当作队列使用
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry arrives
queue.append("Graham")  # Graham arrives
print(queue.popleft())

# 列表推导
vec1 = [2, -2, 3, 4, 6]
vec2 = [3, 1, 2, 5, 4]
print(list(x * y for x in vec1 for y in vec2 if x % 2 != 0 and y % 2 == 0))

# 嵌套列表解析
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12, 13]
]
# 行列转置
m1 = [[row[i] for row in matrix] for i in range(4)]
m2 = []
for i in range(4):
    m2.append([row[i] for row in matrix])

# the following 3 lines implement the nested listcomp
m3 = []
for i in range(4):
    m3_row = []
    for row in matrix:
        m3_row.append(row[i])
    m3.append(m3_row)
print(m1)

print('23'.zfill(4))
