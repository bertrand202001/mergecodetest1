#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:18:09 2019

@author: yujzhang
"""

import re

#先按照整体匹配出来，然后再匹配（）中的
#如果有2个或者多个（），则以元组的方式取显示
#['A B','C D']

s = "A B C D"
p1 = re.compile('\w+\s+\w+')
print(p1.findall(s))

p2 = re.compile('(\w+)\s+\w+')
#第一步：['A B','C D']
#第二步： ['A','C']
print(p2.findall(s))

p3 = re.compile('(\w+)\s+(\w+)')
#第一步：['A B','C D']
#第二步：[('A','B'),('C','D')]
print(p3.findall(s))