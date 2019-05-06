#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 02:03:55 2019

@author: yujzhang
"""

import numpy as np
import datetime as dt

def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    return (date - dt.date.min).days


days, closing_prices = np.loadtxt(
        '/Users/yujzhang/Documents/spider_data/maoyan.csv',
        delimiter=',', usecols=(1, 6), unpack=True, 
        converters={1: dmy2ymd})

twap = np.average(closing_prices, weights=days)
print(twap)