# -*- coding: utf-8 -*-
# Description: 
# 2017/11/24 16:06

import requests
from bs4 import BeautifulSoup
# 这个函数使用来提取流水号的
def toJson(str):
    '''
    提取lt流水号，将数据化为一个字典
    '''
    soup = bs(str)
    tt = {}
    # 提取form表单中所有的input标签，以字典的形式来保存name：value
    for inp in soup.form.find_all('input'):
        if inp.get('name') != None:
            tt[inp.get('name')] =inp.get('value')
    return tt

# 这行代码，是用来维持cookie的，你后续的操作都不用担心cookie，他会自动带上相应的cookie
s = requests.Session()
# 我们需要带表单的参数,这里面有个参数lt,登录操作的流水号，我们需要从html页面中进行提取
payload ={'username':'jackroyal','password':'123456','lt':soup["lt"],'execution':'e1s1','_eventId':'submit'}
r = s.post("http://passport.csdn.net/account/login",data=payload,headers=header)
print (r.text)

