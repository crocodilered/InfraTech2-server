__all__ = ['EquipmentProvider']


from collections import namedtuple


class EquipmentProvider:

    SQL_FILTER = '''
        SELECT
            id,
            identifier,
            title,
            description
        FROM equipment 
        WHERE 
            LOWER(identifier) LIKE "%{0}%" OR 
            LOWER(title) LIKE "%{0}%"
        ORDER BY 
            title'''

    SQL_INSERT = '''
        INSERT INTO equipment (
            identifier,
            title,
            description
        ) VALUES (
            "{1}",
            "{2}",
            "{3}"
        )'''

    SQL_UPDATE = '''
        UPDATE equipment SET
            identifier = "{1}",
            title = "{2}",
            description = "{3}"
        WHERE
            id = {0}'''

    @staticmethod
    def filter(conn, terms: str=None):
        """
        Search equipment by title and inventory number.
        :param conn: MySql connection
        :param terms: Search term
        :return: List of dicts
        """
        r = []
        if conn and terms:
            cursor = conn.cursor()
            sql = EquipmentProvider.SQL_FILTER.format(terms.lower())
            cursor.execute(sql)
            rows = cursor.fetchall()
            fields = ['id', 'identifier', 'title', 'description']
            for row in rows:
                r.append(dict(zip(fields, row)))
        return r

    @staticmethod
    def post(conn, item: list = None):
        """
        Create or update equipment record.
        :param conn: MySql connection.
        :param item: List of item's data: [id, inventory_num, title, description]
        :return: True in any case.
        """
        if conn and item and len(item) == 4:
            cursor = conn.cursor()
            if item[0] == 0:
                sql = EquipmentProvider.SQL_INSERT.format(*item)
            else:
                sql = EquipmentProvider.SQL_UPDATE.format(*item)
            cursor.execute(sql)
            conn.commit()
            return True
