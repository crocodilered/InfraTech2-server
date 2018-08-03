__all__ = ['EquipmentProvider']


class EquipmentProvider:

    FIELDS = ['id', 'identifier', 'title', 'description']

    SQL_COUNT = 'SELECT COUNT(id) FROM equipment'

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
            "{identifier}",
            "{title}",
            "{description}"
        )'''

    SQL_UPDATE = '''
        UPDATE equipment SET
            identifier = "{identifier}",
            title = "{title}",
            description = "{description}"
        WHERE
            id = {id}'''

    @staticmethod
    def filter(conn, terms: str=None):
        """
        Search equipment by title and inventory number.
        :param conn: MySql connection
        :param terms: Search term
        :return: List of dicts
        """
        if conn and terms:
            r = []
            cursor = conn.cursor()
            sql = EquipmentProvider.SQL_FILTER.format(terms.lower())
            cursor.execute(sql)
            for row in cursor.fetchall():
                r.append(dict(zip(EquipmentProvider.FIELDS, row)))
            return r
        return None

    @staticmethod
    def post(conn, item: dict = None):
        """
        Create or update equipment record.
        :param conn: MySql connection.
        :param item: Dict with item's data: id, identifier, title, description
        :return: True in any case.
        """
        if conn and item:
            cursor = conn.cursor()
            sql = EquipmentProvider.SQL_INSERT if item['id'] == 0 else EquipmentProvider.SQL_UPDATE
            cursor.execute(sql.format(**item))
            conn.commit()
            return True
        return False

    @staticmethod
    def count(conn):
        r = None
        if conn:
            cursor = conn.cursor()
            cursor.execute(EquipmentProvider.SQL_COUNT)
            r = cursor.fetchone()[0]
        return r
