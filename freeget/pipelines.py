# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from freeget.Model import Video,DBsession

class FreegetSQLitePipeline(object):
    session = DBsession()
    def process_item(self, item, spider):
        print '开始存数据'
        self.session.query(Video).filter(Video.id == item['id']).update({
            'VID_url':item['VID_url']
        })
        self.session.commit()
        return item
