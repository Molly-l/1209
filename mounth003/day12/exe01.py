import pymysql
import re

#连接数据库
db=pymysql.connect(user='root',
                   passwd='123456',
                   database='country',
                   charset='utf8')
#获取游标
cur=db.cursor()

sql="insert into student (name,gender) values(%s,%s);"
try:
    for i in range(2000000):
        name='name'+str(i)
        gender='m'
        cur.execute(sql,[name,gender])#执行sql语句
    db.commit()
except:
    db.rollback()#回滚

db.close()