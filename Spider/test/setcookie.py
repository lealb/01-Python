# -*- coding: utf-8 -*-
# Description:
# 4/17/17:3:33 PM
from urllib import request
import http.cookiejar

# 创建MozillaCookieJar实例对象
cookie = http.cookiejar.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# 创建请求的request
req = request.Request("http://www.baidu.com")
# 利用urllib2的build_opener方法创建一个opener
opener = request.build_opener(request.HTTPCookieProcessor(cookie))
response = opener.open(req)
print(response.read())

