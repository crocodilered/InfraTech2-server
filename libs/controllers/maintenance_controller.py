import cherrypy as cp
from libs.controllers.base_controller import BaseController
from libs.providers.maintenance_provider import MaintenanceProvider


__all__ = ['MaintenanceController']


class MaintenanceController(BaseController):

    @cp.expose
    @cp.tools.auth()
    @cp.tools.json_in()
    @cp.tools.json_out()
    def post(self):
        """ Update or create given item """
        r = {'errorCode': self.ERROR_WRONG_METHOD}
        if cp.request.method == 'POST':
            params = cp.request.json
            if params and 'item' in params:
                MaintenanceProvider.post(cp.request.db, params['item'])
                r['errorCode'] = 0
            else:
                r['errorCode'] = self.ERROR_WRONG_REQUEST
        return r

    @cp.expose
    @cp.tools.auth()
    @cp.tools.json_in()
    @cp.tools.json_out()
    def list(self):
        """ List maintenance records """
        r = {'errorCode': self.ERROR_WRONG_METHOD}
        if cp.request.method == 'POST':
            params = cp.request.json
            count = params['count'] if params and 'count' in params else None
            offset = params['offset'] if params and 'offset' in params else None
            rows = MaintenanceProvider.list(cp.request.db, count, offset)
            if rows:
                r['data'] = []
                for row in rows:
                    d = {
                        'user': {
                            'email': row[0]
                        },
                        'equipment': {
                            'identifier': row[1],
                            'title': row[2],
                        },
                        'contract': {
                            'identifier': row[3],
                            'contractorTitle': row[4],
                        },
                        'endDate': row[5],
                        'title': row[6],
                        'value': row[7]
                    }
                    r['data'].append(d)
            r['errorCode'] = 0
        return r
