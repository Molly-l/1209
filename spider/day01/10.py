# re='''<div class="movie-item-info">
#         <p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click"
#         data-val="{movieId:1203}">霸王别姬</a></p>
#         <p class="star">
#                 主演：张国荣,张丰毅,巩俐
#         </p>
# <p class="releasetime">上映时间：1993-07-26</p>    </div>
# '''



from urllib import request
from fake_useragent import UserAgent #可以在线生成一个User-Agent请求头
import re
# 1.定义常用变量
url='https://maoyan.com/board/4?offset=0'
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'} #
# 2.请求获取html
req=request.Request(url=url,headers=headers)
resp=request.urlopen(req)
html=resp.read().decode()

# re_bds='<div class="movie-item-info">' \
#        '.*?title="(.*?)" .*?' \
#        '<p class="star"> (.*?) </p>.*?' \
#        '<p class="releasetime">(.*?)</p>'
# 3.解析提取数据re
re_bds='''<div class="movie-item-info">.*?title="(.*?)" data.*?"star">(.*?)</p.*?">(.*?)</p>'''
# re_bds='''<div class="movie-item-info">
#         <p class="name"><a href="/films/3667" title="(.*?)" data-act="boarditem-click" data-val="{movieId:3667}">辛德勒的名单</a></p>
#         <p class="star">
#                 (.*?)
#         </p>
# <p class="releasetime">(.*?)</p>'''

p=re.compile(re_bds,re.S)#re.S 匹配换行符
print(html)
r_list=p.findall(html)
print(r_list)
# 4.保存到本地文件
with open('film.txt','a') as f: #with语句中f自动关闭, 'a'追加
        for r in r_list:
                f.write(
                        r[0]+'\t'+
                        r[1].strip()+'\t'+
                        r[2].strip()[5:15]+'\n'
                )