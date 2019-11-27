import requests
from lxml import etree
import re
import pymysql
from hashlib import md5
#抓取最新县以上  行政区划代码
class MzbSpider(object):
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
        self.db = pymysql.connect(
            'localhost','root','123456','govdb',charset='utf8'
        )
        self.cursor = self.db.cursor()
        # 创建3个列表,用于excutemany()
        self.province = []
        self.city = []
        self.county = []

    def get_false_link(self):
        html = requests.get(url=self.url,headers=self.headers).text
        p = etree.HTML(html)
        link = 'http://www.mca.gov.cn' + p.xpath('//table/tr[2]//a/@href')[0]
        # 对link进行md5加密
        # 查看link是否在request_finger表中
        s = md5()
        s.update(link.encode())
        finger = s.hexdigest()
        sel = 'select finger from request_finger where finger=%s'
        result = self.cursor.execute(sel,[finger])
        if not result:
            self.get_real_link(link)
            # 抓完后把指纹存到表中
            ins = 'insert into request_finger values(%s)'
            self.cursor.execute(ins,[finger])
            self.db.commit()
        else:
            print('数据已是最新')

    def get_real_link(self,link):
        html = requests.get(url=link,headers=self.headers).text
        p = re.compile('window.location.href="(.*?)"',re.S)
        real_link = p.findall(html)[0]
        self.get_data(real_link)

    def get_data(self,real_link):
        html = requests.get(url=real_link,headers=self.headers).text
        p = etree.HTML(html)
        tr_list = p.xpath('//tr[@height="19"]')
        for tr in tr_list:
            name = tr.xpath('./td[3]/text()')[0].strip()
            code = tr.xpath('./td[2]/text()')[0].strip()
            print(name,code)

            if code[-4:] == '0000':
                self.province.append((name,code))
                if code[:2] in ['11','12','31','50']:
                    cfcode = code[:2] + '0000'
                    self.city.append((name,code,cfcode))
            elif code[-2:] == '00':
                cfcode = code[:2] + '0000'
                self.city.append((name,code,cfcode))
                # 永远记录最近的一个市
                last_city = code
            else:
                if code[:2] in ['11','12','31','50']:
                    xfcode = code[:2] + '0000'
                else:
                    # 永远赋值最近的市的编号
                    xfcode = last_city
                self.county.append((name,code,xfcode))
        # 存储到数据库
        self.insert_mysql()

    def insert_mysql(self):
        # 先清空表
        del1 = 'delete from province'
        del2 = 'delete from city'
        del3 = 'delete from county'
        self.cursor.execute(del1)
        self.cursor.execute(del2)
        self.cursor.execute(del3)
        self.db.commit()
        # 再插入新抓的数据
        ins1 = 'insert into province values(%s,%s)'
        ins2 = 'insert into city values(%s,%s,%s)'
        ins3 = 'insert into county values(%s,%s,%s)'
        self.cursor.executemany(ins1,self.province)
        self.cursor.executemany(ins2,self.city)
        self.cursor.executemany(ins3,self.county)
        self.db.commit()

    def run(self):
        self.get_false_link()

if __name__ == '__main__':
    spider = MzbSpider()
    spider.run()

































