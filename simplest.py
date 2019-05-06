#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 15:25:20 2019

@author: yujzhang
"""

#import requests
#response = requests.get("http://www.sina.com.cn")
#response.encoding = 'utf-8'
#print(response.text)
#with open('sina.html', 'w') as f:
#    f.write(response.text)

from urllib import request
req = request.Request("http://www.sina.com.cn")
response = request.urlopen(req)
print(response.read().decode("utf-8"))