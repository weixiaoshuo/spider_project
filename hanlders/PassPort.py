from .BaseHandler import BaseHandler
import logging


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        logging.debug('debug msg')
        logging.info('info msg')
        logging.warning('warning msg')
        logging.error('error msg')
        self.write("hello tornado")
