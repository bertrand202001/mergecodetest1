#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 00:06:45 2019

@author: yujzhang
"""

import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-np.pi, np.pi, 1000)
cos_y = np.cos(x) / 2
sin_y = np.sin(x)
xo = np.pi * 3 / 4
yo_cos = np.cos(xo) / 2
yo_sin = np.sin(xo)

mp.xlim(x.min() * 1.2, x.max() * 1.2)
mp.ylim(sin_y.min() * 1.2, sin_y.max() * 1.2)
mp.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi * 3 / 4, np.pi],[r'$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$' , r'$\frac{3\pi}{4}$', r'$\pi$'])
mp.yticks([-1, -0.5, 0.5, 1])

ax = mp.gca()
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

mp.plot(x, cos_y, linestyle='--', linewidth=1, color='red', label='r$y=\frac{1}{2}cos(x)$')
mp.plot(x, sin_y, linestyle=':', linewidth=3, color='green', label='r$y=sin(x)$')
mp.plot([xo,xo], [yo_cos, yo_sin], linewidth=0.5)
mp.scatter([xo, xo],[yo_cos, yo_sin], marker='*', s=120, edgecolor='dodgerblue', facecolor='white')
mp.legend(loc='lower right')
mp.show()