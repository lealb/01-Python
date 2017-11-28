# -*- coding: utf-8 -*-

# @Author: Leal
# @File: niit.py
# @Time: 2017/11/24 15:26
# @Description: 模拟登陆NIIT

import requests
import http.cookiejar
from bs4 import BeautifulSoup


class NIIT(object):
    def __init__(self):
        """
        :param session: 创建全局的session对象，保证会话的一致性，有效性。
        :param headers: 防止服务器端反爬虫，添加伪装头部信息
        """
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }
        self.session = requests.Session()
        self.session.cookies = http.cookiejar.LWPCookieJar(filename='NIITCookies')
        self.home_url="http://www.training-china.com/index.html"
        self.user_url = "http://www.training-china.com/setting/basic"
        self.loginurl = 'http://www.training-china.com/loginvalidate.html'
        try:
            # 加载Cookies文件
            self.session.cookies.load(ignore_discard=True)
        except IOError:
            print('Cookie not load！')

    def login(self, username, password):
        """
        login
        :param username:
        :param password:
        :return:
        """
        # post form data
        data = {
            "login_username": username,
            "login_password": password,
            "rememberMe": "on",
            "from": self.home_url,
        }
        # if cookie file is not exists, login
        response = self.session.post(url=self.loginurl, data=data, headers=self.headers)
        # print(response.content.decode("utf-8"))
        if niit.isLogin():
            print('Success！')
            self.session.cookies.save()
        else:
            print(response.content)

    def isLogin(self):
        """
        通过查看用户个人信息来判断是否已经登录
        禁止重定向，否则登录失败重定向到首页也是响应200
        :param url: 需要登陆的固定url
        :return: 是否登陆bool值
        """
        login_code = self.session.get(self.user_url, headers=self.headers, allow_redirects=False).status_code
        if login_code == 200:
            return True
        else:
            return False

    def getUserInfo(self):
        self.session.cookies.load(ignore_discard=True)
        soup = BeautifulSoup(self.session.get(self.user_url, headers=self.headers).text, "lxml")
        return soup.find("div", {"class": "control-text"}).string


if __name__ == '__main__':
    niit = NIIT()
    if niit.isLogin():
        print("Need Login:")
        print(niit.session.get(niit.user_url, headers=niit.headers).text)
    else:
        niit.login('yingjiang.li@esgyn.cn', '61NIIT!')
    print("Login UserName:", niit.getUserInfo())
