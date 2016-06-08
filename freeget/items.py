# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field


class FreegetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    id=Field()
    #title = Field()#标题
    #duration = Field()#时长
    #time_created = Field()#添加时间
    #author=Field()#作者
    #viewed=Field()#查看人数
    #remarked=Field()#收藏人数
    #comments=Field()#留言人数
    #remarks=Field()#积分
    #view_url=Field()#播放页面
    #img_url=Field()#图片
    VID_url=Field()
    #file_url=Field()#下载链接
    #updated=Field()
