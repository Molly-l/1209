#把URL地址放到列表
import redis
import time
import random
r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')
url='http://app.mi.com/category/2#page={}'
for i in range(67):
    page_link=url.format(i)
    r.lpush('xiaomi:urls',page_link)
    time.sleep(random.randint(1,5))