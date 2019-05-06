#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 19:14:14 2019

@author: yujzhang
"""

import requests
from lxml import etree


class BaiduImageSpider:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0"}
        self.baseurl = "http://tieba.baidu.com"
    
    #获取所有帖子URL列表
    def getPageUrl(self,params):
        res = requests.get(self.baseurl+"/f?",params=params)
        res.encoding = "utf-8"
        html = res.text
        #构建解析对象
        parseHtml = etree.HTML(html)
        #帖子链接裂脚
        t_list = parseHtml.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
        for t_link in t_list:
            self.getImageUrl(self.baseurl + t_link)
    
    
    #获取帖子中图片URL列表
    def getImageUrl(self,t_link):
        res = requests.get(t_link,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        #构造解析对象
        parseHtml = etree.HTML(html)
        img_list = parseHtml.xpath('//img[@class="BDE_Image"]/@src')
        
        for img_link in img_list:
            self.writeImage(img_link)
    
    
    #保存到本地
    def writeImage(self,img_link):
        res = requests.get(img_link,headers=self.headers)
        res.encoding = "utf-8"
        #得到字节流信息
        html = res.content
        
        #filename,img_link截取最后12位
        filename = img_link[-12:]
        
        with open("/Users/yujzhang/Desktop/spider_data/baidutiebaPic/" + filename,"wb") as f:
            f.write(html)
            print("%s 下载成功" % filename)
            
    def workOn(self):
        name = input("请输入贴吧名：")
        begin = int(input("请输入起始页："))
        end = int(input("请输入终止页："))
        
        for n in range(begin,end+1):
            pn = (n-1)*50
            params = {
                    "kw":name,
                    "pn":str(pn)
                    }
            
            self.getPageUrl(params)
    
if __name__ == "__main__":
    spider = BaiduImageSpider()
    spider.workOn()