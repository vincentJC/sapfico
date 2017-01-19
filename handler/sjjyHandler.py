import tornado.web


# 主页
class indexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

# 数据存储
class uploadHandler(tornado.web.RequestHandler):
    def post(self):
        self.render('check.html')
