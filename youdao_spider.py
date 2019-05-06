#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:43:25 2019

@author: yujzhang
"""

import urllib.request
import urllib.parse
import json

# 请输入你要翻译的内容
key = input("请输入要翻译的内容：")
data = {"i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15534857093853",
        "sign": "9bc5c047df3c1ae447655ac81e4aa682",
        "ts": "1553485709385",
        "bv": "554534c162ce5bb7423851b9099b0959",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
        "typoResult": "false"
        }
#字符串转字节流
data = urllib.parse.urlencode(data)
data = bytes(data,"utf-8")

#发请求，获取响应
#url为POST的地址
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 "}
#此处data为form表单数据，为bytes数据类型
req = urllib.request.Request(url,data=data,headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode("utf-8")
#with open("/Users/yujzhang/Desktop/spider_data/test.html","w",encoding="utf-8") as f:
#    f.write(html)
#print(html)

r_dict = json.loads(html)
#print(r_dict)
print(r_dict['translateResult'][0][0]['tgt'])

