import pymysql

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import torndb
from pymongo import MongoClient

from tornado.options import define, options
from .urls import handlers
import config

define('port', type=int, default=8000, help='run server on the given port')


class Application(tornado.web.Application):

    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(args, kwargs)
        self.db = torndb.Connection(**config.mysql_options)
        self.client = MongoClient(**config.mongodb_options)
        self.mongodb = self.client.ihome

def main():
    options.logging = config.log_lever
    options.log_file_prefix = config.log_file
    tornado.options.parse_command_line()
    app = Application(
        handlers, **config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
