# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QItem(scrapy.Item):
    """no question one answer
    """
    answer: str = scrapy.Field()


class QandAsItem(scrapy.Item):
    """one question many answers
    """
    answers: list = scrapy.Field()
    question: str = scrapy.Field()
    link: str = scrapy.Field()
