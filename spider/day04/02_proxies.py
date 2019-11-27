import requests
import json
#普通代理
url = 'http://httpbin.org/get'
headers = { 'User-Agent': 'xxxxxx' }
proxies = { #设置代理
    'http' : 'http://116.21.122.74:808',
    'https' : 'https://116.21.122.74:808'#https比http更安全
}
resp = requests.get(url=url,proxies=proxies,headers=headers).text

#json=resp.json()
html = resp.text
# python1 =json.loads(html)
print(html)

















