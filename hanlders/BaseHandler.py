# coding:utf-8
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    """handler基类"""

    @property
    def db(self):
        return self.application.db

    # 这里的装饰器是个啥意思呢？

    @property
    def mongodb(self):
        return self.application.home_test

    def prepare(self):
        pass

    def write_error(self, status_code, **kwargs):
        pass

    def set_default_headers(self):
        pass

    def initialize(self):
        pass

    def on_finish(self):
        pass
