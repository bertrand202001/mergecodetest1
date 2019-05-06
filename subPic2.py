#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:57:56 2019

@author: yujzhang
"""

import matplotlib.pyplot as mp
import matplotlib.gridspec as mg

mp.figure('Grid', facecolor='lightgray')
gs = mg.GridSpec(3, 3)
mp.subplot(gs[0, :2])
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '1', ha='center', va='center', size=36, alpha=0.5)

mp.subplot(gs[1:, 0])
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '2', ha='center', va='center', size=36, alpha=0.5)

mp.subplot(gs[2, 1:])
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '3', ha='center', va='center', size=36, alpha=0.5)

mp.subplot(gs[:2, 2])
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '4', ha='center', va='center', size=36, alpha=0.5)
mp.show()