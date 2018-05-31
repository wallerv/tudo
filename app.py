# -*- coding:utf-8 -*- 
"""
-------------------------------------------------
   File Name：     app
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
from handlers import main
from tornado.options import define, options

define('port', default=80, help='run server port', type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            ('/', main.IndexHanader),
            ('/expolre', main.ExploreHanader),
            ('/post/(?P<post_id>[0-9]+)', main.PostHanader)
        ]
        settings = dict(
            debug=True,
            template_path='templates',
            static_path='static'
        )

        super(Application, self).__init__(handlers, **settings)


application = Application()

if __name__ == '__main__':
    tornado.options.parse_command_line()
    application.listen(options.port)
    print("Server start on port {}".format(str(options.port)))
    tornado.ioloop.IOLoop.current().start()
