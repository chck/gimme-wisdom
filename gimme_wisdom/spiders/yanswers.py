# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class Answer(scrapy.Item):
    answer: str = scrapy.Field()


class YanswersSpider(scrapy.Spider):
    name = 'yanswers'
    allowed_domains = ['detail.chiebukuro.yahoo.co.jp']
    base_url = 'http://detail.chiebukuro.yahoo.co.jp/qa/question_detail'

    def __init__(self, qid, *args, **kwargs):
        super(YanswersSpider, self).__init__(*args, **kwargs)
        self.qid = qid
        self.start_urls = [
            '{}/q{}'.format(self.base_url, qid)
        ]

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')

        # best answer is in only first page
        if '?page=' not in response.url:
            best_answer = soup.find('div', class_='mdPstd mdPstdBA othrAns clrfx').find('p', 'queTxt').text
            yield Answer(answer=best_answer)

        # other answer
        for div in soup.find_all('div', class_='othrAns clrfx'):
            answer = div.find('p', class_='queTxt').text
            yield Answer(answer=answer)

        # pagination
        next_page = soup.find('div', class_='mdPager').find('a', class_='aft')
        if not next_page:
            yield
        else:
            yield scrapy.Request(next_page['href'])
