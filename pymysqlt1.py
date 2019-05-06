#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:48:17 2019

@author: yujzhang
"""
import pymysql

db = pymysql.connect("localhost","root","123456",charset="utf8")

cursor = db.cursor()

cursor.execute("create database spiderdb2")
cursor.execute("use spiderdb2")
cursor.execute("create table t2(id int)")
ins = "insert into t1 value(%s)"
cursor.execute(ins,[1])
cursor.execute(ins,[2])

db.commit()

cursor.close()

db.close()
