# -*- coding: utf-8 -*-
import scrapy


class JdspiderSpider(scrapy.Spider):
    name = 'jdspider'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    def parse(self, response):
        pass
