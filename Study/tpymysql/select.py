# -*- coding: utf-8 -*-
# Description:
# 17-4-1:上午12:47
from sqlite3 import OperationalError


class Select:
    '''
    Select list with current where clouse 
    '''

    def __init__(self, db, tablename, where):
        self.db = db
        self._tablename = tablename
        self._where = where
        self._sort_fields = []
        self._limit = None
        self._fields = []
        self._groups = []
        self._having = None

    def sort(self, **fields):
        del self._sort_fields[:]
        for key in fields.keys():
            self._sort_fields.append("".join(["`", key, "` ", fields[key]]))
        return self

    def limit(self, start, count):
        self._limit = "".join(["LIMIT ", str(start), ",", str(count)])
        return self

    def collect(self, *fields):
        if len(fields):
            self._fields += fields
        return self

    def group_by(self, *fields):
        if len(fields) < 1:
            print(OperationalError, "Must have a field")
        for f in fields:
            self._groups.append(f)

    def having(self, cond):
        self._having = cond

    def __getslice__(self, pid, pcount):
        if pid < 1:
            print(OperationalError, "Wrong page id,page id can not lower than 1")
        if pcount < 1:
            print(OperationalError, "Wrong page size,page size can not lower than 1")
        _start = (pid - 1) * pcount
        self._limit = "".join(["LIMIT ", str(_start), ",", str(pcount)])
        return self

    def get_sql(self):
        _sql_slice = ["SELECT "]
        if self._fields:
            _sql_slice.append(",".join(["".join(["`", str(f), "`"]) for f in self._fields]))
        else:
            _sql_slice.append("*")
        _sql_slice.append(" FROM `")
        if str(self._tablename.__class__) == "database.Select":
            _sql_slice.append("(")
            _sql_slice.append(self._tablename.get_sql())
            _sql_slice.append(")t")
        else:
            _sql_slice.append(self._tablename)
        _sql_slice.append("`")
        if self._where:
            _sql_slice.append(" WHERE ")
            if str(self._tablename.__class__) == "database.Select":
                _sql_slice.append(self._where.get_sql(tn='t'))
            else:
                _sql_slice.append(self._where.get_sql())
            _sql_slice.append(" ")
        if len(self._groups) > 0:
            _sql_slice.append("GROUP BY ")
            if str(self._tablename.__class__) == "database.Select":
                _sql_slice.append(",".join([f.get_sql(tn="t") for f in self._groups]))
            else:
                _sql_slice.append(",".join([f.get_sql() for f in self._groups]))
            if self._having:
                _sql_slice.append(" HAVING ")
                _sql_slice.append(self._having.get_sql())
                _sql_slice.append(" ")
        if self._sort_fields:
            _sql_slice.append("ORDER BY ")
            if str(self._tablename.__class__) == "database.Select":
                _sql_slice.append(",".join([self._add_tb('t', s) for s in self._sort_fields]))
            else:
                _sql_slice.append(",".join([s for s in self._sort_fields]))
        if self._limit:
            _sql_slice.append(" ")
            _sql_slice.append(self._limit)
        return "".join(_sql_slice)

    def _add_tb(self, tn, src):
        import re
        p = compile(r'`(\w*?)`')
        return p.sub(r'`%s.\1`' % tn, src)

    def __call__(self):
        _sql = self.get_sql()
        _plist = []
        if str(self._tablename.__class__) == "database.Select":
            for p in self._tablename.get_sql():
                _plist.append(p)
        if self._where:
            for p in self._where:
                _plist.append(p)
        if self._having:
            for p in self._having.get_params():
                _plist.append(p)
        if _plist:
            return self.db.query(_sql, *_plist)
        else:
            return self.db.query(_sql)
