# -*- coding: utf-8 -*-
import scrapy
from tengxun.items import TengxunItem

class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'
    allowed_domains = ['hr.tencent.com']

    url = "https://hr.tencent.com/position.php?&start="
    offset = 0

    start_urls = [url + str(offset)]
    def parse(self, response):
        for i in range(0,3220,10):
            yield scrapy.Request(self.url + str(i), callback=self.parseHtml)

    def parseHtml(self,response):
        base_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        for base in base_list:
            item = TengxunItem()
            item['name'] = base.xpath('./td/a/text()').extract()[0]
            item['type'] = base.xpath('./td[2]/text()').extract()[0]
            item['location'] = base.xpath('./td[4]/text()').extract()[0]
            item['publishTime'] = base.xpath('./td[5]/text()').extract()[0]
            yield item
