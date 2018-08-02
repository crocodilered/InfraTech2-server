__all__ = ['MaintenanceProvider']


class MaintenanceProvider:

    SQL_INSERT = '''
        INSERT INTO maintenance (
            user_id,
            equipment_id,
            contract_id,
            end_date,
            title,
            value
        ) VALUES (
            "{1}",
            "{2}",
            "{3}",
            "{4}",
            "{5}",
            "{6}"
        )
    '''

    SQL_UPDATE = '''
        UPDATE maintenance SET
            user_id = {1},
            equipment_id = {2},
            contract_id = {3},
            end_date = "{4}",
            title = "{5}",
            value = {6}
        WHERE
            id = {0}
    '''

    SQL_LIST = '''
        SELECT
            user.email,
            equipment.identifier,
            equipment.title,
            contract.identifier,
            contract.contractor_title,
            DATE_FORMAT(maintenance.end_date, '%Y-%m-%d'),
            maintenance.title,
            maintenance.value
        FROM maintenance
        LEFT JOIN user ON user.id = maintenance.user_id
        LEFT JOIN contract ON contract.id = maintenance.contract_id
        LEFT JOIN equipment ON equipment.id = maintenance.equipment_id
        ORDER BY maintenance.end_date DESC 
        '''

    @staticmethod
    def post(conn, item: list = None):
        """
        Create or update contractor record.
        :param conn: MySql connection.
        :param item: List of item's data: [id, contract_num, title, value, 'begin_date', 'end_date']
        :return: True in any case.
        """
        if conn and item and len(item) == 7:
            cursor = conn.cursor()
            if item[0] == 0:
                sql = MaintenanceProvider.SQL_INSERT.format(*item)
            else:
                sql = MaintenanceProvider.SQL_UPDATE.format(*item)
            cursor.execute(sql)
            conn.commit()
            return True

    @staticmethod
    def list(conn, count=None, offset=None):
        r = None
        if conn:
            cursor = conn.cursor()
            sql = MaintenanceProvider.SQL_LIST
            if offset and count:
                sql += ' LIMIT {}, {}'.format(offset, count)
            elif count:
                sql += ' LIMIT {}'.format(count)
            cursor.execute(sql)
            rows = cursor.fetchall()
            r = rows
        return r
