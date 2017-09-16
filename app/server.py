import tornado

from services import *
from handlers import *


class GIFStory(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        api_routes = [("/api/v1" + h[0], h[1]) for h in API_HANDLERS]
        handlers = [(r"/", HomeHandler), *api_routes]
        settings = {
            "template_path":"./templates"
        }
        clean_kwargs = { x:kwargs[x] for x in filter(lambda x: if x in settings.keys(), kwargs.keys()) }
        super().__init__(handlers, *args, **kwargs, **settings)

if __name__ == "__main__":
    # Make server
    app = GIFStory()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()