import handler.sjjyHandler


URL = [
    (r'/', handler.sjjyHandler.indexHandler),
    (r'/shujujiaoyan', handler.sjjyHandler.uploadHandler),
]
