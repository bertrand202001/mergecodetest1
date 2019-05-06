#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 17:19:46 2019

@author: yujzhang
"""

from __future__ import unicode_literals
import numpy as np

a = np.arange(1,3)
print(a)

b = np.array([[1,2,3],[4,5,6]])
print(b, b.shape)
c = np.array([np.arange(1,4),np.arange(4,7),np.arange(7,10)])
print(c,c.shape)

d = np.arange(1,10)
#print(type(d[1]))

e = d.astype(float)
print(e.dtype)

f = d.astype(str)
print(f.dtype)

g = np.array([[10,20,30],[40,50,60]])
print(g.shape, g.size, len(g))

h = g.reshape((6,))
print(h.shape, h.size, len(h))

i = g.reshape((3,2))
print(i.shape, i.size, len(i))

k = np.arange(1,25).reshape((2,3,4))
print(k)
print("****************")
l = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(l, l.shape)
print(l[0])
print(l[0][0])
print(l[0][0][0])
print("****************")
for i in range(l.shape[0]):
    for j in range(l.shape[1]):
        for k in range(l.shape[2]):
            print(l[i, j, k])
print("****************")


m = np.array([('123',[4,5,6])],dtype='U3, 3i4')
print(m[0]['f0'],m[0]['f1'])

print("****************")
n = np.array([('123',[4,5,6])],dtype = [('fa', np.str_, 3),('fb', np.int32, 3)])  
print(n[0]['fa'], n[0]['fb'])

print("****************")
o = np.array([('123',[4,5,6])],dtype={'names':['fa', 'fb'],'formats':['U3','3i4']})
print(o[0]['fa'],o[0]['fb'])

p = np.array([('123',[4,5,6])],dtype={'fa':('U3',0),'fb':('3i4',16)})
print(p[0]['fa'],p[0]['fb'], p.itemsize)
print("****************")

q = np.array([0x1234],dtype=('>u2',{'lo':('u1',0),'hi':('u1',1)}))
print('{:x}'.format(q[0]))  
print('{:x} {:x}'.format(q['lo'][0],q['hi'][0]))  

#切片
print("====================")
aa = np.arange(1,10)
print(aa)
print(aa[:3])
print(aa[3:6])
print(aa[6:])
print(aa[::-1])#倒序
print(aa[:-4:-1])
print(aa[-4:-7:-1])
print(aa[-7::-1])
print(aa[::])
print(aa[:])
print(aa[...])
print(aa[1::3])
print(aa[2::3])#【起始：终止：步长】
print("======================")
bb = np.arange(1,25).reshape(2,3,4)
print(bb)
print(bb[:, 0, 0])#[页，行，列]
print(bb[0])
print(bb[0, :, :])
print(bb[0, ...])
print(bb[0,1, ::2])#[页，行，步长]
print(bb[...,1])
print(bb[:,1])
print(bb[0,:,-1])
print(bb[0,1,1::2])
print(bb[0,::-1,-1])
print(bb[-1,1:, 2:])