#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 19:13:29 2019

@author: yujzhang
"""

import requests
from lxml import etree
import pytesseract
import PIL import Image

url = "https://www.douban.com/"
res.encoding = "utf-8"
html = res.text

#先访问网站得到html

parseHtml = etree.HTML(html)

s = parseHtml.xpath('//img[@class="captcha_image"]/@src')[0]

#用xpath把延续横马图片的链接给拿出来


#访问验证码图片链接，得到好tml（字节流）
res = requests.get(s,headers=headers)
res.encoding = "utf-8"
html = res.content
#把图片保存到本地
with open("zhanshen.jpg","wb") as f:
    f.write(html)
#把图片转成字符串
image = Image.open("zhanshen.jpg")
s = pytesseract.image_to_string(image)
print(s)
#把字符串输入到验证码框中

driver = webdriver.PhantomJS()
driver.get(url)
driver.find_element_by_class_name("captcha-solution").sendKeys(s)
driver.save_screenshot("验证码输入.jpg")

driver.quit()