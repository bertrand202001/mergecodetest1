#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:53:47 2019

@author: yujzhang
"""

from selenium import webdriver
from lxml import etree
import time

#把chrome设置成无界面浏览器
opt = webdriver.ChromeOptions()
#opt.set_headless()


# 创建浏览器对象,发请求
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://www.douyu.com/directory/all")
time.sleep(3)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)

#循环
while True:
    #解析（driver.page_source）
    #获取主播名称和观众人数
    
    parseHtml = etree.HTML(driver.page_source)
    names = parseHtml.xpath('//section[@class="layout-Module js-ListContent"]//ul[@class="layout-Cover-list"]/li//h2/text()')
    numbers = parseHtml.xpath('//section[@class="layout-Module js-ListContent"]//ul[@class="layout-Cover-list"]/li//span[@class="DyListCover-hot"]/text()')
    
    for name,number in zip(names,numbers):
        print("主播名称：%s 观众人数：%s" %(name,number))
    #print(driver.find_element_by_xpath('//li[contains(.,"下一页")]').get_attribute('aria-disabled'))
    if driver.find_element_by_xpath('//li[contains(.,"下一页")]').get_attribute('aria-disabled') == 'false':
        #driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        driver.find_element_by_xpath("//span[contains(.,'下一页')]").click()
        time.sleep(2)
    else:
        break
driver.quit()
    #条件判断是否需要点击下一页
    #如果能点，点击
    #如果不能点，break

