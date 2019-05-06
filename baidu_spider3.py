#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:54:15 2019

@author: yujzhang
"""

import urllib.request
import urllib.parse
import random
import time

class BaiduSpider:
    def __init__(self):
        self.header_list = [{"User-Agent":"User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 "},
                         {"User-Agent":"User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"},
                         {"User-Agent":"User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}]
        self.baseurl = "http://tieba.baidu.com/f?kw="
    
    def readPage(self,url):
        headers = random.choice(self.header_list)
        req = urllib.request.Request(url,headers=headers)
        res = urllib.request.urlopen(req,timeout=5)
        time.sleep(2)
        html = res.read().decode("utf-8")
        return html
    
    def writePage(self,path,filename,html):
        with open(path + filename,"w",encoding="utf-8") as f:
            f.write(html)
    
    def workOn(self):
        #主体程序
        name = input("请输入贴吧名：")
        begin = int(input("请输入起始页:"))
        end = int(input("请输入终止页:"))
    
        #对贴吧名name进行编码
        kw = {"kw":name}
        kw = urllib.parse.urlencode(kw)
        #拼接URL,并发送请求获取响应
        for i in range(begin,end+1):
            #拼接URL
            pn = (i-1)*50
            url = self.baseurl + kw + "&pn=" + str(pn)
            html = self.readPage(url)
            filename = "第" + str(i) + "页.html"
            path = "/Users/yujzhang/Desktop/spider_data"
            print("正在爬取第%d页" % i)
            self.writePage(path,filename,html)
            print("第%d页爬取成功" % i)
            print("*" * 30)
    
if __name__ == "__main__":
    spider = BaiduSpider()
    spider.workOn()