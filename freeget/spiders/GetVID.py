# -*- coding: utf-8 -*-
import scrapy
from freeget.Model import Video,DBsession
from scrapy.http import Request
from freeget.items import FreegetItem
import re



class GetvidSpider(scrapy.Spider):
    name = "GetVID"
    allowed_domains = ["freeget"]
    start_urls = (
        'http://www.freeget/',
    )
    session = DBsession()
    def start_requests(self):
        videos = self.session.query(Video).filter(Video.VID_url =='').all()
        if len(videos)>0:
            for video in videos:
                url = video.view_url
                id = video.id
                yield Request(url=url,meta={'id':id},callback=self.parse)

    def parse(self, response):
        pass
        item = FreegetItem()
        html = response.body
        try:
	        pattern = re.compile('(?<=")http://91\S{1,}(?=")')
	        VID_url = pattern.findall(html)[0]
	        if VID_url:
	            item['VID_url']=VID_url
	            item['id']=response.meta['id']
	            yield item
        except Exception:
            pass


