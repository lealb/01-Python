# -*- coding: utf-8 -*-
# Description:
# 17-4-1:上午12:46

class Count(object):
    '''
    Count with current where clouse
    '''

    def __init__(self, db, tablename, where):
        self.db = db
        self.tablename = tablename
        self.where = where

    def __call__(self):
        if self.where:
            _sql = "".join(["SELECT count(1) FROM ", self.tablename, " where ", self.where.get_sql()])
            _params = self.where.get_params()
            return self.db.count(_sql, *_params)
        else:
            _sql = "".join(["SELECT count(1) FROM ", self.tablename])
            return self.db.count(_sql)
