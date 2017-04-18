# -*- coding: utf-8 -*-
# Description: 模拟登录淘宝类
# 4/17/17:5:08 PM

from taobao import tool
from urllib import request, parse
import http.cookiejar
import re
import webbrowser

class Taobao:
    # 初始化方法
    def __init__(self):
        # 登录的URL
        self.loginURL = "https://login.taobao.com/member/login.jhtml"
        # 代理IP地址，防止自己的IP被封禁
        self.proxyURL = 'http://120.193.146.97:843'
        # 登录POST数据时发送的头部信息
        self.loginHeaders = {
            'Host': 'login.taobao.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
            'Referer': 'https://login.taobao.com/member/login.jhtml',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'Keep-Alive'
        }
        # 用户名
        self.username = 'Àî¼Î¶«ÔÀ'
        # ua字符串，经过淘宝ua算法计算得出，包含了时间戳,浏览器,屏幕分辨率,随机数,鼠标移动,鼠标点击,其实还有键盘输入记录,鼠标移动的记录、点击的记录等等的信息
        self.ua='090#qCQX4TXdXsvXITi0XXXXXQk63ofYH97cfD47O6GX+EdIBoY7hE9sZbsp3ou1Z9mczbkkO+gOAG1qDuLCsPRc+t8YxzUYTiYiXiGOACVRBL/2IYPmQCp7tkBaYO5R9GRyqw3+C1TiXivMSMbEIrKgDtlPsfYjq2SsvoOs/jxiXXfUZ8wl5XQXiH/gMWywdmxiXXfUZ8wl5XQXiH/NMWyuxaxiXXfUZ8wl5XQX/rEgMWygASKfWvjy6jPwdgyrOmlg2TQXunmt2C9U4DLbTGON/9aBaZHmCxzbT9YyDEZS+XQXadFD1vpbXXL/mG4iXXtgyXDr0TX2iTGJXvX3lI/VXlTXi4K1QgSkKuSZQXQX6//oeGCnWHOZ0wWplzQ7ehs9BE2vOfr+qfVdkKqnL4nOQ83fyflT9h15vszxqTQXiP+0gzvgXvXnSb+2C4V3SZANRhEmr4ESmyd9ebP3ryBGSb+cLTV3SxqNRhEmr4ESTnYiXXjMclAno1RrwmXiXXFUliQzLggfXvravMmMcm73kML4RUUjzZRDMfyJEJStM16EFfu5k5SN8cJkqE0jzZRDMfyJSH03S17Tqza5ksg3wclkP9KuN47ge5DwTMKtFEg5IosZisDdT3DkWMFg8CWSAmx5BsxNiYWxIHiZTm73kML4KEPrkWFg12K4/XqE8Lu2U5oZCgWMwcysP00u/NbuEXDcB9g3E1o7PjZfInENyhBZLBfg/lRL9uK4X7PpAemURoHgCNEyccE5LX3jrtN2Mt/ZlJqsdLFbL2GvXvXpx761+QTQzmXHm0zEqN9QXvXuTPu2AQIj3XQXiPR22amJXvXqysBnXYJXi4xG+XQXadFSqX3gXXL/9jxiXXfUZ8wlHXQXuKuBIzN/HC4AoYIGuGznh6+4T8QpEphchpmxXvXD3yWEMDK8S8qEa6DhPjByFDOo6BxRXvX0HUrY7xtiBoRawW6mnqQ6036/k3Rr+HSzbKgxXvXD3yFEMgBoS8qEa6DhPjByFDOo6BxRXvX0HULKuQNiBoRa4FpocAYDvhrqthGtsfKr9VL='
        # 密码，在这里不能输入真实密码，淘宝对此密码进行了加密处理，256位，此处为加密后的密码
        self.password2='508d1c9fb7a4f238c081de8431da078f5da906c827e3d811d2542c8707365d7ef0395f84ebc2872d9888a328564d8628e206d448e0d64e40cfb6596d7d9de0b5b07e3e9062976c8175129ce2af443cf342640a32c9992f94fc09d36bdfe02a3c0264232655ba5dde754ae334d58fbdd69d0dd8aa9db498a001e3b2f0b78a3293'
        self.post = {
            'ua': self.ua,
            'TPL_checkcode': '',
            'CtrlVersion': '1,0,0,7',
            'TPL_password': '',
            'TPL_redirect_url': 'https://i.taobao.com/my_taobao.htm?nekot=wO68zrar1MA=1492421015138',
            'TPL_username': self.username,
            'loginsite': '0',
            'newlogin': '0',
            'from': 'tb',
            'fc': 'default',
            'style': 'default',
            'css_style': '',
            'tid': 'XOR_1_000000000000000000000000000000_625C4720470A0A050976770A',
            'support': '000001',
            'loginType': '4',
            'minititle': '',
            'minipara': '',
            'umto': 'NaN',
            'pstrong': '3',
            'llnick': '',
            'sign': '',
            'need_sign': '',
            'isIgnore': '',
            'full_redirect': '',
            'popid': '',
            'callback': '',
            'guf': '',
            'not_duplite_str': '',
            'need_user_id': '',
            'poy': '',
            'gvfdcname': '10',
            'gvfdcre': '',
            'from_encoding ': '',
            'sub': '',
            'TPL_password_2': self.password2,
            'loginASR': '1',
            'loginASRSuc': '1',
            'allp': '',
            'oslanguage': 'zh-CN',
            'sr': '1366*768',
            'osVer': 'windows|6.1',
            'naviVer': 'firefox|35'
        }
        # 将POST的数据进行编码转换
        self.postData = parse.urlencode(self.post)
        print(self.postData)
        # 设置代理
        self.proxy = request.ProxyHandler({'http': self.proxyURL})
        # 设置cookie
        self.cookie = http.cookiejar.LWPCookieJar()
        # 设置cookie处理器
        self.cookieHandler = request.HTTPCookieProcessor(self.cookie)
        # 设置登录时用到的opener，它的open方法相当于urllib2.urlopen
        self.opener = request.build_opener(self.cookieHandler, self.proxy, request.HTTPHandler)
        # 赋值J_HToken
        self.J_HToken = ''
        # 登录成功时，需要的Cookie
        self.newCookie = http.cookiejar.CookieJar()
        # 登陆成功时，需要的一个新的opener
        self.newOpener = request.build_opener(request.HTTPCookieProcessor(self.newCookie))
        # 引入工具类
        self.tool = tool.Tool()

    # 得到是否需要输入验证码，这次请求的相应有时会不同，有时需要验证有时不需要
    def needCheckCode(self):
        # 第一次登录获取验证码尝试，构建request
        req = request.Request(self.loginURL, self.postData, self.loginHeaders)
        # 得到第一次登录尝试的相应
        response = self.opener.open(req)
        # 获取其中的内容
        content = response.read().decode('gbk')
        # 获取状态吗
        status = response.getcode()
        # 状态码为200，获取成功
        if status == 200:
            print("获取请求成功")
            # \u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801这六个字是请输入验证码的utf-8编码
            pattern = re.compile(u'\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801', re.S)
            result = re.search(pattern, content)
            # 如果找到该字符，代表需要输入验证码
            if result:
                print("此次安全验证异常，您需要输入验证码")
                return content
            # 否则不需要
            else:
                # 返回结果直接带有J_HToken字样，表明直接验证通过
                tokenPattern = re.compile('id="J_HToken" value="(.*?)"')
                tokenMatch = re.search(tokenPattern, content)
                if tokenMatch:
                    self.J_HToken = tokenMatch.group(1)
                    print("此次安全验证通过，您这次不需要输入验证码")
                    return False
        else:
            print("获取请求失败")
            return None

    # 得到验证码图片
    def getCheckCode(self, page):
        # 得到验证码的图片
        pattern = re.compile('<img id="J_StandardCode_m.*?data-src="(.*?)"', re.S)
        # 匹配的结果
        matchResult = re.search(pattern, page)
        # 已经匹配得到内容，并且验证码图片链接不为空
        if matchResult and matchResult.group(1):
            return matchResult.group(1)
        else:
            print("没有找到验证码内容")
            return False

    # 输入验证码，重新请求，如果验证成功，则返回J_HToken
    def loginWithCheckCode(self):
        # 提示用户输入验证码
        checkcode = input('请输入验证码:')
        # 将验证码重新添加到post的数据中
        self.post['TPL_checkcode'] = checkcode
        # 对post数据重新进行编码
        self.postData = parse.urlencode(self.post)
        try:
            # 再次构建请求，加入验证码之后的第二次登录尝试
            req = request.Request(self.loginURL, self.postData, self.loginHeaders)
            # 得到第一次登录尝试的相应
            response = self.opener.open(req)
            # 获取其中的内容
            content = response.read().decode('gbk')
            # 检测验证码错误的正则表达式，\u9a8c\u8bc1\u7801\u9519\u8bef 是验证码错误五个字的编码
            pattern = re.compile(u'\u9a8c\u8bc1\u7801\u9519\u8bef', re.S)
            result = re.search(pattern, content)
            # 如果返回页面包括了，验证码错误五个字
            if result:
                print("验证码输入错误")
                return False
            else:
                # 返回结果直接带有J_HToken字样，说明验证码输入成功，成功跳转到了获取HToken的界面
                tokenPattern = re.compile('id="J_HToken" value="(.*?)"')
                tokenMatch = re.search(tokenPattern, content)
                # 如果匹配成功，找到了J_HToken
                if tokenMatch:
                    print("验证码输入正确")
                    self.J_HToken = tokenMatch.group(1)
                    return tokenMatch.group(1)
                else:
                    # 匹配失败，J_Token获取失败
                    print("J_Token获取失败")
                    return False
        except request.HTTPError as e:
            print("连接服务器出错，错误原因", e.reason)
            return False

    # 通过token获得st
    def getSTbyToken(self, token):
        tokenURL = 'https://passport.alipay.com/mini_apply_st.js?site=0&token=%s&callback=stCallback6' % token
        req = request.Request(tokenURL)
        response = request.urlopen(req)
        # 处理st，获得用户淘宝主页的登录地址
        pattern = re.compile('{"st":"(.*?)"}', re.S)
        result = re.search(pattern, response.read())
        # 如果成功匹配
        if result:
            print("成功获取st码")
            # 获取st的值
            st = result.group(1)
            return st
        else:
            print("未匹配到st")
            return False

    # 利用st码进行登录,获取重定向网址
    def loginByST(self, st, username):
        stURL = 'https://login.taobao.com/member/vst.htm?st=%s&TPL_username=%s' % (st, username)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
            'Host': 'login.taobao.com',
            'Connection': 'Keep-Alive'
        }
        req = request.Request(stURL, headers=headers)
        response = self.newOpener.open(req)
        content = response.read().decode('gbk')
        # 检测结果，看是否登录成功
        pattern = re.compile('top.location = "(.*?)"', re.S)
        match = re.search(pattern, content)
        if match:
            print("登录网址成功")
            location = match.group(1)
            return True
        else:
            print("登录失败")
            return False

    # 获得已买到的宝贝页面
    def getGoodsPage(self, pageIndex):
        goodsURL = 'http://buyer.trade.taobao.com/trade/itemlist/listBoughtItems.htm?action=itemlist/QueryAction&event_submit_do_query=1' + '&pageNum=' + str(
            pageIndex)
        response = self.newOpener.open(goodsURL)
        page = response.read().decode('gbk')
        return page

    # 获取所有已买到的宝贝信息
    def getAllGoods(self, pageNum):
        print("获取到的商品列表如下")
        for x in range(1, int(pageNum) + 1):
            page = self.getGoodsPage(x)
            self.tool.getGoodsInfo(page)

    # 程序运行主干
    def start(self):
        # 是否需要验证码，是则得到页面内容，不是则返回False
        needResult = self.needCheckCode()
        # 请求获取失败，得到的结果是None
        if not needResult == None:
            if not needResult == False:
                print("您需要手动输入验证码")
                checkCode = self.getCheckCode(needResult)
                # 得到了验证码的链接
                if not checkCode == False:
                    print("验证码获取成功")
                    print("请在浏览器中输入您看到的验证码")
                    webbrowser.open_new_tab(checkCode)
                    self.loginWithCheckCode()
                # 验证码链接为空，无效验证码
                else:
                    print("验证码获取失败，请重试")
            else:
                print("不需要输入验证码")
        else:
            print("请求登录页面失败，无法确认是否需要验证码")

        # 判断token是否正常获取到
        if not self.J_HToken:
            print("获取Token失败，请重试")
            return
        # 获取st码
        st = self.getSTbyToken(self.J_HToken)
        # 利用st进行登录
        result = self.loginByST(st, self.username)
        if result:
            # 获得所有宝贝的页面
            page = self.getGoodsPage(1)
            pageNum = self.tool.getPageNum(page)
            self.getAllGoods(pageNum)
        else:
            print("登录失败")
