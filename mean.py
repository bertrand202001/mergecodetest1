#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 22:25:28 2019

@author: yujzhang
"""

import numpy as np
import datatime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md


closing_prices = np.loadtxt(
        '/Users/yujzhang/Documents/spider_data/maoyan.csv',
        delimiter=',', usecols=(6), unpack=True)

mean = 0
for closing_price in closing_prices:
    mean += closing_price
    
mean /= closing_prices.size
print(mean)

mean = np.mean(closing_prices)
print(mean)
