# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan2'
    allowed_domains = ['maoyan.com']
    #重写start_requests()方法
    def start_requests(self):
        url='https://maoyan.com/board/4?offset={}'
        for offset in range(0,91,10):
            page_url=url.format(str(offset))
            yield scrapy.Request(url=url, callback=self.parse_html)

    def parse_html(self, response):
        #给items.py中的类：MaoyanItem实例化
        item=MaoyanItem()
        dd_list=response.xpath('//dl[@class="board-wrapper"]/dd')
        for dd in dd_list:
            #给item对象的3个属性赋值，必须使用['']
            item['name']=dd.xpath('./a/@title').get().strip()
            item['star']=dd.xpath('.//p[@class="star"]/text()').get().strip()
            item['time']=dd.xpath('.//p[@class="releasetime"]/text()').get().strip()
            #数据交给管道的方式
            yield item #yield语句之后循环不会停止
                       #return之后循环结束
