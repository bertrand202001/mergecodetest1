#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:23:48 2019

@author: yujzhang
"""

import requests

url = "http://www.baidu.com/"
headers = {"User-Agent":"Mozilla/5.0"}
#发送请求获取响应
response = requests.get(url,headers=headers)
#获取响应对象内容
#print(response.text)#获得字符串内容
#print(response.encoding)
#默认换回编码格式为： ISO-8859-1

response.encoding = "utf-8"
print(response.text)

#获取字节流
print(type(response.content))
#返回服务器响应码
print(response.status_code)

#返回数据URL
print(response.url)