# -*- coding: utf-8 -*-
# Author:leali
# Description:
# Version:v1.0
# Date:2019-01-01 04:38 PM

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
           'http://quotes.toscrape.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags > a.tag::text').extract(),
            }
        # For <a> elements there is a shortcut: response.follow uses their href attribute automatically
        for href in response.css('li.next a'):
            yield response.follow(href, callback=self.parse)
        # next_page = response.css('li.next > a::attr(href)').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
