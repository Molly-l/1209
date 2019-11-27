from urllib import request
from fake_useragent import UserAgent  # 可以在线生成一个User-Agent请求头
import re


class MaoYan:

    # 1.定义常用变量
    url = 'https://maoyan.com/board/4?offset=0'
    headers = {'User-Agent': UserAgent().random}  #
    # 2.请求获取html
    req = request.Request(url=url, headers=headers)
    resp = request.urlopen(req)
    html = resp.read().decode()

    # re_bds='<div class="movie-item-info">' \
    #        '.*?title="(.*?)" .*?' \
    #        '<p class="star"> (.*?) </p>.*?' \
    #        '<p class="releasetime">(.*?)</p>'
    # 3.解析提取数据re
    re_bds = '''<div class="movie-item-info">
            <p class="name"><a href="/films/3667" title="(.*?)" data-act="boarditem-click" data-val="{movieId:3667}">辛德勒的名单</a></p>
            <p class="star">
                    (.*?)
            </p>
    <p class="releasetime">(.*?)</p>'''

    p = re.compile(re_bds, re.S)  # re.S 匹配换行符
    print(html)
    r_list = p.findall(html)
    print(r_list)
    # 4.保存到本地文件
    with open('film.txt', 'a') as f:  # with语句中f自动关闭, 'a'追加
        for r in r_list:
            f.write(
                r[0] + '\t' +
                r[1].strip() + '\t' +
                r[2].strip()[5:15] + '\n'
            )