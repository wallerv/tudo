# -*- coding:utf-8 -*- 
"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :       Administrator
   date：          2018/5/31
-------------------------------------------------
   Change Activity:
                   2018/5/31:
-------------------------------------------------
"""
__author__ = 'Administrator'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
import time
from tornado.options import define, options


class IndexHanader(tornado.web.RequestHandler):
    """

    """

    def get(self, *args, **kwargs):
        self.render('index.html')


class ExploreHanader(tornado.web.RequestHandler):
    """

    """

    def get(self, *args, **kwargs):
        self.render('explore.html')


class PostHanader(tornado.web.RequestHandler):
    """

    """

    def get(self, post_id):
        self.render('post.html', post_id=post_id)
