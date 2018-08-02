import cherrypy as cp
from libs.controllers.base_controller import BaseController


__all__ = ['AnalyticsController']


class AnalyticsController(BaseController):
    """
    Custom queries class.
    It looks like there is no need allotted data provider.
    """

    @cp.expose
    @cp.tools.auth()
    @cp.tools.json_in()
    @cp.tools.json_out()
    def dashboard(self):
        """ Return all the data needed on the dashboard """
        r = {'errorCode': 0}
        conn = cp.request.db

        # Budget execution
        cursor = conn.cursor()
        sql = '''
            SELECT 
                DATE_FORMAT(begin_date, "%Y-%m-%d"), 
                DATE_FORMAT(end_date, "%Y-%m-%d"), 
                CONVERT(value, char)
            FROM budget 
            WHERE
                CURDATE() >= begin_date AND
                CURDATE() <= end_date
            LIMIT 1
        '''
        cursor.execute(sql)
        budget_row = cursor.fetchone()

        sql = '''
            SELECT CONVERT(SUM(value), char) 
            FROM maintenance 
            WHERE 
                end_date >= "{0}" AND 
                end_date <= "{1}"
        '''.format(*budget_row)
        cursor.execute(sql)
        budget_exec_row = cursor.fetchone()

        r['budget'] = {
            'beginDate': budget_row[0],
            'endDate': budget_row[1],
            'value': budget_row[2],
            'execution': budget_exec_row[0],
        }

        return r

