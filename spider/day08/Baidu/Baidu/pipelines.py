# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#管道文件
class BaiduPipeline(object):
    def process_item(self, item, spider):#item抓下来的数据
        return item

#存入mysql数据库
class