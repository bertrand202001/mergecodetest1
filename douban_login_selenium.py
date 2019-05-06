#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 19:21:20 2019

@author: yujzhang
"""

from selenium import webdriver
import time

#创建浏览器对象，发请求

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://www.douban.com/")
time.sleep(0.5)
#获取截图(验证码)
driver.save_screenshot("验证码.png")
#找用户名，密码，验证，登录豆瓣按钮
ulogin = driver.find_element_by_xpath('//div[@class="account-body-tabs"]/ul[@class="tab-start"]/li[2]')
ulogin.click()
time.sleep(0.5)

uname = driver.find_element_by_name("form_email")
uname.send_keys("309435365@qq.com")

pwd = driver.find_element_by_name("form_password")
pwd.send_keys("zhanshen001")

key = input("请输入验证码：")
yzm = driver.find_element_by_id("captcha_field")
yzm.send_keys(key)
driver.save_screenshot("完成.png")

login = driver.find_element_by_class_name("bn-submit")
login.click()
time.sleep(1)
driver.save_screenshot("登录成功.png")
#关闭浏览器
driver.quit()