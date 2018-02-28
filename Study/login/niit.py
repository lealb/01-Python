# -*- coding: utf-8 -*-

# @Author: Leal
# @File: niit.py
# @Time: 2017/11/24 15:26
# @Description: 模拟登陆NIIT

import requests
import http.cookiejar
from bs4 import BeautifulSoup
import time


class NIIT(object):
    def __init__(self):
        """
        :param session: 创建全局的session对象，保证会话的一致性，有效性。
        :param headers: 防止服务器端反爬虫，添加伪装头部信息
        """
        self.headers = {
            'User-Agent':  # {
                'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
            #  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
            # }

        }
        self.session = requests.Session()
        self.session.cookies = http.cookiejar.LWPCookieJar(filename='NIITCookies')
        self.home_url = "http://www.training-china.com/index.html"
        self.user_url = "http://www.training-china.com/setting/basic"
        self.loginurl = 'http://www.training-china.com/loginvalidate.html'
        try:
            # 加载Cookies文件
            self.session.cookies.load(ignore_discard=True)
        except IOError:
            print('Cookie not load！')

    def login(self, username, password):
        """
        login 自动登陆送积分
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

    def follow(self):
        start = time.clock()
        # 10000-77200 目前
        """关注好友挣积分
        优化 声明多个线程，分割多段进行提交
        """
        for i in range(13300, 77200):
            follow_url = "http://www.training-china.com/notice/" + str(i) + "/unfollow.html?notice_IsFaculty=1"
            # notice/76941/follow.html?notice_IsFaculty=0
            res = self.session.get(follow_url, headers=self.headers)

        end = time.clock()
        print("Return:", res.text)
        print("Run Time: %s Seconds" % (end - start))

    def video(self):
        """
        course/index25/22/151/finish.html
        index57/143 3704-3724
        index25/22 150-156
        index25/21 80-99
        index19/23 232-298
        index52/30 761-856
        index47/29 733-760
        kafka index3/7 151-161
        hadoop 编程 index3/17 37-79
        使用Sqoop 进行数据交换 index3/9 142-145
        hbase 企业应用程序开发 index/18 100-141
        :return:
        """
        # video_list=["index25",]
        course_id = "index52/30/"
        for i in range(761, 900):
            video_url = "http://www.training-china.com/course/" + course_id + str(i) + "/finish.html"
            # time.sleep(10)
            res = self.session.get(video_url, headers=self.headers)
        print(res.text)

    def addGroup(self):
        """
        加入学团送积分
        :return:
        """
        pass

    def article(self):

        for i in range(16, 21):
            article_url = "http://www.training-china.com/kn/contents/article" + str(i) + ".html"
            res = self.session.get(article_url, headers=self.headers)
        print(res.text)


if __name__ == '__main__':
    niit = NIIT()
    if niit.isLogin():
        print("Login:")
        print(niit.session.get(niit.user_url, headers=niit.headers).text)
    else:
        username = input("UserName:")
        password = input("Password:")
        niit.login(username, password)
    print("Login UserName:", niit.getUserInfo())
    niit.video()
    # niit.article()
    # niit.follow()
