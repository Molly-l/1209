import pymysql
#链接数据库
db=pymysql.connect(host='localhost',port=3306,\
                   user='root',
                   passwd='123456',
                   database='stu',
                   charset='utf8')
#获取游标
cur=db.cursor()
#执行语句
sql="insert into class02 values(6,'小亮',12,'w',78,'xxx');"
cur.execute(sql)
#提交到数据库
db.commit()
#关闭游标
cur.close()
#关闭数据库
db.close()
