import requests
#用代理获取代理号，验证筛选可用的
class ProxyPool(object):
    def __init__(self):
        # 开放代理
        self.url = 'http://dev.kdlapi.com/api/getproxy/?orderid=967379014307497&num=30&protocol=2&method=2&an_an=1&an_ha=1&sep=1'
        # 私密代理
        self.url = 'http://dps.kdlapi.com/api/getdps/?orderid=987379589186512&num=30&pt=1&sep=1'
        self.headers = { 'User-Agent':'Mozilla/5.0' }
        self.f = open('proxyip.txt','a')




    def parse_html(self):
        html = requests.get(url=self.url,headers=self.headers).text
        # proxy_list: ['IP:Port','IP:Port']
        proxy_list = html.split('\r\n') #根据换行分隔元素  #\r行首 \n换行
        for proxy in proxy_list:
            # 测试proxy是否可用
            self.test_proxy(proxy)

    # 测试IP是否可用,可用则保存到文件
    def test_proxy(self,proxy):
        proxies = {
            'http':'http://309435365:szayclhp@{}'.format(proxy),
            'https':'https://309435365:szayclhp@{}'.format(proxy)
        }
        test_url = 'http://httpbin.org/get' #测试的网址，会将请求头作为消息返回
        try:
            res = requests.get( #既发送又接收，有异常会报错
                url=test_url,
                proxies=proxies,
                headers=self.headers,
                timeout=2
            )
            print(proxy,'成功')
            self.f.write(proxy + '\n')

        except Exception as e:
            print(proxy,'\033[42m失败\033[0m')

    def run(self):
        self.parse_html()
        # 所有ip测试完成后关闭文件
        self.f.close()

if __name__ == '__main__':
    spider = ProxyPool()
    spider.run()






















