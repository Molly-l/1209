from urllib import request, parse
import time
import random
from spider.day01.useragents import ua_list

class TiebaSpider(object):
    def __init__(self):
        self.url='http://tieba.baidu.com/f?kw={}&pn={}'

    #1.请求
    def get_html(self,url):
        headers = {'User-Agent':random.choice(ua_list)}
        req=request.Request(url=url,headers=headers)
        resp = request.urlopen(req)
        html = resp.read().decode()
        return html
    #2.解析
    def perse_html(self):
        pass
    #3.保存
    def save_html(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)
    #4.入口函数
    def run(self):
        name=input('输入贴吧名：')
        begin=int(input('输入起页'))
        end=int(input('输入终止页'))
        params=parse.quote(name)
        #for循环：拼接地址，发请求，保存
        for i in range(begin,end+1):
            pn=(i-1)*50
            url=self.url.format(params,pn)
            html=self.get_html(url)
            filename=name+' %s页'%str(i)
            self.save_html(filename,html)
            print('%d页抓取成功'%i)
            # 每抓取1页随机休眠1-2秒钟
            # time.sleep(random.randint(1,2))
            time.sleep(random.uniform(0,1))

if __name__ == '__main__':
    spider=TiebaSpider()
    spider.run()
