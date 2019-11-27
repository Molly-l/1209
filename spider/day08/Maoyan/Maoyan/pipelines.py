# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline(object):
    def process_item(self, item, spider):
        print(item['name'])
        return item

# 自定义管道 - MySQL数据库
import pymysql
from .settings import *
class MaoyanMysqlPipeline(object):
    #监听爬虫，爬虫启动时只执行1次，一般用于数据库连接
    def open_spider(self,spider):
        self.db=pymysql.connect(host=MYSQL_HOST,
                                user=MYSQL_USER,
                                password=MYSQL_PWD,
                                database=MYSQL_DB,
                                charset=MYSQL_CHAR)
        self.cursor = self.db.cursor() #创建一个游标对象

    def process_item(self, item, spider):#必须有
        ins = 'insert into filmtab values(%s,%s,%s)'
        # 因为execute()的第二个参数为列表
        L = [item['name'], item['star'], item['time']]
        self.cursor.execute(ins, L)
        self.db.commit()

        return item

    #监听爬虫，爬虫启动时只执行1次，一般用于数据库断开
    def close_spider(self,spider):
        print('我是close_spider函数输出')
        # 一般用于断开数据库连接
        self.cursor.close()
        self.db.close()

'''
class MaoyanMongoPipeline(object):
    #监听爬虫，爬虫启动时只执行1次，一般用于数据库连接
    def open_spider(self,spider):
        self.db=pymysql.connect(host=MYSQL_HOST,
                                user=MYSQL_USER,
                                password=MYSQL_PWD,
                                database=MYSQL_DB,
                                charset=MYSQL_CHAR)
        self.cursor = self.db.cursor() #创建一个游标对象

    def process_item(self, item, spider):#必须有
        ins = 'insert into filmtab values(%s,%s,%s)'
        # 因为execute()的第二个参数为列表
        L = [item['name'], item['star'], item['time']]
        self.cursor.execute(ins, L)
        self.db.commit()

        return item

    #监听爬虫，爬虫启动时只执行1次，一般用于数据库断开
    def close_spider(self,spider):
        print('我是close_spider函数输出')
        # 一般用于断开数据库连接
        self.cursor.close()
        self.db.close()
'''