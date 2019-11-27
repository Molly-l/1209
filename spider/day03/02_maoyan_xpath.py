from urllib import request
from lxml import etree
import time
import random
from fake_useragent import UserAgent

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        # 计数变量
        self.i = 0

    def get_html(self,url):
        headers = { 'User-Agent':UserAgent().random }
        req = request.Request(url=url,headers=headers)
        resp = request.urlopen(req)
        html = resp.read().decode('utf-8')
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self,html):
        p = etree.HTML(html)
        item = {}
        # 1.基准xpath: dd节点对象列表 [dd1,dd2,dd3]
        dd_list = p.xpath('//dl[@class="board-wrapper"]/dd')
        # 2.for循环遍历,依次提取每个电影信息
        for dd in dd_list:
            item['name'] = dd.xpath('.//p[@class="name"]/a/text()')[0]
            item['star'] = dd.xpath('.//p[@class="star"]/text()')[0].strip()
            item['releasetime'] = dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()[5:15]

            print(item)



    def save_html(self,film_list):
        item = {}
        for film in film_list:
            item['name'] = film[0].strip()
            item['star'] = film[1].strip()
            item['time'] = film[2].strip()[5:15]
            print(item)
            self.i += 1

    def run(self):
        for offset in range(0,91,10):
            url = self.url.format(offset)
            self.get_html(url)
            # 休眠
            time.sleep(random.uniform(0,1))
        print('数量:',self.i)

if __name__ == '__main__':
    start = time.time()
    spider = MaoyanSpider()
    spider.run()
    end = time.time()
    print('执行时间:%.2f' % (end-start))









































