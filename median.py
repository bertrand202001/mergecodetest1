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

size = closing_prices.size

sorted_prices = np.msort(closing_prices)

median = (sorted_prices[int((size - 1) / 2)] + sorted_prices[int(size / 2)]) / 2

print(median)
median = np.median(closing_prices)
print(median)