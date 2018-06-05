# -*- coding: utf-8 -*-
# Description:
# 17-4-1:上午12:48
from sqlite3 import OperationalError


class Update:
    '''
    Update Query Generator
    '''

    def __init__(self, db, tablename, where):
        self.db = db
        self._tablename = tablename
        self._where = where
        self._update_cols = None

    def __call__(self, *fields):
        if len(fields) < 1:
            print(OperationalError, "Must have unless 1 field to update")
            # raise
        _params = []
        _cols = []
        for f in fields:
            _cols.append(f.get_sql())
            _params.append(f.get_params()[0])
        _sql_slice = ["UPDATE ", self._tablename, " SET ", ",".join(_cols)]
        if self._where:
            _sql_slice.append(" WHERE ")
            _sql_slice.append(self._where.get_sql())
            for p in self._where.get_params():
                _params.append(p)
        _sql = "".join(_sql_slice)
        return self.db.execute(_sql, *_params)
