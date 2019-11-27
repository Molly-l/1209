import requests
import json
from threading import Thread,Lock
from queue import Queue
import time
import random
from fake_useragent import UserAgent
from lxml import etree
import csv


#小米应用商店抓取 (多线程)  所有应用分类、名称、链接
class XiaomiSpider(object):
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId={}&pageSize=30'
        self.q = Queue()
        self.i = 0
        # 创建互斥锁
        self.lock = Lock()
        self.proxies = {
            'http':'http://309435365:szayclhp@43.226.164.156:16816',
            'https': 'https://309435365:szayclhp@43.226.164.156:16816',
        }
        # 存入csv文件
        self.f = open('小米.csv','a',newline='') #Windows要写(newline='')
        self.writer = csv.writer(self.f) #将writer对象写入打开f为csv格式


    # 功能函数:获取响应内容
    def get_html(self,url):
        headers = { 'User-Agent' : UserAgent().random }
        html = requests.get(url=url,headers=headers,proxies=self.proxies).text #获取整个页面内容

        return html

    # 获取所有类别的id
    def get_id(self):
        url = 'http://app.mi.com/'
        html = self.get_html(url) #获取整个页面内容
        p = etree.HTML(html)
        li_list = p.xpath('//div[@class="sidebar"]/div[2]/ul[1]/li')
        for li in li_list: #每个应用的链接
            id = li.xpath('./a/@href')[0].split('/')[-1] # href="/category/15"
            type_name = li.xpath('./a/text()')[0]#每个应用的name
            self.url_in(id)

    # url入队列
    def url_in(self,id):
        total = self.get_total(id)
        for page in range(0,total):
            url = self.url.format(page,id)
            self.q.put(url) # 每个应用的url入队列

    # 获取总页数
    def get_total(self,id):
        url = self.url.format(0,id)
        html = self.get_html(url)
        print(html)
        html = json.loads(html)#将响应内容由: json 转为 python
        # count:为应用数量
        count = int(html['count'])
        if count % 30 == 0:
            total = count // 30
        else:
            total = count // 30 + 1

        return total #总页数

    # 线程事件函数: 请求+解析+保存
    def parse_html(self):
        while True:
            if not self.q.empty():#q.empty()判断队列是否为空，为空返回True
                url = self.q.get() #当队列为空时,阻塞
                html = json.loads(self.get_html(url))#将响应内容由: json转为 python
                item = {}
                app_list = []
                for app in html['data']:
                    item['name'] = app['displayName']
                    item['type'] = app['level1CategoryName']
                    item['link'] = app['packageName']
                    app_list.append(
                        (item['name'],item['type'],item['link'])
                    )
                    print(item)
                # 写文件需要加锁
                self.lock.acquire()
                self.writer.writerows(app_list) #
                self.lock.release()

            else:
                break

    # 主函数
    def run(self):
        # URL入队列
        self.get_id()
        t_list = []
        # 创建多个线程
        for i in range(5):
            t = Thread(target=self.parse_html)
            t_list.append(t)
            t.start()
        # 回收线程
        for j in t_list:
            j.join()

        # 最终关闭文件
        self.f.close()

if __name__ == '__main__':
    begin = time.time()
    spider = XiaomiSpider()
    spider.run()
    end = time.time()
    print('执行时间:%.2f' % (end-begin))





























