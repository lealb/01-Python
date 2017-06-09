# -*- coding: utf-8 -*-
# Description: 百度贴吧爬虫
# 4/17/17:10:31 AM
from baidutianba import tool
from urllib import request
import re

class BDTB:
    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self, baseUrl, seeLZ = 0, floorTag = 1):
        # base链接地址
        self.baseURL = baseUrl
        # 是否只看楼主
        if seeLZ is not 0:
            self.seeLZ = '?see_lz=' + str(seeLZ)
        # HTML标签剔除工具类对象
        self.tool = tool.Tool()
        # 全局file变量，文件写入操作对象
        self.file = None
        # 楼层标号，初始为1
        self.floor = 1
        # 默认的标题，如果没有成功获取到标题的话则会用这个标题
        self.defaultTitle = "百度贴吧"
        # 是否写入楼分隔符的标记
        self.floorTag = floorTag

    # 传入页码，获取该页帖子的代码
    def getPage(self, pageNum):
        try:
            # 构建URL
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            req = request.Request(url)
            response = request.urlopen(req)
            # 返回UTF-8格式编码内容
            return response.read().decode('utf-8')
        # 无法连接，报错
        except request.URLError as e:
            if hasattr(e, "reason"):
                print("连接百度贴吧失败,错误原因", e.reason)
                return None

    def getTitle(self, page):
        # 得到标题的正则表达式
        pattern = re.compile(r'<h(\d)(\W)+class="core_title_txt.*>(.*)</h\1>')
        result = re.search(pattern, page)
        if result:
            # 如果存在，则返回标题
            result = result.group(0)
            pattern2 = r'(?<=>)(.*)(?=</h\d>)'
            result2 = re.search(pattern2, result).group(0).strip()
            # bs4.BeautifulSoup(matched_result, 'html.parser').text.strip()
            print(result2)
            return result2
        else:
            return None

    # 获取帖子一共有多少页
    def getPageNum(self, page):
        # 获取帖子页数的正则表达式
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span class="red">(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            print(result.group(1).strip()) # 打印测试
            return result.group(1).strip()
        else:
            return None

    # 获取每一层楼的内容,传入页面内容
    def getContent(self, page):
        # 匹配所有楼层的内容
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            # 将文本进行去除标签处理，同时在前后加入换行符
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode('utf-8'))
        return contents

    # 写入数据
    def writeData(self, contents):
        # 向文件写入每一楼的信息
        for item in contents:
            # print(item.decode())
            if self.floorTag == '1':
                # 楼之间的分隔符
                floorLine = "\n" + str(self.floor) + u"----------------------------------\n"
                self.file.write(floorLine)
            self.file.write(item.decode())
            self.floor += 1

    # 开始
    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        # 如果标题不是为None，即成功获取到标题
        if title is None:
            title = self.defaultTitle
        self.file = open(title + ".txt", "w+")
        if pageNum == None:
            print("URL已失效，请重试")
            return
        try:
            print("该帖子共有" + str(pageNum) + "页")
            for i in range(1, int(pageNum) + 1):
                print("正在写入第" + str(i) + "页数据")
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        # 出现写入异常
        except IOError as e:
            print("写入异常，原因" + e.message)
        finally:
            self.file.close()
            print("写入任务完成")
