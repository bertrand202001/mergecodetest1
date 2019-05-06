#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:09:55 2019

@author: yujzhang
"""
#创建编译对象，贪婪匹配
#re.S作用：使.能够匹配\n在内的所有内容
import re

s = """<div><p>we are family</div></p><div><p>running man</div></p>"""
#贪婪匹配： .*  非贪婪匹配：.*?
p = re.compile('<div><p>.*</div></p>')
p = re.compile('<div><p>.*?</div></p>')
#匹配字符串s
r = p.findall(s)
print(r)