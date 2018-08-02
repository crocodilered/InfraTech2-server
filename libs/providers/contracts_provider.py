__all__ = ['ContractsProvider']


class ContractsProvider:

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
            contractor_title
    '''

    SQL_INSERT = '''
        INSERT INTO contract (
            identifier,
            contractor_title,
            value,
            begin_date,
            end_date
        ) VALUES (
            "{1}",
            "{2}",
            "{3}",
            "{4}",
            "{5}"
        )
    '''

    SQL_UPDATE = '''
        UPDATE contract SET
            identifier = "{1}",
            contractor_title = "{2}",
            value = "{3}",
            begin_date = "{4}",
            end_date = "{5}"
        WHERE
            id = {0}
    '''

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
            contractor_title
    '''

    @staticmethod
    def filter(conn, terms: str=None):
        """
        Search contractor by title and contract number.
        :param conn: MySql connection
        :param terms: Search term
        :return: List of tuples
        """
        r = None
        if conn and terms:
            cursor = conn.cursor()
            sql = ContractsProvider.SQL_FILTER.format(terms.lower())
            cursor.execute(sql)
            rows = cursor.fetchall()
            r = rows
        return r

    @staticmethod
    def post(conn, item: list = None):
        """
        Create or update contractor record.
        :param conn: MySql connection.
        :param item: List of item's data: [id, contract_num, title, value, 'begin_date', 'end_date']
        :return: True in any case.
        """
        if conn and item and len(item) == 6:
            cursor = conn.cursor()
            if item[0] == 0:
                sql = ContractsProvider.SQL_INSERT.format(*item)
            else:
                sql = ContractsProvider.SQL_UPDATE.format(*item)
            cursor.execute(sql)
            conn.commit()
            return True

    @staticmethod
    def current_list(conn):
        r = None
        if conn:
            cursor = conn.cursor()
            cursor.execute(ContractsProvider.SQL_CURRENT_LIST)
            rows = cursor.fetchall()
            r = rows
        return r
