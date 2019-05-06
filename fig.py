#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:32:22 2019

@author: yujzhang
"""

import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-np.pi, np.pi, 1000)

cos_y = np.cos(x) / 2
sin_y = np.sin(x)

mp.figure('Figure Object 1', figsize=(4, 3), dpi=120, facecolor='lightgray')
mp.xlabel('x', fontsize=12)
mp.ylabel('y', fontsize=12)
mp.tick_params(labelsize=8)
mp.tight_layout()
mp.plot(x, cos_y, c='dodgerblue',
        label=r'$y=\frac{1}{2}cos(x)$')
mp.show()