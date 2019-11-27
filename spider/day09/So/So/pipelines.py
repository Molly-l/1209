# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import scrapy

class SoPipeline(object):
    # 重写get_media_requests()方法
    def get_media_requests(self, item, info):
        yield scrapy.Request(
            url=item['img_url'],
            meta={'name': item['img_title']}
        )

    # 重写file_path()方法,自定义文件名
    def file_path(self, request, response=None, info=None):
        img_link = request.url

    # request.meta属性
        filename = request.meta['name'] + '.' + img_link.split('.')[-1]
        return filename