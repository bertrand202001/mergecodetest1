# -*- coding: utf-8 -*-
import scrapy
from csdn.items import CsdnItem


class CsdnspiderSpider(scrapy.Spider):
    name = 'csdnspider'
    allowed_domains = ['blog.csdn.net']
    start_urls = ['https://blog.csdn.net/csdnsevenn/article/details/89464792']

    def parse(self, response):
        item = CsdnItem()
	
        item["name"] = response.xpath('//h1[@class="title-article"]/text()').extract()[0]
        item["time"] = response.xpath('//span[@class="time"]/text()').extract()[0]
        item["number"] = response.xpath('//span[@class="read-count"]/text()').extract()[0]
        yield item
