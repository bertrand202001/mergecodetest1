#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:54:21 2019

@author: yujzhang
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#创建浏览器对象，发请请求
driver = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs")
driver.get("http://www.baidu.com")

#百度搜索框输入python
kw = driver.find_element_by_id("kw")
kw.send_keys("python")
driver.save_screenshot("01_python.png")

#全选，剪切，粘贴，清空搜索框，
kw = driver.find_element_by_id("kw")
kw.send_keys(Keys.CONTROL,'a')
driver.save_screenshot("02_python.png")

kw = driver.find_element_by_id("kw")
kw.send_keys(Keys.CONTROL,'x')
driver.save_screenshot("03_python.png")

kw = driver.find_element_by_id("kw")
kw.send_keys(Keys.CONTROL,'v')
driver.save_screenshot("04_python.png")

kw = driver.find_element_by_id("kw")
kw.clear()
driver.save_screenshot("05_python.png")

kw = driver.find_element_by_id("kw")
kw.send_keys("danei")
driver.save_screenshot("06_python.png")

kw = driver.find_element_by_id("kw")
kw.send_keys(Keys.ENTER)
driver.save_screenshot("07_python.png")