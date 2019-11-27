from urllib import request

# urlopen() : 向URL发请求,返回响应对象
response=request.urlopen('http://httpbin.org/get')
# 提取响应内容/响应对象resp方法
html = response.read().decode('utf-8')
# 返回HTTP响应码
code = response.getcode()
# 返回实际数据的URL地址
url = response.geturl()
# 打印响应内容
print(html)

