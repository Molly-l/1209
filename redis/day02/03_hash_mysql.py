import redis
import pymysql

#1.

r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')
#连接数据库
db=pymysql.connect('localhost','root','123456','userdb',charset='utf8')
cursor=db.cursor()
username=input('输入用户名')
res=r.hgetall(username)
if res:
    print('redis:',res)
else:
    sel='select age,score from user where name=%s'
    cursor.execute(sel,[username])#从mysql中查
    userinfo=cursor.fetchone()#从cursor中拿出第一个
    print('mysql',userinfo)
    r.hmset(username,{'age':userinfo[0],'score':userinfo})
    r.expire(username,30)