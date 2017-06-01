# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from typing import List
from gimme_wisdom.items import AnswerItem, QandAsItem


class NkidsSpider(scrapy.Spider):
    name = 'nkids'
    allowed_domains = ['kids.nifty.com']
    base_url = 'http://kids.nifty.com'
    start_urls = ['{}/cs/catalog/kids_soudan/idx/cnt_idx/1.htm'.format(base_url)]

    def parse(self, response):
        """parse page list
        """
        soup = BeautifulSoup(response.body, 'lxml')

        # if 'catalog' in response.url:
        #     enqueue a page which has question list
        # yield scrapy.Request(response.url, callback=self.parse_questions)
        # elif 'kuchikomi' in response.url:
        #     enqueue a page which has one question page
        # yield scrapy.Request(response.url, callback=self.parse_answers)

        # enqueue a page which has question list
        yield scrapy.Request(response.url, callback=self.parse_questions)

        # pagination
        maybe_next_page: List(str) = self._find_next_page(soup)
        if not maybe_next_page:
            yield
        else:
            yield scrapy.Request(self._url(maybe_next_page[-1]['href']))

    def parse_questions(self, response):
        """parse question list
        """
        soup = BeautifulSoup(response.body, 'lxml')

        for q in soup.find(id='questionArea').find_all('li'):
            _ = q.find('span', class_='ttl')
            yield scrapy.Request(self._url(q.a['href']),
                                 meta={
                                     'qtitle': _.em.text,
                                     'category': _.img['alt'],
                                 },
                                 callback=self.parse_question)

    def parse_question(self, response):
        """parse one question page
        """
        soup = BeautifulSoup(response.body, 'lxml')

        self._find_next_page(soup)

        # qtitle = soup.find('div', id='soudanContents').find('span', class_='ttl').em.text
        # return QandAsItem(url=response.url, qtitle=qtitle, answers=[Answer(atitle='xxx')])

        # print('==========================')
        # print(response.meta)
        # print('==========================')

        # yield scrapy.Request()
        # yield scrapy.Request(self._url('x'), callback=self.parse)

        """
        ここでparse_answersの返り値を待って、QandAsItemに詰めてreturnしたい
        """
        def xxx(maybe_next_page):
            """未完成で力尽きた再帰関数
            """
            if not maybe_next_page:
                yield
            else:
                maybe_next_page: List(str) = self._find_next_page(soup)
                yield xxx(maybe_next_page)

        maybe_next_page: List(str) = self._find_next_page(soup)
        if not maybe_next_page:
            yield
        else:
            yield scrapy.Request(self._url(maybe_next_page[-1]['href']))

        yield from self.parse_answers(url)

    def parse_answers(self, url):
        """parse answer list
        """
        soup = BeautifulSoup(response.body, 'lxml')
        #     print('----------------')
        #     print(response.meta)
        #     print('----------------')

        answers: List(AnswerItem) = []
        for a in soup.find(id='answerArea').find_all('li'):
            _ = a.find('span', class_='ttl')
            atitle = _.em.text
            adetail = _.span.text
            answers.append(AnswerItem(atitle=atitle, adetail=adetail))
        yield answers

    def _url(self, path: str) -> str:
        return self.base_url + path

    def _find_next_page(self, soup: BeautifulSoup) -> List(str):
        maybe_next_page = soup.find('div', class_='paging mgT20').find_all('a', class_='Pre')
        return [page for page in maybe_next_page if page.text == 'つぎへ']
