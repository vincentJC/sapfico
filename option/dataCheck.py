#!/usr/bin/python3
# -*- encoding:utf-8 -*-
from openpyxl import Workbook
from openpyxl import load_workbook


typelist = {
    'cbzx': cbzxCheck,
    'jyht': jyhtCheck,
    'khzsj': khzsjCheck,
    'gyszsj': gyszsjCheck,
    'yhzsj': yhzsjCheck,
    'fzhs': yhzsjCheck,
    'zckp': zckpCheck
    }


def checkall(*args):
    for checkkey in args:
        typelist[args['typekey']](args['url'])


def cbzxCheck(arg):
    wb = load_workbook(arg)
    print(wb.get_sheet_names('成本中心主数据收集'))

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
