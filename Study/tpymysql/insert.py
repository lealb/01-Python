# -*- coding: utf-8 -*-
# Description:
# 17-4-1:上午12:49
class Insert(object):
    '''
    Insert Query Generator
    '''

    def __init__(self, db, tablename):
        self.db = db
        self.tablename = tablename

    def __call__(self, **fileds):
        columns = fileds.keys()
        _prefix = "".join(['INSERT INTO ', '`', self.tablename, '`'])
        _fields = ",".join(["".join(['`', column, '`']) for column in columns])
        _values = ",".join(["%s" for i in range(len(columns))])
        _sql = "".join([_prefix, "(", _fields, ") VALUES (", _values, ")"])
        _params = [fileds[key] for key in columns]
        return self.db.execute(_sql, *tuple(_params))
