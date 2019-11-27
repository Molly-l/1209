import redis
import pymysql

#1.

r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')
r.zadd('mobile-001',day01_dict)
r.zadd('mobile-002',day02_dict)
r.zadd('mobile-003',day03_dict)
