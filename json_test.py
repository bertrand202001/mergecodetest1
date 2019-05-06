#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 13:43:15 2019

@author: yujzhang
"""

import json

#Json格式的数组
jsarry = '[1,2,3,4]'

#数组-》列表

L = json.loads(jsarry)
print(type(L),L)

#json格式对象
jsobj = '{"city":"Auckland","name":"Grafton"}'

#对象-》字典
D = json.loads(jsobj)
print(type(D),D)

M = [1,2,3,4]
T = (1,2,3,4)
H = {"city":"Auckland"}

#Python 格式-》json格式
jsarray1 = json.dumps(L)
print(type(jsarray1),jsarray1)

jsarray2 = json.dumps(T)
print(type(jsarray2),jsarray2)

jsobj = json.dumps(H,ensure_ascii=False)
print(type(jsobj),jsobj)
