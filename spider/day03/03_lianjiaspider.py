import requests
from lxml import etree
from fake_useragent import UserAgent
import time
import random
class LianjiaSpider(object):
    def __init__(self):
        self.url = 'https://bj.lianjia.com/ershoufang/pg{}/'

    def parse_html(self, url):#发送请求接受响应并提取信息
        headers = {'User-Agent': UserAgent().random }
        #有问题的页面，尝试3次，如果不行直接抓取下一页数据
        for i in range(3):
            try:
                html = requests.get(url=url, headers=headers,timeout=3).text
                self.get_data(html)
                break
            except Exception as e:
                print('Retry')

    def get_data(self,html):#提取信息
        # 1.创建解析对象
        p = etree.HTML(html)
        # 2.基准xpath: 每个房源的li节点对象列表
            ##按照xpath表达式从响应内容中匹配出需要的信息
        li_list = p.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATALOGCLICKDATA"]')
        print(li_list)
        item = {}
        for li in li_list:
        # 名称+位置
            name_list = li.xpath('.//div[@class="positionInfo"]/a[1]/text()')
            item['name'] = name_list[0].strip() if name_list else None #
            print(item)
            address_list = li.xpath('.//div[@class="positionInfo"]/a[2]/text()')
            item['address'] = address_list[0] if address_list else None
            # 户型+面积+方位+精装+楼层+年代+类型
            hlist = li.xpath('.//div[@class="houseInfo"]/text()')
            if hlist:
                # hlist: ['三室两厅','100平米','南北',...]
                hlist = hlist[0].split('|')
                item['model'] = hlist[0].strip()
                item['area'] = hlist[1].strip()
                item['direct'] = hlist[2].strip()
                item['perfect'] = hlist[3].strip()
                item['floor'] = hlist[4].strip()
                item['year'] = hlist[5].strip()
                item['type'] = hlist[6].strip()
                # if
            else:
                item['model'] = item['area'] = item['direct'] = item['perfect'] = item['floor'] = item['year'] = item['type']=None
            # 单价+总价
            total_list = li.xpath('.//div[@class="totalPrice"]/span/text()')
            item['total'] = float(total_list[0]) * 10000 if total_list else None
            unit_list = li.xpath('.//div[@class="unitPrice"]/span/text()')
            item['unit'] = unit_list[0][2:-4] if unit_list else None
        print(item)

    def run(self):
        for pg in range(1):
            url = self.url.format(pg+1)
            self.parse_html(url)
            # 随机休眠
            time.sleep(random.uniform(0, 2))
            print('第%d页抓取成功' % pg)
if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.run()