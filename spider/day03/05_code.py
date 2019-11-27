import requests
from lxml import etree
import os

class TarenaCodeSpider(object):
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/AIDCode/aid1907/13-Redis/'
        self.auth = ('tarenacode','code_2013')

    def parse_html(self):
        # 1.创建文件夹
        directory = '/home/tarena/' + '/'.join(self.url.split('/')[3:])
        if not os.path.exists(directory):
            os.makedirs(directory)
        # 2. 请求,解析提取 href 的值
        html = requests.get(
            url=self.url,
            auth=self.auth,
            headers = {'User-Agent':'Mozilla/5.0'}
        ).text

        p = etree.HTML(html)
        href_list = p.xpath('//a/@href')
        # href_list: ['..','day01/','xxx.zip']
        for href in href_list:
            if href.endswith('.zip') or href.endswith('.rar'):
                self.download(href,directory)

    # 下载文件: 拼接url,发请求,保存到本地文件
    def download(self,href,directory):
        file_url = self.url + href
        html = requests.get(
            url=file_url,
            auth=self.auth,
            headers={ 'User-Agent':'Mozilla/5.0' }
        ).content
        # filename: /home/tarena/AIDCode/aid1907/13-Redis/redis_day01.zip
        filename = directory + href
        with open(filename,'wb') as f:
            f.write(html)
        print(filename,'下载成功')

    def run(self):
        self.parse_html()

if __name__ == '__main__':
    spider = TarenaCodeSpider()
    spider.run()






















