# -*- coding: utf-8 -*-
import scrapy
import json

class ImagespiderSpider(scrapy.Spider):
    name = 'imagespider'
    allowed_domains = ['capi.douyucdn.cn']

    baseUrl = "http://capi.douyucdn.cn/api/v1/getVerticalRoon?limit=20&offset="

    offset = 0
    start_urls = [baseUrl + str(offset)]

    def parse(self, response):
        #response为json格式，先把响应转化成python数据类型
        res = json.loads(response.text)["data"]
        if len(nickList) == 0:
            return
        for nick in res:
            item = DouyuItem()
            item["imgLink"] = nick["vertical_src"]
            item["nickName"] = nick["nickname"]
            item["nickCity"] = nick["nickCity"]
            yield item

        self.offset += 20
        yield scrapy.Request(self.baseUrl+str(self.offset),callback = self.parse)
      
