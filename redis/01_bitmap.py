import redis

r=redis.Redis(host='localhost',port=6379,db=0,password=123456)
#
r.setbit('user:001',0,1)
r.setbit('user:001',29,1)

r.setbit('user:002',199,1)

for i in range(0,365,2):#2，步长
    r.setbit('user:003',i,1)

for i in range(0,365,3):
    r.setbit('user:004',i,1)

user_list=r.keys('user:*')
print(user_list)
