#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/29 8:29 下午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 3.py
import requests

from my_proxy import get_proxy


def test_mitmproxy():
    """
    走 mitmproxy 代理
    让 mitmproxy 修改请求走免费代理
    :return:
    """
    certfile_path = 'mitmproxy-ca-cert.pem'
    url = 'https://httpbin.org/ip'
    proxies = {
        "http": "http://127.0.0.1:8080",
        "https": "https://127.0.0.1:8080"
    }

    r1 = requests.get(url, proxies=proxies, verify=certfile_path)
    print(r1.text)

    # r2 = requests.get(url)
    # print(r2.text)


def test_proxy():
    """
    测试免费代理有没有效果
    :return:
    """
    url = 'http://httpbin.org/get'
    ip, port = get_proxy().split(':')
    proxies = {
        "http": f"http://{ip}:{port}",
        "https": f"http://{ip}:{port}"
    }
    r1 = requests.get(url, proxies=proxies)
    print(r1.text)

    r2 = requests.get(url)
    print(r2.text)


if __name__ == '__main__':
    test_mitmproxy()
    # test_proxy()

