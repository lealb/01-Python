# -*- coding: utf-8 -*-
# Description:
# 4/17/17:3:32 PM

from urllib import request
import http.cookiejar

# 设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
# 声明一个CookieJar对象实例来保存cookie
cookie = http.cookiejar.CookieJar()

# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = http.cookiejar.MozillaCookieJar(filename)

# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)

# 通过handler来构建opener
opener = request.build_opener(handler)
# 此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print('Name = ' + item.name)
    print('Value = ' + item.value)

# 保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)
