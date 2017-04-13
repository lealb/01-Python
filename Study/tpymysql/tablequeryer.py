# -*- coding: utf-8 -*-
# Description:
# 17-4-1:上午12:41
from tpymysql import select, insert, pymysqlutils, conds
from sqlite3 import OperationalError


class TableQueryer:
    '''
    Support for single table simple querys
    '''

    def __init__(self, db, tablename):
        self.tablename = tablename
        self.db = db

    def get_one(self, query):
        rs = select.Select(self.db, self.tablename, query)()
        if len(rs) > 0:
            if len(rs) > 1:
                print(OperationalError, "returned multi row when fetch one result")
            return rs[0]
        return None

    def insert(self, **fields):
        return insert.Insert(self.db, self.tablename)(**fields)

    def __call__(self, query=None):
        return pymysqlutils.PyMysqlUtils(self.db, self.tablename, query)

    def __getattr__(self, field_name):
        return conds.conds(field_name)
