#写操作演示（insert ）
import pymysql

#连接数据库
db=pymysql.connect(user='root',
                   passwd='123456',
                   database='stu',
                   charset='utf8')
#获取游标
cur=db.cursor()
#执行sql语句
name=input('name:')
price=float(input('price:'))
comment=input('comment:')
# sql='insert into interest (id,name,hobby,level,price,comment) vlues \
#     (%d,"%s","%s",%d,%f)'

sql='insert into interest values(50,"%s","sing","kk",%f,"%s");'%(name,price,comment)

# cur.execute(sql,[103,"fgh","draw",6,20.05])#执行语句
cur.execute(sql)
#修改操作
# sql="update interest where name='cvb'"
# cur.execute(sql)
#
# #删除操作
# sql="delete interest where name='sd'"
# cur.execute(sql)

db.commit()#同步数据库
cur.close()
db.close()