#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 13:16:00 2019

@author: yujzhang
"""

import numpy as np
import datetime as dt

#转换器函数： 将日-月-年格式的日期字符串转换为星期

def dmy2wday(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    wday = date.weekday() #用0-6表示周一至周日
    return wday
    

wdays, closing_prices = np.loadtxt(
        '/Users/yujzhang/Documents/spider_data/data_set/da_data/aapl.csv', delimiter=',',
        usecols=(1, 6), unpack=True, converters={1: dmy2wday})

print(wdays)

ave_closing_prices = np.zeros(5)
for wday in range(ave_closing_prices.size):
    ave_closing_prices[wday] = np.take(closing_prices, np.where(wdays == wday)).mean()

for wday, ave_closing_price in zip(['MON','TUE','WED','THU','FRI'], ave_closing_prices):
    print(wday, np.round(ave_closing_price, 2))