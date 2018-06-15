# -*- coding: utf-8 -*-
# python 小程序示例
print(1)
# 1.计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和 循环 判断
sum = 0;
x = 1;
n = 1;
while True:
    sum += 2 ** (x - 1);
    n = n + 1;
    x = x + 1;
    if n > 20:
        break;
print(sum);

#######################################
print(2)
# 2.dict运用遍历
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
# 格式化输出
for key in ['Adam', 'Lisa', 'Bart']:
    print("%s: %d" % (key, d[key]))
# 输入
d = {
    'zhangsan': 99,
    'lisi': 88,
    'wangwu': 77,
}
grade = input("请输入分数:\n")
for i in d:
    if d[i] != grade:
        print("Not Find")
        break
    else:
        print(i)

#######################################
print(3)
# 3.set的运用
s = set([name.lower() for name in ['Adam', 'Lisa', 'Bart', 'Paul']])
print('adam' in s)
# set格式化输出
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    # print ("%s:%d")%x
    print(x[0], ':', x[1])

# set取其差集
s = set(['Adam', 'Lisa', 'Paul'])
products = ['Adam', 'Lisa', 'Bart', 'Paul']
m = set(products)
p = s - m
q = m - s
s = p | q
print(s)

#######################################
# 4.python函数
print(4)
print(sum([n ** 2 for n in range(1, 101)]))  # i*i equal i**2

# 1
products = []
x = 1
N = 100
while x <= N:
    products.append(x * x)
    x = x + 1
print(sum(products))


# 4.1递归函数-汉诺塔
# move(n, a, b, c)表示的是有n个盘子在a柱子上，将要移到c柱子上面去
def move(n, a, b, c):
    # 如果a柱子上面只有一个盘子，则直接移到c柱子上面去并输出路径，结束递归
    if n == 1:
        print(a, '-->', c)
        return
    # 表示的是将n-1的盘子从a柱子上面移到b柱子上面去
    move(n - 1, a, c, b)
    # 输出最下面个盘子移从a移到c的路径
    print(a, '-->', c)
    # move(1,a,b,c)
    # 将b柱子上面的n-1个盘子移动到c柱子上面
    move(n - 1, b, a, c)


move(4, 'A', 'B', 'C')


# power N次方
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


#######################################
# 5.切片字符串拼接
# 首字母大写，拼接+
def firstCharUpper(s):
    return s[0].upper() + s[1:]


print(firstCharUpper('hello'))

# 6迭代
for i in range(1, 101)[6::7]:
    print(i)
