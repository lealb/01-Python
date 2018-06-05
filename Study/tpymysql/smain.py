# -*- coding: utf-8 -*-
# Description:
# git clone https://github.com/PyMySQL/PyMySQL
# cd PyMySQL/
# python3 setup.py install
# 需要安装 sudo apt-get install python3-setuptools
# 测试mysql
# 17-3-31:下午10:00
from tpymysql import tconnect, tcount

"""
使用mysql样本数据测试：
http://downloads.mysql.com/docs/sakila-db.tar.gz
1.安装通过source 安装导入sakila-schema.sql和sakila-data.sql文件
"""

if __name__ == "__main__":
    try:
        tconnect.Connect(user="root", password="leal520")
        print(tcount.Count("zhaopin", "jobszhi")())
    except Exception as e:
        print("Connect Filed", e)
