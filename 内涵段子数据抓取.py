#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:12:14 2019

@author: yujzhang
"""

import urllib.request
import re

class NeihanSpider:
    def __init__(self):
        self.baseurl = "http://www.2345.com/"
        self.headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)"}
        self.page = 1
    
    #下载页面
    def loadPage(self,url):
        print("loding page...")
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("gbk")
        self.parsePage(html)
        
    #解析页面
    def parsePage(self,html):
        print("parsing page...")
        p = re.compile('<span class="table_left">(.*?)</span>',re.S)
        r_list = p.findall(html)
        print(r_list)
        #[("什么动物。。。","海豹")，（），（），（）]
        self.writePage(r_list)
    
    #保存页面
    def writePage(self,r_list):
        print("writing page...")
        for r_tuple in r_list:
            print(r_tuple)
            with open("/Users/yujzhang/Desktop/spider_data/jizhuanwan.txt","a",encoding="utf-8") as f:
                f.write(r_tuple.strip() + "\n")
                    
    
    def workOn(self):
        #self.loadPage(self.baseurl)
        while True:
            c = input("是否继续(y/n):")
            if c.strip().lower() == "y":
                self.page +=1
                url = self.baseurl + "jzw/" + str(self.page) + ".htm"
                print(url)
                self.loadPage(url)
            else:
                print("爬取结束，谢谢使用！")
                break
                   
    
if __name__ == "__main__":
    spider = NeihanSpider()
    spider.workOn()
    