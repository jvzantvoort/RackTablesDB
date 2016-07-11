#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""RackTablesDB.db - wrapper for database access"""

import RackTablesDB.config
import MySQLdb

class DatabaseException(Exception):
    """Exception Class for the RackTablesDB.db library

    :param str: the error message
    :type str: str
    :returns: Formatted exception message
    """

    def __init__(self, message=None):
        self.message = message
        Exception.__init__(self)

    def __str__(self):
        return "Database error %s" % self.message

class Database(object):
    """This class is a wrapper for the database access.

    """

    def __init__(self):
        self.config = RackTablesDB.config.Config()
        self._db = MySQLdb.connect(host=self.config.host,
                                   user=self.config.user,
                                   passwd=self.config.password,
                                   db=self.config.name)
        self._cursor = self._db.cursor(MySQLdb.cursors.DictCursor)

    def query(self, sql):

        if len(sql) == 0:
            raise DatabaseException("empty query string")

        self._cursor.execute(sql)
        return self._cursor.fetchall()

if __name__ == '__main__':
    db = Database()
    for row in db.query('show tables'):
        print row
