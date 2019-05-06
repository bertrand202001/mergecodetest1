#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:20:59 2019

@author: yujzhang
"""

import numpy as np
import matplotlib.pyplot as mp

t = np.linspace(0, 8 * np.pi, 1001)
r_spiral = 0.8 * t

mp.figure('Polar', facecolor='lightgray')
mp.gca(projection='polar')
mp.title('Polar', fontsize=20)
mp.xlabel(r'$\theta$', fontsize=14)
mp.ylabel(r'$\rho$', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
#函数值=f(自变量)
#垂直坐标=f(水平坐标)
#极径=f(极角)
#水平坐标->自变量->极角
#垂直坐标->函数值->极径
mp.plot(t, r_spiral, c='dodgerblue', label=r'$\rho=0.8\theta$')
mp.legend()
mp.show()