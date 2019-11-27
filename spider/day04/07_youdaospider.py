import requests
import time
import random
from hashlib import md5
#借用有道翻译获取
class YoudaoSpider(object):
    def __init__(self):
        # post_url为F12抓包抓到的地址 headers -> General -> Request URL
        self.post_url = 'http://fanyi.youdao.com/' \
                        'translate_o?smartresult=dict&' \
                        'smartresult=rule'
        self.proxies = {#设置代理
            'http':'http://309435365:szayclhp@120.26.167.133:16817',
            'https':'https://309435365:szayclhp@120.26.167.133:16817'
        }
        self.headers = {
            # 检查频率最高的3个
            "Cookie": "OUTFOX_SEARCH_USER_ID=-1503804236@10.108.160.19; OUTFOX_SEARCH_USER_ID_NCOO=909810129.8233626; JSESSIONID=aaaZeLbI5jXLT_44xqU5w; ___rl__test__cookies=1573807897878",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",

        }

    # 获取salt,sign,ts
    def get_salt_sign_ts(self,word):
        ts = str(int(time.time()*1000)) #时间戳
        salt = ts + str(random.randint(0,9)) #时间戳+随机数
        string = "fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj" #验证
        s = md5() #s哈希对象
        s.update(string.encode()) #将需要进行摘要计算的字符串添加到s中
        sign = s.hexdigest()

        return ts,salt,sign

    # 主函数
    def attack_youdao(self,word):
        # 1. 先拿到salt,sign,ts
        ts,salt,sign = self.get_salt_sign_ts(word)
        # 2. 定义form表单数据为字典: data={}
        # 检查了salt sign
        # url headers formdata
        formdata = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": "57d46cf581e5c43f8109a84cf9227e5e",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        # 3. 直接发请求:requests.post(url,data=data,headers=xxx)
        html = requests.post(  #用异步方式发post请求，一般接收到的是json格式的数据
            url=self.post_url,
            data=formdata,
            proxies=self.proxies,
            headers=self.headers
        ).json() #将json格式的字符串转为python数据类型

        print('翻译结果:',html['translateResult'][0][0]['tgt'])

    def run(self):
        word = input('请输入要翻译的单词:')
        self.attack_youdao(word)

if __name__ == '__main__':
    spider = YoudaoSpider()
    spider.run()






