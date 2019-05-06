#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 13:08:22 2019

@author: yujzhang
"""

import numpy as np

#产生9个介于【10，100）区间的随机数
a = np.random.randint(10, 100, 9)

print(a)
print(np.max(a), np.min(a))

print(np.argmax(a), np.argmin(a))