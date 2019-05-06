#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:08:05 2019

@author: yujzhang
"""

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8])

print(a, b)
c = np.convolve(a, b, 'full')
print(c)

d = np.convolve(a, b, 'same')
print(d)

e = np.convolve(a, b, 'valid')
print(e)