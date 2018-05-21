# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:5/21/2018-1:37 PM


class Pager:

    def __init__(self, current_page):
        # 用户当前请求的页码（第一页、第二页...）
        self.current_page = current_page
        # 每页默认显示10条数据
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val


if __name__ == "__main__":
    page = input("Please input page:")
    try:
        p = Pager(int(page))
        print("Output:%s-%s" % (p.start, p.end))
    except Exception as ex:
        print(ex)
