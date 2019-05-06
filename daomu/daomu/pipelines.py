# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from daomu import settings
import pymongo

class DaomuPipeline(object):
    def process_item(self, item, spider):
        print("=================")
        print(item["bookName"])
        print(item["bookTitle"])
        print(item["zhName"])
        print(item["zhNum"])
        print(item["zhLink"])
        print("=================")


class DaomumongoPipline(object):
    def __init__(self):
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT
        dbName = settings.MONGODB_DBNAME
        docName = settings.MONGODB_DOCNAME

        conn = pymongo.MongoClient(host=host,port=port)
        db = conn.dbName
        self.myset = db.docName
   
    def process_item(self, item, spider):
        #把item对象转为字典
        bookInfo = dict(item)
        self.myset.insert(bookInfo)
        print("存入数据库成功")
        #return item
