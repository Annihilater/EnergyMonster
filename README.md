# EnergyMonster

## 思路

1. 使用 Appium 控制安卓手机自动刷新小程序内店铺列表
2. 使用 mitmproxy 获取小程序请求的响应，从响应中提取店铺数据
3. 将数据储存到 MongoDB

## 用法

代码在 mitm_scrapy 文件夹内，启动文件为 main.py。启动前需要另外开启 Appium Server 和 MongoDB 数据库，并确保有真机或者安卓模拟器连接到本机。

## 效果展示

![image-20191230143324183](https://klause-blog-pictures.oss-cn-shanghai.aliyuncs.com/ipic/2019-12-30-063324.png)



## 待办

- [ ] 使用 Scrapy 抓接口