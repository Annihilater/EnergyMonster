#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/29 1:50 下午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : main.py
import random
import threading
import time

from appium import webdriver

from appium.webdriver.common.touch_action import TouchAction

# from config import el_discover, el_mini_program, el_my_mini_program, el_energy_master, el_energy_master_search_page, \
#     el_energy_master_search_button, el_energy_master_search_position, position, el_energy_master_search_first, \
#     el_energy_master_search_complete, nearby_stores_x, nearby_stores_y, deviceName, platformName, platformversion, \
#     appPackage, appActivity, noReset, newCommandTimeout, unicodeKeyboard, resetKeyboard
from mitmproxy_run import mitmproxy_run
from config import *


def main():
    # This sample code uses the Appium python client
    # pip install Appium-Python-Client
    # Then you can paste this into a file and simply run with Python

    url = "http://localhost:4723/wd/hub"
    caps = {"deviceName": deviceName,
            "platformName": platformName,
            "platformversion": platformversion,
            "appPackage": appPackage,
            "appActivity": appActivity,
            "noReset": noReset,
            "newCommandTimeout": newCommandTimeout,
            "unicodeKeyboard": unicodeKeyboard,
            "resetKeyboard": resetKeyboard,
            }

    driver = webdriver.Remote(url, caps)

    try:
        driver.implicitly_wait(10)

        # 点击-发现
        el2 = driver.find_element_by_xpath(el_discover)
        el2.click()
        print('点击-发现-成功')

        # 点击-小程序
        el3 = driver.find_element_by_xpath(el_mini_program)
        el3.click()
        print('点击-小程序-成功')

        # 点击-我的小程序
        el4 = driver.find_element_by_xpath(el_my_mini_program)
        el4.click()
        print('点击-我的小程序-成功')

        # 点击-怪兽充电小程序
        el5 = driver.find_element_by_id(el_energy_master)
        el5.click()
        print('点击-怪兽充电小程序-成功，等待 10 秒')
        for i in range(10):
            time.sleep(1)
            print(f'等待: {i + 1} 秒')

        # 点击-进入搜索位置页面
        el6 = driver.find_element_by_xpath(el_energy_master_search_page)
        el6.click()
        print('点击-进入搜索位置页面-成功')
        time.sleep(10)  # 这里等待时间需要长一些，之前设置的是 5 秒，报错了

        # 点击-搜索按钮
        el7 = driver.find_element_by_accessibility_id(el_energy_master_search_button_accessibility_id)
        el7.click()
        print('点击-搜索按钮-成功')
        time.sleep(3)

        # 输入-位置
        el8 = driver.find_element_by_id(el_energy_master_search_position)
        time.sleep(3)
        el8.send_keys(position)
        print('输入-位置-成功')
        time.sleep(3)

        # 选择-第一个位置
        el9 = driver.find_element_by_xpath(el_energy_master_search_first)
        el9.click()
        print('选择-第一个位置-成功')
        time.sleep(3)

        # 点击-完成
        el10 = driver.find_element_by_id(el_energy_master_search_complete)
        el10.click()
        print('点击-完成-成功')
        time.sleep(3)

        # 点击-附近门店
        TouchAction(driver).tap(x=nearby_stores_x, y=nearby_stores_y).perform()
        print('点击-附近门店-成功，等待 15 秒')
        for i in range(15):
            time.sleep(1)
            print(f'Wait: {i + 1} Seconds')

    except Exception as e:
        print('Error.')
        print(e)

    for i in range(10000):
        print(f'第 {i} 次下拉')
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        print(f'window_size: width: {x}, height: {y}')
        sx = x * 0.50
        sy = y * 0.9
        ey = y * 0.1
        driver.swipe(sx, sy, sx, ey)

    driver.quit()


if __name__ == '__main__':
    thread = threading.Thread(target=mitmproxy_run)
    thread.start()
    main()
