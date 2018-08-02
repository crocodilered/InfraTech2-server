import cherrypy


__all__ = ['Root']


class Root:

    @cherrypy.expose
    def index(self):
        pass
