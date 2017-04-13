# -*- coding: utf-8 -*-
# Description:
# 17-4-1:上午12:42
from tpymysql import insert, count, select, update, delete


class PyMysqlUtils:
    def __init__(self, db, tablename, query):
        self.insert = insert.Insert(db, tablename)
        self.count = count.Count(db, tablename, query)
        self.select = select.Select(db, tablename, query)
        self.update = update.Update(db, tablename, query)
        self.delete = delete.Delete(db, tablename, query)
