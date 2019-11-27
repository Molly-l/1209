import redis
import pymysql

#1.

r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')
r.zadd('music:rank',{'song1':1,'song2':1,'song3':1})
r.zadd('music:rank',{'song4':1,'song5':1,'song6':1})
#增加播放次数
r.zincrby('music:rank',20,'song1')
r.zincrby('music:rank',50,'song2')
r.zincrby('music:rank',30,'song3')
#获取前三名：
r_list=r.zrevrange('music:rank',0,2,withscores=True)
i=1
for name in r_list:
    print('第名： 播放次数：'.format(i,
                             name[0].decode(),
                             int(name[1]),))
    i+=1