#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:23:23 2019

@author: yujzhang
"""

import re
import requests

class NoteSpider:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0"}
        self.url = "http://code.tarena.com.cn/"
        self.auth = ("tarenacode","code_2013")
    
    def getParsePage(self):
        res = requests.get(self.url, 
                           headers=self.headers,
                           auth=self.auth,
                           timeout=3)
        
        res.encodeing = "utf-8"
        html = res.text
        p = re.compile('<a href=".*?>(.*?)</a>',re.S)
        r_list = p.findall(html)
        self.writePage(r_list)
    
    def writePage(self,r_list):
        with open("test.txt","a") as f:
            for r_str in r_list:
                f.write(r_str + "\n\n")
                
        print("写入成功")
    
if __name__=="__main__":
    spider = NoteSpider()
    spider.getParsePage()