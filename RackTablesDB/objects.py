
"""

MariaDB [racktables_db]> describe Object;
+--------------+------------------+------+-----+---------+----------------+
| Field        | Type             | Null | Key | Default | Extra          |
+--------------+------------------+------+-----+---------+----------------+
| id           | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name         | char(255)        | YES  |     | NULL    |                |
| label        | char(255)        | YES  |     | NULL    |                |
| objtype_id   | int(10) unsigned | NO   | MUL | 1       |                |
| asset_no     | char(64)         | YES  | UNI | NULL    |                |
| has_problems | enum('yes','no') | NO   |     | no      |                |
| comment      | text             | YES  |     | NULL    |                |
+--------------+------------------+------+-----+---------+----------------+


"""

import RackTablesDB.db


class Object(object):

    def __init__(self):
        self.object_id = int()
        self.object_name = str()
        self._db = RackTablesDB.db.Database()
        self.base_query = """SELECT
          obj.`id`,
          obj.`name`,
          obj.`label`,
          obj.`asset_no`,
          obj.`has_problems`,
          obj.`comment`,
          dict.`dict_value` as object_type
        FROM `Object` obj
        LEFT OUTER JOIN `Dictionary` dict
        ON
          obj.`objtype_id` = dict.`dict_key`"""

    def _where(self, **kwargs):
        """

        Example::

          obj = RackTablesDB.objects.Object()

          for row in obj._where(object_type = 'Server'):
               print row['id'], row['name']

        :param kwargs: where clause items
        :return: list of dictionaries
        """
        sql = self.base_query
        sqll = list()

        for k, v in kwargs.iteritems():
            sqll.append("%s = %s" % (k, v))
        sql += " WHERE %s" % " AND ".join(sqll)
        return self._db.query(sql)

    def _get_col(self, column, **where):
        """

        Example::

          obj = RackTablesDB.objects.Object()

          row = obj._get_col(name = 'webserver1')

        :param column:
        :type column: str
        :param where:
        :type where: dict
        :return: dict
        """
        id_data = self._where(**where)
        retv = list()

        if len(id_data) != 1:
            return retv

        row = id_data[0]

        try:
            return row[column]
        except KeyError:
            return

    def getnameid(self, name):
        """
        Example::

          obj = RackTablesDB.objects.Object()

          id = obj.getnameid('webserver1')

        :param name:
        :return:
        """
        return self._get_col('id', name = name)

    def getidname(self, id):
        """
        Example::

          obj = RackTablesDB.objects.Object()

          id = obj.getidname(1)

        :param id

        :return:
        """

        return self._get_col('name', id = id)

class Rack(Object):

    def __init__(self):
        super(Rack, self).__init__()
        self.base_query += " WHERE object_type = \"Rack\""

    def list(self):
        return self._db.query(self.base_query)

    def _where(self, **kwargs):
        """

        Example::

          obj = RackTablesDB.objects.Rack()

          for row in obj._where(has_problems = 'yes'):
               print row['id'], row['name']

        :param kwargs: where clause items
        :return: list of dictionaries
        """
        sql = self.base_query
        sqll = list()

        for k, v in kwargs.iteritems():
            sqll.append("%s = %s" % (k, v))
        sql += " %s" % " AND ".join(sqll)
        return self._db.query(sql)

    def add(self, **kwargs):
        pass

    def remove(self, id):
        pass

