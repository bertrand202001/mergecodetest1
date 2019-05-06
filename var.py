#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 13:16:00 2019

@author: yujzhang
"""

import numpy as np

closing_prices = np.loadtxt(
        '/Users/yujzhang/Documents/spider_data/data_set/da_data/aapl.csv', delimiter=',',
        usecols=(6), unpack=True)

mean = np.mean(closing_prices)
devs = closing_prices - mean
dsqs = devs ** 2 # 离差方

pvar = np.sum(dsqs) / dsqs.size #总体方差
pstd = np.sqrt(pvar) #总体标准差

svar = np.sum(dsqs) / (dsqs.size - 1) #样本方差
sstd = np.sqrt(svar) #样本标准差
print(pstd, sstd)

pstd = np.std(closing_prices)
sstd = np.std(closing_prices, ddof=1)
print(pstd, sstd)