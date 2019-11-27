# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'#爬虫名
    allowed_domains = ['www.baidu.com']#允许爬取的域名
    start_urls = ['http://www.baidu.com/']#第一个要怕取得url地址

    def parse(self, response):
        #方法一：
        r_list=response.xpath('').extract()[0] #.extract()把列表中所有的选择器对象序列化为字符串
        #.extract_first() 序列化并提取列表中第一个选择器  =.get()
        r_list = response.xpath('').extract_first()
        print(r_list)
