import cherrypy as cp
from libs.controllers.base_controller import BaseController
from libs.providers.equipment_provider import EquipmentProvider


__all__ = ['EquipmentController']


class EquipmentController(BaseController):

    @cp.expose
    @cp.tools.auth()
    @cp.tools.json_in()
    @cp.tools.json_out()
    def filter(self):
        """ Return list of equipment by given term """
        r = {'errorCode': self.ERROR_WRONG_METHOD}
        if cp.request.method == 'POST':
            params = cp.request.json
            if params and 'terms' in params:
                r['rows'] = EquipmentProvider.filter(cp.request.db, params['terms'])
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
                EquipmentProvider.post(cp.request.db, params['item'])
                r['errorCode'] = 0
            else:
                r['errorCode'] = self.ERROR_WRONG_REQUEST
        return r
