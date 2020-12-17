# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'
import string
import random


class URL:
    raw2short = {}
    short2raw = {}
    base_url = "http://127.0.0.1/short_url/"

    def __init__(self, raw_url):
        self.raw_url = raw_url

    @property
    def short_url(self):
        if self.raw2short.get(self.raw_url):
            return self.raw2short[self.raw_url]
        while True:
            path_ = ''.join([random.choice(string.hexdigits) for _ in range(5)])
            if path_ not in self.raw2short:
                self.short2raw[self.base_url + path_] = self.raw_url
                self.raw2short[self.raw_url] = self.base_url + path_
                break
        return self.base_url + path_




if __name__ == '__main__':
    url = URL(raw_url="https://www.youtube.com/watch?v=lgohIqT6HmA")
    print(url.short_url)
    url = URL(raw_url="https://www.youtube.com/watch?v=lgohIqT6HmA")
    print(url.short_url)
