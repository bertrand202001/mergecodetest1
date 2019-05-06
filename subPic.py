#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:48:40 2019

@author: yujzhang
"""

import matplotlib.pyplot as mp

mp.figure('Subplot', facecolor='lightgray')
mp.subplot(221)
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '1', ha='center', va='center', size=36, alpha=0.5)


mp.subplot(222)
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '2', ha='center', va='center', size=36, alpha=0.5)


mp.subplot(223)
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '3', ha='center', va='center', size=36, alpha=0.5)

mp.subplot(224)
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '4', ha='center', va='center', size=36, alpha=0.5)
mp.show()