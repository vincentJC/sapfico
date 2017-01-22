#!/usr/bin/python3
# -*- encoding:utf-8 -*-
from openpyxl import Workbook
from openpyxl import load_workbook
import appconfig


#typelist = {
#    'cbzx':cbzxCheck,
#    'jyht':jyhtCheck,
#    'khzsj':khzsjCheck,
#    'gyszsj':gyszsjCheck,
#    'yhzsj':yhzsjCheck,
#    'fzhs':yhzsjCheck,
#    'zckp':zckpCheck
#    }


def checkall(*args):
    for checkkey in args:
        if checkkey['typekey'] == 'cbzx':
            print(checkkey['url'])
            cbzxCheck(checkkey['url'],checkkey['name'])
        elif checkkey['typekey'] == 'jyht':
            jyhtCheck(checkkey['url'],checkkey['name'])
        elif checkkey['typekey'] == 'jyht':
            khzsjCheck(checkkey['url'],checkkey['name'])
        elif checkkey['typekey'] == 'jyht':
            gyszsjCheck(checkkey['url'],checkkey['name'])
        elif checkkey['typekey'] == 'jyht':
            yhzsjCheck(checkkey['url'],checkkey['name'])
        elif checkkey['typekey'] == 'jyht':
            fzhsCheck(checkkey['url'],checkkey['name'])
        elif checkkey['typekey'] == 'jyht':
            zckpCheck(checkkey['url'],checkkey['name'])
        else:
            continue



def cbzxCheck(url,name):
    wb = load_workbook(url)
    #print(wb.get_sheet_names('成本中心主数据收集'))
    ws = wb['成本中心主数据收集']
    for row in ws.rows:
        for cell in row:
            cell.value = 1
    wb.save(url)


def jyhtCheck(arg):
    pass


def khzsjCheck(arg):
    pass


def gyszsjCheck(arg):
    pass


def yhzsjCheck(arg):
    pass


def fzhsCheck(arg):
    pass


def zckpCheck(arg):
    pass
