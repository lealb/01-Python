# -*- coding: utf-8 -*-
# Description:
# 17-4-1:上午12:48

class Delete(object):
    def __init__(self, db, tablename, where):
        self.db = db
        self._tablename = tablename
        self._where = where

    def __call__(self):
        _sql_slice = ["DELETE FROM ", "`", self._tablename, "`"]
        if self._where:
            _sql_slice.append(" WHERE ")
            _sql_slice.append(self._where.get_sql())
            _sql = "".join(_sql_slice)
            return self.db.execute(_sql, self._where.get_params())
