# -*- coding: utf-8 -*-
import scrapy
from SPguazi.items import SpguaziItem


class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['guazi.com']
    start_urls = ['http://guazi.com/']
    cookies = {}

    def parse(self, response):
        pass
