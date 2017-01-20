#!/usr/bin/python3
# -*- encoding:utf-8 -*-
import handler.sjjyHandler


URL = [
    (r'/', handler.sjjyHandler.indexHandler),
    (r'/download', handler.sjjyHandler.downloadHandler)
]
