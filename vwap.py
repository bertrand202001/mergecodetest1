#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 02:03:55 2019

@author: yujzhang
"""

import numpy as np

closing_prices, volumes = np.loadtxt(
        '/Users/yujzhang/Documents/spider_data/maoyan.csv',
        delimiter=',', usecols=(6, 7), unpack=True)

vwap, wsum = 0, 0
for closing_price, volume in zip(closing_prices, volumes):
    vwap += closing_price * volume
    wsum += volume
    
vwap /= wsum
print(vwap)
vwap = np.average(closing_prices, weight=volumes)
print(vwap)

mean = np.mean(closing_prices)
print(mean)