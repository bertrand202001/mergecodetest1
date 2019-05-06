#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 15:22:30 2019

@author: yujzhang
"""

#导入selenium库中的webdriver接口
from selenium import webdriver

#创建phantomjs浏览器对象
driver = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs")
#发请求
driver.get("http://www.baidu.com/")
r = driver.page_source.find("kw")
print(r)
#获取网页截屏
#driver.save_screenshot("/Users/yujzhang/Desktop/baidu.png")
#print("图片保存成功")
#关闭
driver.quit()