#!/usr/bin/python3
# -*- encoding:utf-8 -*-
import tornado.web
import appconfig
import os
import datetime
import time
import option.dataCheck
# 主页
class indexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

# 数据上载及校验
class downloadHandler(tornado.web.RequestHandler):
    def post(self):
        uplistname = {
            'cbzx':'成本中心',
            'jyht':'简易合同',
            'khzsj':'客户主数据',
            'gyszsj':'供应商主数据',
            'yhzsj':'银行主数据',
            'fzhs':'辅助核算',
            'zckp':'资产卡片'
            }
        fileNewName = {}
        fileNewList = []
        # 字典循环
        for inputname in uplistname:
            if self.request.files.get(inputname) is None:
                continue
            else:
                fileMeta = self.request.files[inputname]
            # 生成新的文件名字，时间+原文件名
            fileName = datetime.datetime.now().strftime('%Y%m%d%H%M')+'_'+fileMeta[0]['filename']
            # 生成文件路径
            filePath = os.path.join(appconfig.upload_path,fileName)
            # 生成文件字典
            fileNewName['type'] = uplistname.get(inputname)
            fileNewName['name'] = fileName
            fileNewName['url'] = filePath
            fileNewName['typekey'] = inputname
            # 生成上传文件列表
            fileNewList.append(fileNewName)
            # 重置字典文件
            fileNewName = {}
            with open(filePath,'wb') as upfile:
                upfile.write(fileMeta[0]['body'])
        self.write('<p style="color:green">正在验证数据，请等待！</p><br>')
        self.flush()
        #time.sleep(2)
        option.dataCheck.checkall(fileNewList)
        self.write('<p style="color:green">数据验证完毕，请下载数据</p><br>')
        self.render('check.html', files=fileNewList)
