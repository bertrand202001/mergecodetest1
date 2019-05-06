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
    

wdays, opening_prices, highest_prices, lowest_prices, closing_prices = np.loadtxt(
        '/Users/yujzhang/Documents/spider_data/data_set/da_data/aapl.csv', delimiter=',',
        usecols=(1, 3, 4, 5, 6), 
        unpack=True, 
        dtype='M8[D], f8, f8, f8, f8',
        converters={1: dmy2wday})

wdays = wdays[:16]
opening_prices = opening_prices[:16]
highest_prices = highest_prices[:16]
lowest_prices = lowest_prices[:16]
closing_prices = closing_prices[:16]

#第一个星期一的索引
first_monday = np.where(wdays == 0)[0][0]
last_friday = np.where(wdays == 4)[0][-1]
indices = np.arange(first_monday, last_friday + 1)
indices = np.split(indices, 3)

def week_summary(indices):
    opening_price = opening_prices[indices[0]]
    highest_price = highest_prices[indices].max()
    lowest_price = lowest_prices[indices].min()
    closing_price = closing_prices[indices[-1]]
    return opening_price, highest_price, lowest_price, closing_price
            
summaries = np.apply_along_axis(week_summary, 1, indices)
print(summaries)
np.savetxt('/Users/yujzhang/Documents/spider_data/data_set/da_data/aapl2.csv', summaries,
           delimiter=',', fmt='%g')