#!/usr/bin/python3
# -*- encoding:utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import url
import appconfig


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        url.URL,
        **appconfig.settings
    )
    httpser = tornado.httpserver.HTTPServer(app)
    httpser.listen(appconfig.port)
    tornado.ioloop.IOLoop.current().start()
