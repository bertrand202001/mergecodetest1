#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 23:55:03 2019

@author: yujzhang
"""

import numpy as np

a = np.array([[1+1j, 2+4j, 3+7j],[4+2j, 5+5j, 6+8j],[7+3j, 8+6j, 9+9j]])


print(a.shape)
print(a.dtype)
print(a.size)
print(a.ndim)
print(a.size)
print(a.itemsize)
print(a.nbytes)
print(a.real, a.imag, sep='\n')
print(a.T)

print([elem for elem in a.flat])
b = a.tolist()
print(b)

