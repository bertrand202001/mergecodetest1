#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 23:37:09 2019

@author: yujzhang
"""

import urllib.request
import re
import csv

class MaoyanSpider:
    def __init__(self):
        self.baseurl = "https://maoyan.com/board/4?offset="
        self.headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)"}
        self.page = 1
    
    #下载页面
    def loadPage(self,url):
        print("loding page...")
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        self.parsePage(html)
        
    #解析页面
    def parsePage(self,html):
        print("parsing page...")
        p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?releasetime">(.*?)</p>',re.S)
        r_list = p.findall(html)
        print(r_list)
        #[("什么动物。。。","海豹")，（），（），（）]
        self.writePage(r_list)
    
    #保存页面
    def writePage(self,r_list):
        print("writing page...")
        for r_tuple in r_list:
            with open("/Users/yujzhang/Desktop/spider_data/maoyan.csv","a",newline="",encoding="utf-8") as f:
                #创建写入对象
                writer = csv.writer(f)
                #L = list(r_tuple)
                L = [r_tuple[0].strip(),r_tuple[1].strip(),r_tuple[2].strip()]
                writer.writerow(L)
                    
    
    def workOn(self):
        #self.loadPage(self.baseurl)
        with open("/Users/yujzhang/Desktop/spider_data/maoyan.csv","a",newline="",encoding="utf-8") as f:
            #创建写入对象
            writer = csv.writer(f)
            writer.writerow(["电影名称","主演","上映时间"])
        while True:
            c = input("是否继续(y/n):")
            if c.strip().lower() == "y":
                self.offset = (self.page-1)*10
                url = self.baseurl + str(self.offset)
                print(url)
                self.loadPage(url)
                self.page += 1
            else:
                print("爬取结束，谢谢使用！")
                break
                   
    
if __name__ == "__main__":
    spider = MaoyanSpider()
    spider.workOn()
    