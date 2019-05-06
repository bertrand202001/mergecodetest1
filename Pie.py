#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:49:25 2019

@author: yujzhang
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 12:48:33 2019

@author: yujzhang
"""

import numpy as np
import matplotlib.pyplot as mp

values = [30, 25, 22, 36, 21]
spaces = [0.01, 0.01, 0.01, 0.01, 0.01]
labels = ['Python', 'JavaScript',
          'C++', 'Java','PHP']

colors = ['dodgerblue', 'orangered',
          'limegreen', 'violet', 'gold']

apples = np.array([
        30, 25, 22, 36, 21, 29, 20, 24, 33, 19, 27, 15])

oranges = np.array([
        24, 33, 19, 27, 35, 20, 15, 27, 20, 32, 20, 22])


mp.figure('Pie', facecolor='lightgray')
mp.title('Pie', fontsize=20)
mp.pie(values, spaces, labels, colors, '%d%%')
#等轴比例
mp.axis('equal')

mp.show()