# -*- coding: utf-8 -*-
# Author:leali
# Description: 测试mysql的中文
# Version:v1.0
# Date:5/22/2018-1:55 PM

import  pymysql
if __name__ == "__main__":
    # 打开数据库连接
    db = pymysql.connect("127.0.0.1", "leal", "lidan", "test")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
qsql = "SELECT * FROM py_employee \
       WHERE income > '%d'" % (1000)

try:
    # 执行查询SQL语句
    cursor.execute(qsql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
               (fname, lname, age, sex, income ))
except:
    # 如果发生错误则回滚
    db.rollback()
finally:
    db.close()
