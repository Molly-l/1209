import redis

#链接到数据库
r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')
#直接操作redis数据库db0
print(r.keys('*'))
key_list=r.keys('*')
for key in key_list:
    print(key.decode())

print(r.type('tedu:teachers'))
#exists()返回值0|1
print(r.exists('tedu:teachers'))
#删除
r.delete('tedu:teachers')
