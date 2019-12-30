#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/29 6:24 下午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : config.py

# position settings
# position = "复旦大学"
# position = '东方明珠'
position = '虹桥火车站'

# caps settings
deviceName = 'TKQKCMU8WCHEJBIR'
platformName = 'Android'
platformversion = '6.0'
appPackage = 'com.tencent.mm'
appActivity = '.ui.LauncherUI'
noReset = 'True'
newCommandTimeout = 6000
unicodeKeyboard = 'True'
resetKeyboard = 'True'

# elements xpath config
el_discover = "//android.widget.FrameLayout[@content-desc=\"当前所在页面,与的聊天\"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView"
el_mini_program = "//android.widget.FrameLayout[@content-desc=\"当前所在页面,与的聊天\"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.mm.ui.mogic.WxViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout"
el_my_mini_program = "//android.widget.FrameLayout[@content-desc=\"当前所在页面,小程序\"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout"
el_energy_master = "com.tencent.mm:id/rb"
el_energy_master_search_page = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[3]"

el_energy_master_search_button_accessibility_id = "搜索位置"
el_energy_master_search_button_id = "com.tencent.mm:id/dbm"
el_energy_master_search_button_xpath = '//android.widget.ImageButton[@content-desc="搜索位置"]'

el_energy_master_search_position = "com.tencent.mm:id/lh"
el_energy_master_search_first = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[1]"
el_energy_master_search_complete = "com.tencent.mm:id/kx"

nearby_stores_x = 134
nearby_stores_y = 1763
