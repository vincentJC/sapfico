import os.path


port = 8000

settings = {
    #设置templates路径：
    'template_path':os.path.join(os.path.dirname(__file__),"templates"),
    #设置静态文件解析路径：
    'static_path':os.path.join(os.path.dirname(__file__),"static"),
    #设置调试模式：
    'debug':True,
    #设置gzip压缩：
    'gzip':True,
}
