#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 14:08:58 2019

@author: yujzhang
"""

import requests
import json
import csv


#url要写get请求的url
url = "https://movie.douban.com/j/chart/top_list?"
headers = {"User-Agent":"Mozilla/5.0"}
L2 = ["剧情","喜剧"]
tp_list = {"剧情":"11","喜剧":"24"}
tp = input("请输入电影类型：")

if tp in L2:
    num = input("请输入要爬取的数量：")
    film_type = tp_list[tp]
        
    params = {
            "type":film_type,
            "interval_id":"100:90",
            "action":"",
            "start":"0",
            "limit":num}
    
    res = requests.get(url,params=params,headers=headers)
    res.encoding = "utf-8"
    html = res.text
    print(html)
    
    #数组转列表
    html = json.loads(html)
    for item in html:
        name = item['title']
        score = item["rating"]
        with open("douban.csv","a",newline="") as f:
            writer = csv.writer(f)
            L = [name,score]
            writer.writerow(L)
else:
    print("您输入的类型不存在！")
