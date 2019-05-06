#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 21:31:12 2019

@author: yujzhang
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 19:14:14 2019

@author: yujzhang
"""

import requests
from lxml import etree
import pymysql


class QiuShiSpider:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0"}
        self.baseurl = "https://www.qiushibaike.com/text/"
        self.page = 1
        self.db = pymysql.connect("localhost","root","123456",charset="utf8")
        self.cursor = self.db.cursor()
    
    #获取所有帖子URL列表
    def getPageUrl(self,page):
        res = requests.get(self.baseurl+"page/"+str(page),headers = self.headers)
        res.encoding = "utf-8"
        html = res.text
        #构建解析对象
        parseHtml = etree.HTML(html)
        #获取用户名，段子，好笑和评论信息
        element_list = []
        base_list = parseHtml.xpath('//div[contains(@id,"content-left")]/div')
        for base in base_list:
            user_name = base.xpath('./div[1]/a[2]/h2|./div[1]/span[2]/h2')[0].text
            content = base.xpath('./a[1]//span[1]')[0].text
            laughing = base.xpath('.//span[@class="stats-vote"]/i')[0].text
            comment = base.xpath('.//span[@class="stats-comments"]/a/i')[0].text
            element_list.append({
                    "username":user_name,
                    "content":content,
                    "laughing":laughing,
                    "comment":comment
                    })
        print(element_list)
    
        self.writeToMysql(element_list)
              
    
    #写入本地数据库
    def writeToMysql(self,element_list):
        ins = "insert into qiushi2(username,content,laughing,comment) values(%s,%s,%s,%s)"
        self.cursor.execute("use spiderdb0418")
        for el in element_list:
            L = [el['username'].strip(),el['content'].strip(),el['laughing'].strip(),el['comment'].strip()]
            self.cursor.execute(ins,L)
            self.db.commit()
            print("成功写入数据库")
            
    def workOn(self):
        begin = int(input("请输入起始页："))
        end = int(input("请输入终止页："))
        
        for n in range(begin,end+1):
            page = n        
            self.getPageUrl(page)
    
if __name__ == "__main__":
    spider = QiuShiSpider()
    spider.workOn()