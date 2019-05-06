#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 22:33:27 2019

@author: yujzhang
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 23:37:09 2019

@author: yujzhang
"""

import requests
import re
import csv
import pymysql

class LianJiaSpider:
    def __init__(self):
        self.baseurl = "https://bj.lianjia.com/ershoufang/pg"
        self.headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)"}
        self.page = 1
        self.db = pymysql.connect("localhost","root","123456",charset="utf8")
        self.cursor = self.db.cursor()
    
    #下载页面
    def loadPage(self,url):
        print("loding page...")
        res = requests.get(url,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parsePage(html)
        
    #解析页面
    def parsePage(self,html):
        print("parsing page...")
        p = re.compile('<div class="houseInfo">.*?data-el="region">(.*?)</a>.*?<div class="totalPrice"><span>(.*?)</span>',re.S)
        r_list = p.findall(html)
        print(r_list)
        #[("什么动物。。。","海豹")，（），（），（）]
        self.writePage(r_list)
        self.writeToMysql(r_list)
    
    #保存页面
    def writePage(self,r_list):
        print("writing page...")
        for r_tuple in r_list:
            with open("/Users/yujzhang/Desktop/spider_data/lianjia.csv","a",newline="",encoding="utf-8") as f:
                #创建写入对象
                writer = csv.writer(f)
                #L = list(r_tuple)
                L = [r_tuple[0].strip(),r_tuple[1].strip()+"万"]
                writer.writerow(L)
                
                
    #保存数据到mysql
    def writeToMysql(self,r_list):
        ins = "insert into lianjia(name,price) values(%s,%s)"
        self.cursor.execute("use spiderdb0418")
        for r_tuple in r_list:
            L = [r_tuple[0].strip(),float(r_tuple[1].strip())*10000]
            self.cursor.execute(ins,L)
            self.db.commit()        
    
    def workOn(self):
        #self.loadPage(self.baseurl)
        with open("/Users/yujzhang/Desktop/spider_data/lianjia.csv","a",newline="",encoding="utf-8") as f:
            #创建写入对象
            writer = csv.writer(f)
            writer.writerow(["小区名称","总价"])
        while True:
            c = input("是否继续(y/n):")
            if c.strip().lower() == "y":
                url = self.baseurl + str(self.page)
                print(url)
                self.loadPage(url)
                self.page += 1
            else:
                self.cursor.close()
                self.db.close()
                print("爬取结束，谢谢使用！")
                break
                   
    
if __name__ == "__main__":
    spider = LianJiaSpider()
    spider.workOn()
        