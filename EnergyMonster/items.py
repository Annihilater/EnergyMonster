# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EnergymonsterItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ShopItem(scrapy.Item):
    totalBorrowDesc = scrapy.Field()
    totalReturnDesc = scrapy.Field()
    distance = scrapy.Field()
    shopId = scrapy.Field()
    shopNo = scrapy.Field()
    address = scrapy.Field()
    distanceDesc = scrapy.Field()
    shopImg = scrapy.Field()
    shopName = scrapy.Field()
    businessHours = scrapy.Field()
    hasCabinet = scrapy.Field()
    hasDesktop = scrapy.Field()
    totalBorrowNum = scrapy.Field()
    totalReturnNum = scrapy.Field()
    warehouseStatusPrompt = scrapy.Field()
