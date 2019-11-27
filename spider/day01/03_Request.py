from urllib import request

url='http://httpbin.org/get'
headers={'User-Agent':''}
# 1.创建请求对象(重构User-Agent)
req=request.Request(url=url,headers=headers)
# 2.发请求获取响应对象(urlopen)
resp=request.urlopen(req)
# 3.获取响应对象内容
html = resp.read().decode('utf-8')
print(html)