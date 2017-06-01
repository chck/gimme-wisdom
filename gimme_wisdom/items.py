# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QItem(scrapy.Item):
    """no question one answer
    """
    answer = scrapy.Field()


class QandAsItem(scrapy.Item):
    """one question many answers
    """
    answers = scrapy.Field()
    question = scrapy.Field()
    link = scrapy.Field()
