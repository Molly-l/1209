import requests
#私密代理
url = 'https://www.xicidaili.com/'
headers = {'User-Agent':'Mozilla/5.0'}
proxies = { #用户名/密码/ip/端口号
    'http':'http://309435365:szayclhp@120.26.167.133:16817',
    'https':'https://309435365:szayclhp@120.26.167.133:16817'
}

html = requests.get(url=url,proxies=proxies,headers=headers).text
print(html)