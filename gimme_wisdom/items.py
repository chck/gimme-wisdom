# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnswerItem(scrapy.Item):
    atitle: str = scrapy.Field()
    adetail: str = scrapy.Field()


class QandAsItem(scrapy.Field):
    """one question many answers
    """
    url: str = scrapy.Field()
    category: str = scrapy.Field()
    qtitle: str = scrapy.Field()
    qdetail: str = scrapy.Field()
    answers: list = list(AnswerItem())
