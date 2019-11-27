import requests
import re

url = 'http://www.baidu.com/'
headers = {
    'User-Agent':'xxxxxxxxxxxxxx'
}
resp = requests.get(url=url,headers=headers)
# 响应对象resp属性
resp.encoding = 'utf-8' #设置响应的编码方式
html = resp.text #获取响应值
print(html)


html = resp.content #获取整个响应的字节串
code = resp.status_code #获取状态码 200/400
url = resp.url



html = requests.get(url=url,headers=headers).text




