# -*- coding: utf-8 -*-
# Description:
# 4/17/17:3:36 PM
from urllib import request, parse
import http.cookiejar

filename = 'mycrosecookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = http.cookiejar.MozillaCookieJar(filename)
opener = request.build_opener(request.HTTPCookieProcessor(cookie))
postdata = parse.urlencode({
    'userName': 'cse.yjli12',
    'passWord': '888888'
})
# 登录教务系统的URL
loginUrl = 'http://eol.gzu.edu.cn/eol/homepage/common/'
# 模拟登录，并把cookie保存到变量
result = opener.open(loginUrl, postdata.encode('utf-8'))
# 保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
# 利用cookie请求访问另一个网址，此网址是成绩查询网址
infoUrl = 'http://eol.gzu.edu.cn/eol/main.jsp'
# 请求访问成绩查询网址
result = opener.open(infoUrl)
print(result.read())
