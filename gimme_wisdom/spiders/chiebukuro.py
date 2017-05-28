# -*- coding: utf-8 -*-
import scrapy


class ChiebukuroSpider(scrapy.Spider):
    name = 'chiebukuro'
    allowed_domains = ['detail.chiebukuro.yahoo.co.jp']
    start_urls = ['http://detail.chiebukuro.yahoo.co.jp/']

    def parse(self, response):
        pass
