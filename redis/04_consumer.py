import redis
r=redis.Redis(host='127.0.0.1',port=6379,db=0)
while True:
    res=r.brpop('xiaomi:urls',4)
    if res:
        print('正在抓取：',res[1].decode())
    else:
        print('抓取结束')
        break