# -*- coding: utf-8 -*-
# Description:
# 2017/11/27 17:46

import requests
import http.cookiejar
from subprocess import Popen
import time
import json
from bs4 import BeautifulSoup


class Zhihu(object):
    TYPE_PHONE_NUM = "phone_num"
    TYPE_EMAIL = "email"

    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                                      '(KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
                        "Host": "www.zhihu.com",
                        "Referer": "https://www.zhihu.com/",
                        }
        # 建立一个会话，可以把同一用户的不同请求联系起来；直到会话结束都会自动处理cookies
        self.session = requests.Session()
        # 建立LWPCookieJar实例，可以存Set-Cookie3类型的文件。
        self.session.cookies = http.cookiejar.LWPCookieJar("ZhihuCookie")
        self.home_url = "https://www.zhihu.com"
        self.user_url = "https://www.zhihu.com/settings/profile"
        try:
            self.session.cookies.load(ignore_discard=True)
        except IOError:
            print('Cookie not load！')

    def get_xsrf(self):
        """
        获取参数_xsrf
        """
        soup = BeautifulSoup(self.session.get(self.home_url, headers=self.headers).text, "lxml")
        _xsrf = soup.find("input", {"name": "_xsrf"})["value"]
        return _xsrf

    def get_captcha(self):
        """
        获取验证码本地显示,可以尝试自动图片识别
        返回你输入的验证码
        """
        # 添加时间戳避免验证码失效问题
        captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + str(int(time.time() * 1000)) + "&type=login"
        response = self.session.get(captcha_url, headers=self.headers)
        with open('captcha.gif', 'wb') as f:
            f.write(response.content)
        # Pillow显示验证码
        Popen('captcha.gif', shell=True)
        captcha = input('This time need input captcha： ')
        return captcha

    def login(self, username, password):
        """
        输入自己的账号密码，模拟登录知乎
        """
        login_url = 'https://www.zhihu.com/login/' + self.getUsernameType(username)
        data = {'_xsrf': self.get_xsrf(),
                'password': password,
                'remember_me': 'true',
                self.getUsernameType(username): username
                }

        # 若不用验证码，直接登录
        result = self.session.post(login_url, data=data, headers=self.headers)
        # 打印返回的响应，r = 1代表响应失败，msg里是失败的原因
        # loads可以反序列化内置数据类型，而load可以从文件读取
        if (json.loads(result.text))["r"] == 1:
            data['captcha'] = self.get_captcha()
            result = self.session.post(login_url, data=data, headers=self.headers)
            print((json.loads(result.text))['msg'])
        # 保存cookie到本地
        self.session.cookies.save(ignore_discard=True, ignore_expires=True)

    def getUsernameType(self, username):
        """
        判断用户名类型
        经测试，网页的判断规则是纯数字为phone_num，其他为email
        检测到11位数字则是手机登录
        if re.match(r'\d{11}$', username):
        """
        if username.isdigit():
            return self.TYPE_PHONE_NUM
        return self.TYPE_EMAIL

    def isLogin(self):
        # 禁止重定向，否则登录失败重定向到首页也是响应200
        login_code = self.session.get(self.user_url, headers=self.headers, allow_redirects=False).status_code
        if login_code == 200:
            return True
        else:
            return False

    def getInfo(self):
        soup = BeautifulSoup(self.session.get(self.user_url, headers=self.headers).text, "lxml")
        username = soup.find("span", {"class": "name"}).string
        return username


if __name__ == '__main__':
    zhihu = Zhihu()
    if zhihu.isLogin():
        print('Login')
    else:
        username = input("UserName:")
        password = input("Password:")
        zhihu.login(username,password)
    print("Login UserName:", zhihu.getInfo())
