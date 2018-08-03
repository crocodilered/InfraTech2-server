__all__ = ['ContractsProvider']


class ContractsProvider:

    FIELDS = ['id', 'identifier', 'contractorTitle', 'value', 'beginDate', 'endDate']

    SQL_COUNT = 'SELECT COUNT(id) FROM contract'

    # Using DATE_FORMAT cos of date type is not JSON-serializable
    SQL_FILTER = '''
        SELECT
            id,
            identifier,
            contractor_title,
            value,
            DATE_FORMAT(begin_date, '%Y-%m-%d'),
            DATE_FORMAT(end_date, '%Y-%m-%d')
        FROM contract 
        WHERE 
            LOWER(identifier) LIKE "%{0}%" OR 
            LOWER(contractor_title) LIKE "%{0}%"
        ORDER BY 
            contractor_title'''

    SQL_INSERT = '''
        INSERT INTO contract (
            identifier,
            contractor_title,
            value,
            begin_date,
            end_date
        ) VALUES (
            "{identifier}",
            "{contractorTitle}",
            "{value}",
            "{beginDate}",
            "{endDate}"
        )'''

    SQL_UPDATE = '''
        UPDATE contract SET
            identifier = "{identifier}",
            contractor_title = "{contractorTitle}",
            value = "{value}",
            begin_date = "{beginDate}",
            end_date = "{endDate}"
        WHERE
            id = {id}'''

    SQL_CURRENT_LIST = '''
        SELECT
            id,
            identifier,
            contractor_title,
            value,
            DATE_FORMAT(begin_date, '%Y-%m-%d'),
            DATE_FORMAT(end_date, '%Y-%m-%d')
        FROM contract
        WHERE
            CURDATE() > begin_date AND
            CURDATE() <= end_date
        ORDER BY 
            contractor_title'''

    @staticmethod
    def filter(conn, terms: str=None):
        """
        Search contractor by title and contract number.
        :param conn: MySql connection
        :param terms: Search term
        :return: List of tuples
        """
        r = []
        if conn and terms:
            cursor = conn.cursor()
            sql = ContractsProvider.SQL_FILTER.format(terms.lower())
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                r.append(dict(zip(ContractsProvider.FIELDS, row)))
        return r if len(r) > 0 else None

    @staticmethod
    def post(conn, item: dict = None):
        """
        Create or update contractor record.
        :param conn: MySql connection.
        :param item: List of item's data: [id, contract_num, title, value, 'begin_date', 'end_date']
        :return: True in any case.
        """
        if conn and item:
            cursor = conn.cursor()
            sql = ContractsProvider.SQL_INSERT if item['id'] == 0 else ContractsProvider.SQL_UPDATE
            cursor.execute(sql.format(**item))
            conn.commit()
        return True

    @staticmethod
    def current_list(conn):
        r = []
        if conn:
            cursor = conn.cursor()
            cursor.execute(ContractsProvider.SQL_CURRENT_LIST)
            rows = cursor.fetchall()
            for row in rows:
                r.append(dict(zip(ContractsProvider.FIELDS, row)))
        return r if len(r) > 0 else None

    @staticmethod
    def count(conn):
        r = None
        if conn:
            cursor = conn.cursor()
            cursor.execute(ContractsProvider.SQL_COUNT)
            r = cursor.fetchone()[0]
        return r
