# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'
import string
import random

from api.configs import API


class URL:
    raw2short = {}
    short2raw = {}
    base_url = "http://127.0.0.1:%s/short2raw/" % (API.port.value, )

    def __init__(self, raw_url):
        self.raw_url = raw_url

    @property
    def short_url(self):
        if len(self.raw2short) < len(string.ascii_letters)**API.path_length.value:
            if self.raw2short.get(self.raw_url):
                return self.raw2short[self.raw_url]
            while True:
                path_ = ''.join([random.choice(string.ascii_letters) for _ in
                                 range(API.path_length.value)])
                if path_ not in self.raw2short:
                    self.short2raw[self.base_url + path_] = self.raw_url
                    self.raw2short[self.raw_url] = self.base_url + path_
                    break
            return self.base_url + path_
        else:
            raise Exception