import requests
import time
import random
from fake_useragent import UserAgent
import json
import re
#豆瓣排行榜  电影名称、评分
class DoubanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=20'
        self.i = 0

    # 获取响应内容
    def get_html(self,url):
        headers = { 'User-Agent': UserAgent().random }
        html = requests.get(url=url,headers=headers).text
        return html

    # 解析提取数据
    def parse_html(self,url):
        # html: '[{},{},{}]'
        # json.loads() : 把json格式字符串转为Python数据类型
        html = self.get_html(url)#获取到每页电影整个内容
        html = json.loads(html)
        item = {}
        for film in html:#从整页内容中循环取出每个信息
            item['name'] = film['title']
            item['score'] = film['score']
            item['time'] = film['release_date']
            print(item)
            self.i += 1

    def run(self):

        types_dict = self.get_types_dict()

        menu = ''
        for key in types_dict:
            menu = menu + key + '|'#拼接 (menu+ 叠加)
        print(menu)#展示

        typ = input('请输入电影类型:')
        types = types_dict[typ] #types_dict={'剧情','11'}

        total = self.get_total(types)# 获取电影总数
        for start in range(0,total,20):
            url = self.url.format(types,start)#每页url
            self.parse_html(url)
            time.sleep(random.uniform(0,1))
        print('总数:',self.i)

    # 获取所有类型的字典
    def get_types_dict(self):
        url = 'https://movie.douban.com/chart'
        html = self.get_html(url)
        p = re.compile('<span><a href=".*?type_name=(.*?)&type=(.*?)&interval_id=100:90&action=">.*?</span>',re.S)
        # r_list: [('剧情','11'),('爱情','13'),()]
        r_list = p.findall(html)
        types_dict = {} #设置为字典，通过键可以取值
        for r in r_list:
            types_dict[r[0]] = r[1]

        return types_dict

    # 获取电影总数
    def get_total(self,types):
        url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(types)
        html = json.loads(self.get_html(url))#获取每个类型url的整个内容
        total = html['total']
        return total




if __name__ == '__main__':
    spider = DoubanSpider()
    spider.run()























