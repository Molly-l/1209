import requests
from lxml import etree
import re
#抓取最新县以上  行政区划代码
class MzbSpider(object):
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

    def get_false_link(self):
        html = requests.get(url=self.url,headers=self.headers).text
        p = etree.HTML(html)
        link = 'http://www.mca.gov.cn' + p.xpath('//table/tr[2]//a/@href')[0]
        print(link)
        self.get_real_link(link)

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

    def run(self):
        self.get_false_link()

if __name__ == '__main__':
    spider = MzbSpider()
    spider.run()

































