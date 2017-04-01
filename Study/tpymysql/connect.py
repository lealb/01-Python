# -*- coding: utf-8 -*-
# Description: pymysql 操作类
# 17-4-1:上午12:00
import logging
import itertools
import pymysql
from sqlite3 import OperationalError, Row
from tpymysql import tablequeryer, insert


class Connect(object):
    def __init__(self, host, database, user=None, password=None):
        self.host = host
        self.database = database

        args = dict(charset="utf8", database=database, init_command='SET time_zone = "+8:00"',
                    sql_mode="TRADITIONAL")

        if user is not None:
            args["user"] = user
        if password is not None:
            args["passwd"] = password

        # We accept a path to a MySQL socket file or a host(:port) string
        if "/" in host:
            args["unix_socket"] = host
        else:
            self.socket = None
            pair = host.split(":")
            if len(pair) == 2:
                args["host"] = pair[0]
                args["port"] = int(pair[1])
            else:
                args["host"] = host
                args["port"] = 3306

        self._db = None
        self._db_args = args
        try:
            self.reconnect()
        except:
            logging.error("Cannot connect to MySQL on %s", self.host,
                          exc_info=True)

    def __del__(self):
        self.close()

    def close(self):
        """Closes this database connection."""
        if self._db is not None:
            self._db.close()
            self._db = None

    def commit(self):
        if self._db is not None:
            try:
                self._db.ping()
            except:
                self.reconnect()
            try:
                self._db.commit()
            except Exception as e:
                self._db.rollback()
                logging.exception("Can not commit", e)

    def rollback(self):
        if self._db is not None:
            try:
                self._db.rollback()
            except Exception as e:
                logging.error("Can not rollback", e)

    def reconnect(self):
        """Closes the existing database connection and re-opens it."""
        self.close()
        self._db = pymysql.connect(**self._db_args)
        self._db.autocommit(False)

    def iter(self, query, *parameters):
        """Returns an iterator for the given query and parameters."""
        if self._db is None:
            self.reconnect()
        cursor = pymysql.cursors.SSCursor(self._db)
        try:
            self._execute(cursor, query, parameters)
            column_names = [d[0] for d in cursor.description]
            for row in cursor:
                yield Row(zip(column_names, row))
        finally:
            cursor.close()

    def query(self, query, *parameters):
        """Returns a row list for the given query and parameters."""
        cursor = self._cursor()
        try:
            self._execute(cursor, query, parameters)
            column_names = [d[0] for d in cursor.description]
            return [Row(itertools.izip(column_names, row)) for row in cursor]
        finally:
            cursor.close()

    def get(self, query, *parameters):
        """Returns the first row returned for the given query."""
        rows = self.query(query, *parameters)
        if not rows:
            return None
        elif len(rows) > 1:
            raise Exception("Multiple rows returned for Database.get() query")
        else:
            return rows[0]

    def execute(self, query, *parameters):
        """Executes the given query, returning the lastrowid from the query."""
        cursor = self._cursor()
        try:
            self._execute(cursor, query, parameters)
            return cursor.lastrowid
        finally:
            cursor.close()

    def count(self, query, *parameters):
        """Executes the given query, returning the count value from the query."""
        cursor = self._cursor()
        try:
            cursor.execute(query, parameters)
            return cursor.fetchone()[0]
        finally:
            cursor.close()

    def __getattr__(self, tablename):
        '''
        return single table queryer for select table
        '''
        return tablequeryer.TableQueryer(self, tablename)

    def fromQuery(self, Select):
        '''
        return single table queryer for query
        '''
        return tablequeryer.TableQueryer(self, Select)

    def insert(self, table, **datas):
        '''
        Executes the given parameters to an insert SQL and execute it
        '''
        return insert.Insert(self, table)(**datas)

    def executemany(self, query, parameters):
        """Executes the given query against all the given param sequences.
        We return the lastrowid from the query.
        """
        cursor = self._cursor()
        try:
            cursor.executemany(query, parameters)
            return cursor.lastrowid
        finally:
            cursor.close()

    def _cursor(self):
        if self._db is None: self.reconnect()
        try:
            self._db.ping()
        except:
            self.reconnect()
        return self._db.cursor()

    def _execute(self, cursor, query, parameters):
        try:
            return cursor.execute(query, parameters)
        except OperationalError:
            logging.error("Error connecting to MySQL on %s", self.host)
            self.close()
            raise
