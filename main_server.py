import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import torndb
from pymongo import MongoClient

from tornado.options import define, options
from urls import handlers
from config import *

define('port', type=int, default=8800, help='run server on the given port')

class Application(tornado.web.Application):

    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.db = torndb.Connection(**mysql_options)
        self.client = MongoClient(**mongodb_options)
        self.mongodb = self.client.ihome

def main():
    options.logging = log_lever
    options.log_file_prefix = log_file
    tornado.options.parse_command_line()
    app = Application(
        handlers, **settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
