# -*- coding: utf-8 -*-
# Description: html 下载
# 17-3-31:下午2:32
import urllib


class HtmlDownloader(object):
    def download(self, url):
        if url is not None:
            try:
                # 超时异常处理 10s
                request = urllib.request.urlopen(url, timeout=10)
                if request.getcode() == 200:
                    return request.read()
                else:
                    return None
            except Exception as e:
                print(str(e))
        else:
            return None
