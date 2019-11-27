import time
import random
from urllib import parse

import requests
from fake_useragent import UserAgent
from lxml import etree


class TiebaImageSpider:
    def __init__(self):
        self.url='http://tieba.baidu.com/f?kw={}&pn={}'
        self.headers={'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'}

    # 解析函数 - 实现最终图片抓取
    def parse_html(self, page_url):
        page_html=self.get_html(page_url)

        print(99,page_html)
        # 提取50个帖子链接 ['/p/2323','/p/23232']
        xpath_bds='//li[@class=" j_thread_list clearfix"]/div/div/div/div/a/@href'
        tlink_list=self.xpath_func(page_html,xpath_bds)
        print(888,tlink_list)


        for tlink in tlink_list:
            # 拼接帖子的URL地址
            tie_url='http://tieba.baidu.com'+tlink
            # 把1个帖子中所有的图片保存到本地
            self.save_image(tie_url)
            # 爬完1个帖子中所有图片,休眠0-2秒钟

    # 功能函数1: 请求  整个页面内容
    def get_html(self, url):
        html=requests.get(url=url, headers=self.headers).text

        return html

    # 功能函数2: xpath解析
    def xpath_func(self, html, xpath_bds):
        p=etree.HTML(html)
        link_list=p.xpath(xpath_bds)
        return link_list

    # 把t_url中所有图片下载下来
    def save_image(self, t_url):

        tie_html=self.get_html(t_url)

        xpath_bds='//div[@class="d_post_content j_d_post_content "]/img[@class="BDE_Image"]/@src'
        tu_list=self.xpath_func(tie_html,xpath_bds)
        print(tu_list)
        for tulink in tu_list:
            self.download_image(tulink)
            time.sleep(random.uniform(0,1))


    # 保存1张图片到本地
    def download_image(self, tulink):
        tu=requests.get(url=tulink, headers=self.headers).content
        tu_filename=tulink[-10:]
        print(tu_filename)
        with open(tu_filename,'wb') as f:
            f.write(tu)
            print(tu_filename, '下载成功')

    # 主入口
    def run(self):
        # name = input('输入贴吧名：')
        # start = int(input('输入起始页：'))
        # end = int(input('输入终止页：'))
        name = '李毅吧'
        start = 1
        end = 2
        params = parse.quote(name)
        for pages in range(start, end+1):
            pn=(pages-1)*50
            url=self.url.format(params,pn)
            print(url)
            self.parse_html(url)


if __name__ == '__main__':
    spider=TiebaImageSpider()
    spider.run()