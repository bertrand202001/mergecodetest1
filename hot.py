#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:10:33 2019

@author: yujzhang
"""

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

n = 1000
#网格化
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))

print(x.shape, y.shape)

z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

mp.figure('Hot', facecolor='lightgray')
mp.title('Hot', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.contourf(x, y, z, 8, cmap='jet')
#绘制热成像图
mp.imshow(z, cmap='jet', origin='low')
mp.colorbar().set_label('z', fontsize=14)
mp.show()