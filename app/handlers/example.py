import tornado
from tornado.web import RequestHandler

class ExampleHandler(RequestHandler):
    def get():
        # Do stuff here

        self.render("example.html")