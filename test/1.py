#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/27 10:55 上午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 1.py


row = {
    "totalBorrowDesc": "可使用",
    "totalReturnDesc": "可归还",
    "distance": "138.36m",
    "shopId": 2342342,
    "shopNo": "xxxx",
    "address": "xxxx",
    "distanceDesc": "138m",
    "shopImg": "http://energymonster-public.oss-cn-shanghai.aliyuncs.com/143243243",
    "shopName": "xxxxxxxx）",
    "businessHours": "10:00-22:00",
    "hasCabinet": 1,
    "hasDesktop": 0,
    "totalBorrowNum": 4,
    "totalReturnNum": 1,
    "warehouseStatusPrompt": "仓口即将还满，如要还宝请尽快前往"
}

# print(row.keys())
result = {}
for field in row.keys():
    print(f'{field} = scrapy.Field()')
