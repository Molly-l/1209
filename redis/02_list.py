import redis

r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')
r.rpush('tedu:teachers','laoqi','guo')
r.linsert('tedu:teachers','after','laoqi','tao')
r.ltrim('tedu:teachers',0,1)

while True:
    print(r.brpop('tedu:teachers',1))