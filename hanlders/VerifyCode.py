# coding:utf-8

from .BaseHandler import BaseHandler
import logging
from utils.captcha import captcha
import constants

class ImageCodeHandler(BaseHandler):
    """"""

    def get(self):
        code_id = self.get_argument('cur')
        pre_code_id = self.get_argument('pre')
        if pre_code_id :
            try:
                pass
            except Exception as e:
                logging.error(e)
        name, text, image = captcha.captcha.generate_captcha()

        self.mongodb.insert({"imageCode": code_id , "text": text})
        self.set_header("Content-Type", "/image/jpg")
        self.write(image)
