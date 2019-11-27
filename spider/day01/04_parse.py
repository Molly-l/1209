from urllib import request, parse

#拼接url地址
word=input('输入搜索内容：')
# params=parse.urlencode({'wd':word})
params=parse.quote(word)

# url='http://www.baidu.com/s?{}'
url='http://www.baidu.com/s?wd={}'
url=url.format(params)


# 2.发请求获取响应内容
headers={'User-Agent':'Mozilla/5.0'}
req=request.Request(url=url,headers=headers)
resp=request.urlopen(req)
html = resp.read().decode('utf-8')
# 3.保存到本地文件
filename=word+'.html'
with open(filename,'w') as f:
    f.write(html)