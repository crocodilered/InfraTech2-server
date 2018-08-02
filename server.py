import os
import cherrypy
from libs.tools.auth_tool import AuthTool
from libs.plugins.db_plugin import DbPlugin as DbPlugin
from libs.plugins.auth_plugin import AuthSessions as AuthSessionsPlugin

cherrypy.tools.auth = AuthTool()

from libs.controllers.root import Root as RootController
from libs.controllers.auth_controller import AuthController
from libs.controllers.equipment_controller import EquipmentController
from libs.controllers.contracts_controller import ContractsController
from libs.controllers.maintenance_controller import MaintenanceController
from libs.controllers.analytics_controller import AnalyticsController

app = RootController()
app.auth = AuthController()
app.equipment = EquipmentController()
app.contracts = ContractsController()
app.maintenance = MaintenanceController()
app.analytics = AnalyticsController()

curr_dir = os.path.abspath(os.path.dirname(__file__))
conf_file = os.path.join(curr_dir, 'conf', 'server.conf')

application = cherrypy.tree.mount(app, '/', conf_file)

cherrypy.config.update(conf_file)

db_conf = application.config['Database']
DbPlugin(cherrypy.engine, {
    'host': db_conf['mysql.host'],
    'port': db_conf['mysql.port'],
    'user': db_conf['mysql.user'],
    'password': db_conf['mysql.password'],
    'database': db_conf['mysql.database']
}).subscribe()

AuthSessionsPlugin(cherrypy.engine).subscribe()

if __name__ == '__main__':
    cherrypy.engine.start()
