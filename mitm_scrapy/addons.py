#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/28 1:52 下午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : addons.py
import json

from mitmproxy import ctx, http, command

from mongo import MongoDBClient
from my_proxy import get_proxy


class EnergyMonster:
    def __init__(self):
        self.host = 'wchat.enmonster.com'
        self.search_url = 'https://wchat.enmonster.com/applet/nss/search/v2'

    def request(self, flow: http.HTTPFlow):
        if flow.request.url == self.search_url and flow.request.method == 'POST':
            pass
        pass

    @command.command("energymonster.inc")
    def response(self, flow: http.HTTPFlow):
        """
        处理响应
        :param flow:
        :return:
        """
        if flow.request.url == self.search_url and flow.request.method == 'POST':
            if flow.response.status_code == 200:
                r = json.loads(flow.response.text)
                if r['msg'] == 'ok' and r['code'] == 0:
                    client = MongoDBClient()
                    client.save_to_mongodb(r['data']['rows'])
                    ctx.log.info('Save Successful!')
                else:
                    ctx.log.info(f'Failed {str(r)}')
            else:
                ctx.log.info('API Requests Failed!')


class Test:
    """
    用于测试 mitmproxy 修改请求，使用代理
    """

    def request(self, flow: http.HTTPFlow):
        if flow.request.host == 'httpbin.org' and flow.request.method == 'GET':
            ip, port = get_proxy().split(':')
            proxy = (ip, int(port))
            print(f"--------------开始修改 ip 为 {ip}:{port}")
            if flow.live:
                print("--------------设置代理")
                flow.live.change_upstream_proxy_server(proxy)
        else:
            print('Wrong!')

    def response(self, flow: http.HTTPFlow):
        if flow.request.host == 'httpbin.org' and flow.request.method == 'GET':
            print(f'--------------请求的 ip 为: {json.loads(flow.response.text)["origin"]}')
            message = 'This request was using mitmproxy!'
            data = json.loads(flow.response.text)
            data.update({'message': message})
            flow.response.text = json.dumps(data)


addons = [
    EnergyMonster(),
    # Test(),
]
