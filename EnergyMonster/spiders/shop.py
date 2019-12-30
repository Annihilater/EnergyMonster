# -*- coding: utf-8 -*-
import json

import scrapy

from EnergyMonster.items import ShopItem
from EnergyMonster.settings import HEADERS


class ShopSpider(scrapy.Spider):
    name = 'shop'
    allowed_domains = ['wchat.enmonster.com']
    start_urls = ['http://wchat.enmonster.com/']

    def start_requests(self):
        url = "https://wchat.enmonster.com/applet/nss/search/v2"

        payload = {
            "latitude": "xxx",
            "longitude": "xxx",
            "locatedLatitude": "xxx",
            "locatedLongitude": "xxx",
            "platform": 1,
            "queryCabtAvailable": 1,
            "pageIndex": 3,
            "pageSize": 15,
            "hasCabinet": 1,
            "activityId": ""
        }
        x_sign = 'xxx'
        x_nonce = 'xxx'
        x_wx_token = 'xxx'
        x_mac = 'xxx'
        HEADERS.update({'X-SIGN': x_sign,
                        'X-NONCE': x_nonce,
                        'X-WX-TOKEN': x_wx_token,
                        'X-MAC': x_mac, })
        yield scrapy.Request(url=url, method='POST', headers=HEADERS, body=json.dumps(payload), callback=self.parse)

    def parse(self, response):
        r = json.loads(response.text)
        if r['msg'] == 'ok' and r['code'] == 0:
            data = r['data']
            if data['currentPage'] < data['totalPage']:
                # 请求下一页
                pass
            rows = data['rows']
            for row in rows:
                item = ShopItem()
                for field in item.fields:
                    try:
                        item[field] = row[field]
                    except NameError:
                        self.logger.debug('Field is not Defined' + field)
                yield item
        else:
            self.logger.debug('Request Failed!')
            print(json.loads(response.text))
