from urllib import request
import http.cookiejar

url = "https://www.imooc.com"
# 第一种 直接请求
print("直接请求")
resp = request.urlopen(url)
# 状态码
print(resp.getcode())
# 读取内容
content = resp.read()
print(len(content))

# 第二种 添加 data 、http header
print("添加对象")
resq = request.Request(url)  # 创建对象
# resq.data('java')
resq.add_header('User-Agent', 'Mozilla/5.0')
resp = request.urlopen(resq)
print(resp.getcode)
print(len(content))

# 第三种
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
resp = request.urlopen(url)
print(resp.getcode())
print(cj)
# print(resp.read())
