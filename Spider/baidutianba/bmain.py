# -*- coding: utf-8 -*-
# Description: 测试主类
# 4/17/17:10:34 AM

from baidutianba import bdtb

if __name__ == "__main__":
    print("请输入帖子代号")
    baseNum = input();
    baseURL = 'http://tieba.baidu.com/p/' + str(baseNum)
    seeLZ = input("是否只获取楼主发言，是输入1，否输入0\n")
    floorTag = input("是否写入楼层信息，是输入1，否输入0\n")
    print(baseURL)
    bdtb = bdtb.BDTB(baseURL, seeLZ, floorTag)
    bdtb.start()
