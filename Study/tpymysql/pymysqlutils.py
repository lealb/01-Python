# -*- coding: utf-8 -*-
# Description:
# 17-4-1:上午12:42
from tpymysql import tinsert, tcount, tselect, tupdate, tdelete


class PyMysqlUtils:
    def __init__(self, db, tablename, query):
        self.insert = tinsert.Insert(db, tablename)
        self.count = tcount.Count(db, tablename, query)
        self.select = tselect.Select(db, tablename, query)
        self.update = tupdate.Update(db, tablename, query)
        self.delete = tdelete.Delete(db, tablename, query)
