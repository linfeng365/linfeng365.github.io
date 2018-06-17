---
layout: post
title: MWeb 七牛图床
description: 很方便上传图片获得外链方法。
category: blog
---
# MWeb 七牛图床

很方便上传图片获得外链方法。

## 配置
1.注册七牛。在对象存储新建一个存储空间。
获得一个测试域名如:ovtab06ib.bkt.clouddn.com
根据存储空间区域(华北,华中,华南等),查看存储区域的上传域名。(对应 MWeb `API 地址`选项)
https://developer.qiniu.com/kodo/manual/1671/region-endpoint
在个人面板,密钥管理查看 AccessKey 和 SecretKey 。



2.回到 MWeb ,把配置参数填下。 如图

![](http://ovtzx06ib.bkt.clouddn.com/15046645634730.jpg)




完成配置。

## 使用方法:
把图片拖进文章,在"发布"菜单中,选择"把本地图片传至图床..." 
然后就可以"复制Markdown"或"新建文档"获得替换为图床链接的新文本。

![](http://ovtzx06ib.bkt.clouddn.com/15046669657004.jpg)


