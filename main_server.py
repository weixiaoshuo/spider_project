import pymysql


import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.options import define, options
from .urls import handlers
from .config import settings

import torndb

define('port', type=int, default=8000, help='run server on the given port')


class Application(tornado.web.Application):

    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(args, kwargs)


def main():
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers, **settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()