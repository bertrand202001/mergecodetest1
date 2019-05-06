#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:27:56 2019

@author: yujzhang
"""

from bs4 import BeautifulSoup
import requests

#html = '<div id="test">aaa</div>'

#创建解析对象
#soup = BeautifulSoup(html,'lxml')
#查找节点
#r_list = soup.find_all(id="test")
#print(r_list)
#for r in r_list:
#    print(r.get_text())

url = "https://www.qiushibaike.com/text/"
headers = {"User-Agent":"Mozila/5.0"}


res = requests.get(url,headers=headers)
res.encoding = "utf-8"
html = res.text

soup = BeautifulSoup(html,'lxml')
r_list = soup.find_all("div",attrs={"class":"content"})

for r in r_list:
    print(r.span.get_text().strip())
    print("*" * 30)