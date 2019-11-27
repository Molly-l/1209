import time
import random
# from useragents import ua_list
import requests
from fake_useragent import UserAgent

#贴吧下载图片
class TiebaSpider:
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?'

    # 1.请求:
    def get_html(self,params):
        headers = {'User-Agent':UserAgent().random}
        html = requests.get(url=self.url,params=params,headers=headers).text

        return html

    # 2.解析
    def parse_html(self):
        pass

    # 3.保存
    def save_html(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)

    # 4.入口函数
    def run(self):
        name = input('请输入贴吧名:')
        begin = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))

        # for循环 - 拼接地址,发请求,保存
        for page in range(begin,end+1):
            pn = (page-1)*50
            params = {
                'kw':name,
                'pn':str(pn),
            }

            html = self.get_html(params)
            filename = name + '-第%s页.html' % str(page)
            self.save_html(filename,html)
            print('第%d页抓取成功' % page)
            # 每抓取1页随机休眠1-2秒钟
            # time.sleep(random.randint(1,2))
            time.sleep(random.uniform(0,1))

if __name__ == '__main__':
    spider = TiebaSpider()
    spider.run()

















