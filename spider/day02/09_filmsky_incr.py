from urllib import request
import re
import time
import random
from fake_useragent import UserAgent
import pymysql
from hashlib import md5
import sys

class FilmSkySpider(object):
    def __init__(self):
        self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
        self.db = pymysql.connect(
            'localhost','root','123456','filmskydb',
            charset='utf8'
        )
        self.cursor = self.db.cursor()

    # 功能函数1: 获取html函数
    def get_html(self,url): #接收一个url，向这个url发请求，获取到响应内容并返回给调用者
        headers = { 'User-Agent':UserAgent().random }
        req = request.Request(url=url,headers=headers)
        resp = request.urlopen(req)
        html = resp.read().decode('gb18030','ignore')

        return html

    # 功能函数2: 解析函数
    def parse_func(self,re_bds,html):
        p = re.compile(re_bds,re.S)
        r_list = p.findall(html)

        return r_list

    # 解析提取所需数据
    def parse_html(self,one_url):
        one_html = self.get_html(one_url) #传入的url返回对应的相应内容
        re_bds = '<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>'
        # href_list=re.findall(re_bds,one_html)
        href_list = self.parse_func(re_bds,one_html)#按照正则表达式从响应内容中匹配出需要的信息
        # href_list: ['/html/xxxx','/html/xxxx','']
        for href in href_list:
            link = 'https://www.dytt8.net' + href #二级url

            s = md5()
            s.update(link.encode())#计算link的摘要
            finger = s.hexdigest()#获取16进制摘要内容
            ############################
            if not self.is_go_on(finger):
                # 向详情页发请求,提取 名字和下载链接，存入数据库
                self.parse_two_page(link)#
                # 抓取1个电影之后,随机休眠
                time.sleep(random.randint(1,2))
                # 抓取完成后把finger存入到指纹表中
                ins = 'insert into request_finger values(%s)'
                self.cursor.execute(ins,[finger])
                self.db.commit()
            else:
                # 一旦抓取完成,直接退出进程
                sys.exit('完成')


    # 判断finger在指纹表中是否存在
    def is_go_on(self,finger):
        sel = 'select finger from request_finger where ' \
              'finger=%s'
        result = self.cursor.execute(sel,[finger])#执行sql语句
        if result:
            return True

    # 解析二级页面函数
    def parse_two_page(self,link):
        two_html = self.get_html(link)
        re_bds = '<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>.*?<td style="WORD-WRAP.*?>.*?>(.*?)</a>'
        r_list = self.parse_func(re_bds,two_html)
        # r_list: [('电影名称','下载链接')]
        item = {}
        if r_list:
            item['name'] = r_list[0][0].strip()
            item['download'] = r_list[0][1].strip()
            print(item)
            ins = 'insert into filmtab values(%s,%s)'
            L = [ item['name'],item['download'] ]
            self.cursor.execute(ins,L)
            self.db.commit()

    def run(self):
        for i in range(1,205):
            one_url = self.url.format(i)
            self.parse_html(one_url)

if __name__ == '__main__':
    spider = FilmSkySpider()
    spider.run()














