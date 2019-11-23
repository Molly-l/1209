import pymysql
import re

#连接数据库
db=pymysql.connect(user='root',
                   passwd='123456',
                   database='dict',
                   charset='utf8')
#获取游标
cur=db.cursor()

sql="insert into words (word,mean) values(%s,%s);"
f=open('dict.txt','r')
for line in f:
    # list01=line.split(' ')
    # word=list01[0]
    # mean=list01[1].strip()
    # cur.execute(sql,[word,mean])
    tup=re.findall(r'(\S+)\s+(.*)',line)[0]

    cur.execute(sql,tup)
try:
    db.commit()
except:
    db.rollback()

cur.close()
db.close()