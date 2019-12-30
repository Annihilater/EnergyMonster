#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/28 3:39 下午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : mitmproxy_run.py
import os


def mitmproxy_run():
    print("将会启动 mitmproxy 服务")
    os.system("mitmweb -s addons.py")


if __name__ == '__main__':
    mitmproxy_run()
