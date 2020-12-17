# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'
import string
import random


class URL:
    raw2short = {}

    def __init__(self, raw_url):
        self.raw_url = raw_url

    #TODO cached_property
    @property
    def short_url(self):
        while True:
            path_ = ''.join([random.choice(string.hexdigits) for _ in range(5)])
            if path_ not in self.raw2short:
                self.raw2short[path_] = self.raw_url
                break
        return path_




if __name__ == '__main__':
    url = URL(raw_url="https://www.youtube.com/watch?v=lgohIqT6HmA")
    print(url.short_url)
    url = URL(raw_url="https://www.youtube.com/watch?v=lgohIqT6HmA")
    print(url.short_url)
    print(url.short_url)
