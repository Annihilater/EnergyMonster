#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/29 9:14 下午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : my_proxy.py


import requests


def get_proxy():
    """
    获取免费的随机代理，请开启 ProxyPool 项目的 API: http://localhost:5555/random
    :return:
    """
    url = 'http://localhost:5555/random'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None


if __name__ == '__main__':
    ip, port = get_proxy().split(':')
    print((ip, int(port)))
