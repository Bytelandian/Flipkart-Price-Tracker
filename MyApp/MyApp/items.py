# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyappItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    description=scrapy.Field()
    price=scrapy.Field()
    rating=scrapy.Field()
    usersrated=scrapy.Field()
    url=scrapy.Field()
    date=scrapy.Field()
    time=scrapy.Field()
    review=scrapy.Field()
