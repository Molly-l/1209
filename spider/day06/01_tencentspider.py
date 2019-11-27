import requests
import json
from fake_useragent import UserAgent
from threading import Thread,Lock
import time
from queue import Queue
from urllib import parse


class TencentSpider(object):
    def __init__(self):
        self.one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1563912271089&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        self.two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1563912374645&postId={}&language=zh-cn'
        self.one_q = Queue()
        self.two_q = Queue()
        self.lock = Lock()
        # 计数
        self.i = 0
        # 打开json文件
        self.f = open('tencent.json','a')
        self.item_list = []

    # 功能函数: 获取html
    def get_html(self,url):
        headers = { 'User-Agent':UserAgent().random }
        html = requests.get(url=url,headers=headers).text
        return html

    # 一级页面URL入队列
    def url_in(self):
        keyword = input('请输入职位类别:')
        keyword = parse.quote(keyword)
        total = self.get_total(keyword)
        for index in range(1,total+1):
            one_url = self.one_url.format(keyword,index)
            self.one_q.put(one_url)

    # 获取某个类别总页数
    def get_total(self,keyword):
        url = self.one_url.format(keyword,1)
        html = json.loads(self.get_html(url))
        count = int(html['Data']['Count'])
        if count % 10 == 0:
            total = count // 10
        else:
            total = count // 10 + 1

        return total

    # 线程事件函数 - 一级页面 - postId
    def parse_one_page(self):
        while True:
            if not self.one_q.empty():
                one_url = self.one_q.get()
                html = json.loads(self.get_html(one_url))
                for job in html['Data']['Posts']:
                    post_id = job['PostId']
                    two_url = self.two_url.format(post_id)
                    # 放到二级页面队列中
                    self.two_q.put(two_url)
            else:
                break

    # 线程事件函数 - 二级页面 - 名称+要求+职责+时间+地点
    def parse_two_page(self):
        while True:
            try:
                two_url = self.two_q.get(timeout=3)
                html = json.loads(self.get_html(two_url))
                item = {}
                item['name'] = html['Data']['RecruitPostName']
                item['city'] = html['Data']['LocationName']
                item['duty'] = html['Data']['Responsibility']
                item['requ'] = html['Data']['Requirement']
                item['time'] = html['Data']['LastUpdateTime']
                print(item)

                self.lock.acquire()
                self.i += 1
                self.item_list.append(item)
                self.lock.release()
            except Exception as e:
                break

    # 入口函数
    def run(self):
        self.url_in()
        one_list = []
        two_list = []

        for i in range(3):
            t = Thread(target=self.parse_one_page)
            one_list.append(t)
            t.start()

        for i in range(5):
            t = Thread(target=self.parse_two_page)
            two_list.append(t)
            t.start()

        for one in one_list:
            one.join()

        for two in two_list:
            two.join()

        print('数量:',self.i)

        # 存到json文件
        json.dump(self.item_list,self.f,ensure_ascii=False)
        self.f.close()

if __name__ == '__main__':
    begin = time.time()
    spider = TencentSpider()
    spider.run()
    end = time.time()
    print('执行时间:%.2f' % (end-begin))
























