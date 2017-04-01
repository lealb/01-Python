# -*- coding: utf-8 -*-
# Description:
# git clone https://github.com/PyMySQL/PyMySQL
# cd PyMySQL/
# python3 setup.py install
# 需要安装 sudo apt-get install python3-setuptools
# 测试mysql
# 17-3-31:下午10:00
from tpymysql import connect


if __name__ == "__main__":
    try:
        connect.Connect("127.0.0.1", "test", "leal", "lidan")
    except Exception as e:
        print("Connect Filed", e)


