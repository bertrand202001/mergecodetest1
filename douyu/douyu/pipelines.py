# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import scrapy

class DouyuImagePipeline(ImagesPipeline):
    #1.获取图片链接,此方法名不能变，是继承的
    def get_media_requests(self,item,info):
        imageLink = item["imgLink"]
    
    #2.向图片链接发请求,响应会保存在settings.py中的IMAGE_STORE路径中
        yield scrapy.Request(imageLink)

class DouyuPipeline(object):
    def process_item(self, item, spider):
        return item
