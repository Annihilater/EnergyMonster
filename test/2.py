#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/27 2:09 下午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 2.py
import json

p = {
    "latitude": "xxxxx",
    "longitude": "xxxxxx",
    "locatedLatitude": "xxxxx",
    "locatedLongitude": "xxxxx",
    "platform": 1,
    "queryCabtAvailable": 1,
    "pageIndex": 3,
    "pageSize": 15,
    "hasCabinet": 1,
    "activityId": ""
}
d = str(p)
e = json.dumps(p)
print(d)
print(e)
