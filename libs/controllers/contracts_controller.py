import cherrypy as cp
from libs.controllers.base_controller import BaseController
from libs.providers.contracts_provider import ContractsProvider


__all__ = ['ContractsController']


class ContractsController(BaseController):

    @cp.expose
    @cp.tools.auth()
    @cp.tools.json_in()
    @cp.tools.json_out()
    def filter(self):
        """ Return list of contracts by given term """
        r = {'errorCode': self.ERROR_WRONG_METHOD}
        if cp.request.method == 'POST':
            params = cp.request.json
            if params and 'terms' in params:
                r['rows'] = ContractsProvider.filter(cp.request.db, params['terms'])
                r['errorCode'] = 0
            else:
                r['errorCode'] = self.ERROR_WRONG_REQUEST
        return r

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
                ContractsProvider.post(cp.request.db, params['item'])
                r['errorCode'] = 0
            else:
                r['errorCode'] = self.ERROR_WRONG_REQUEST
        return r

    @cp.expose
    @cp.tools.auth()
    @cp.tools.json_in()
    @cp.tools.json_out()
    def current_list(self):
        """ Get list of contracts that actual for NOW-date """
        r = {'errorCode': self.ERROR_WRONG_METHOD}
        if cp.request.method == 'POST':
            r['rows'] = ContractsProvider.current_list(cp.request.db)
            r['errorCode'] = 0
        return r
