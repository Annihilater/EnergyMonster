#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/28 3:51 下午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : mongo.py
import pymongo

mongo_uri = '127.0.0.1'
mongo_db = 'EnergyMonster'
mongo_collection = 'ShopItem'


class MongoDBClient:
    """
    MongoDB Client
    """

    def __init__(self):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.name = mongo_collection

    def save_to_mongodb(self, rows: list):
        """
        存入 MongoDB
        :param rows:
        :return:
        """
        for row in rows:
            if not self.db[self.name].find_one({'shopId': row['shopId']}):
                self.db[self.name].insert(row)
