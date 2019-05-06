#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 22:17:44 2019

@author: yujzhang
"""

import hashlib

def hashStr(strInfo):
    """
    对字符串进行hash,得到一个16进制的指纹数据
    """
    h = hashlib.md5()
    h.update(strInfo.encode("utf-8"))
    return h.hexdigest()

#print(hashStr("hello"))
#print(hashStr("hello1"))

CHUNKSIZE = 2048
def hashFile(fileName):
    """
    对文件进行hash，得到一个16进制的指纹数据
    """
    h = hashlib.sha256()
    with open(fileName,"rb") as f:
        while True:
            chunk = f.read(CHUNKSIZE)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

print(hashFile("simplest.py"))



