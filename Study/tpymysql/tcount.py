# -*- coding: utf-8 -*-
# Description:
# 17-4-1:上午12:46
from tpymysql import tconnect
class Count(object):
    '''
    Count with current where clouse
    '''

    def __init__(self, db, tablename, where=None):
        self.db = db
        self.tablename = tablename
        self.where = where

    def __call__(self):
        if self.where is not None:
            _sql = "".join(["SELECT COUNT(1) FROM ", self.tablename, " WHERE ", self.where.get_sql()])
            _params = self.where.get_params()
            return self.db.count(_sql, *_params)
        else:
            _sql = "".join(["SELECT COUNT(1) FROM ", self.tablename])
            print(_sql)
            return self.db.count(_sql)
