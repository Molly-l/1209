import pymysql
import re
#连接数据库
db=pymysql.connect(user='root',
                   passwd='123456',
                   database='dict',
                   charset='utf8')
#获取游标
cur=db.cursor()
# with open('tu.jpg','rb') as f:
#     data=f.read()
#
# sql="insert into images values (1,%s)"
# cur.execute(sql,[data])

#提取图片
sql="select image from images where id=1;"
cur.execute(sql)#执行sql语句
r=cur.fetchone()
print(r)
with open('q.jpg','wb') as f:
    f.write(r[0])

# db.commit()提交

cur.close()
db.close()