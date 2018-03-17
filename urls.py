from hanlders import PassPort
from hanlders import VerifyCode
from tornado.web import StaticFileHandler
import os

handlers = [
    #(r'/', PassPort.IndexHandler),
    (r'/api/piccode', VerifyCode.ImageCodeHandler),
    (r'/(.*)', StaticFileHandler,dict(path=os.path.join(os.path.dirname(__file__),
                                'html'), default_filename='index.html')),
]
